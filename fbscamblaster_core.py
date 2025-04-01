# fbscamblaster_core.py
import requests
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
import time
import random
import re

def renew_tor_ip():
    """Rotate Tor IP for stealth."""
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    time.sleep(5)

def get_headers():
    """Generate fake headers to mimic a real user."""
    ua = UserAgent()
    return {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://www.facebook.com/'
    }

def get_user_id(profile_url):
    """Extract user ID from a Facebook profile URL."""
    match = re.search(r'(facebook\.com\/(?:profile\.php\?id=)?)([\w\d]+)', profile_url)
    return match.group(2) if match else None

def report_profile(profile_url, report_count, output_callback):
    """Hammer the target profile with reports."""
    user_id = get_user_id(profile_url)
    if not user_id:
        output_callback("[CHEEKY] Invalid URL. Fix your target, you dumb fuck.")
        return

    session = requests.Session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
    report_url = "https://www.facebook.com/ajax/report.php"  # Sniff the real endpoint
    reasons = ["Scam", "Fake account", "Spam", "Fraud"]

    for i in range(report_count):
        headers = get_headers()
        payload = {
            'user_id': user_id,
            'reason': random.choice(reasons),
            'source': 'profile',
            'rand_id': random.randint(1000, 9999)
        }
        
        try:
            response = session.post(report_url, headers=headers, data=payload, timeout=10)
            output_callback(f"[CHEEKY] Report {i+1}/{report_count} sent. Status: {response.status_code}")
        except Exception as e:
            output_callback(f"[CHEEKY] Shit broke: {e}")
        
        if i % 5 == 0:
            renew_tor_ip()
        time.sleep(random.uniform(1, 3))

    output_callback(f"[CHEEKY] Target {profile_url} hit hard. Job done, you savage fuck.")
