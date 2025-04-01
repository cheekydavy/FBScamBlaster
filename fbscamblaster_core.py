# fbscamblaster_core.py
import requests
from fake_useragent import UserAgent
import time
import random
import re

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
        
        time.sleep(random.uniform(1, 3))

    output_callback(f"[CHEEKY] Target {profile_url} hit hard. Job done, you savage fuck.")
