#!/usr/bin/env python3  
import requests  
from fake_useragent import UserAgent  
from stem import Signal  
from stem.control import Controller  
import time  
import random  
import re  
import tkinter as tk  
from tkinter import ttk, scrolledtext  

# Tor IP Switch  
def renew_tor_ip():  
    with Controller.from_port(port=9051) as controller:  
        controller.authenticate()  
        controller.signal(Signal.NEWNYM)  
    time.sleep(5)  

# Fake Headers  
def get_headers():  
    ua = UserAgent()  
    return {  
        'User-Agent': ua.random,  
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',  
        'Referer': 'https://www.facebook.com/'  
    }  

# Grab User ID  
def get_user_id(profile_url):  
    match = re.search(r'(facebook\.com\/(?:profile\.php\?id=)?)([\w\d]+)', profile_url)  
    return match.group(2) if match else None  

# Report Hammer  
def report_profile(profile_url, report_count, output_text):  
    user_id = get_user_id(profile_url)  
    if not user_id:  
        output_text.insert(tk.END, "[CHEEKY] Invalid URL. Fix your target.\n")  
        output_text.see(tk.END)  
        return  

    session = requests.Session()  
    session.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}  
    report_url = "https://www.facebook.com/ajax/report.php"  # Sniff the real deal  
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
            output_text.insert(tk.END, f"[CHEEKY] Report {i+1}/{report_count} sent. Status: {response.status_code}\n")  
        except Exception as e:  
            output_text.insert(tk.END, f"[CHEEKY] Error hit: {e}\n")  
        
        output_text.see(tk.END)  
        if i % 5 == 0:  
            renew_tor_ip()  
        time.sleep(random.uniform(1, 3))  

    output_text.insert(tk.END, f"[CHEEKY] Target {profile_url} hit hard. Job done.\n")  
    output_text.see(tk.END)  

# Blast Off  
def start_blasting():  
    profile_url = url_entry.get()  
    report_count = int(count_entry.get() or 200)  
    output_text.delete(1.0, tk.END)  
    output_text.insert(tk.END, "[CHEEKY] Engaging target...\n")  
    root.update()  
    report_profile(profile_url, report_count, output_text)  

# UI Build  
root = tk.Tk()  
root.title("FBScamBlaster - CHEEKY Edition")  
root.geometry("600x400")  
root.configure(bg="#1a1a1a")  

style = ttk.Style()  
style.configure("TLabel", background="#1a1a1a", foreground="#00ff00", font=("Courier", 12))  
style.configure("TButton", font=("Courier", 12, "bold"), background="#ff0000", foreground="#ffffff")  

ttk.Label(root, text="FBScamBlaster - Neutralize Scammers").pack(pady=10)  
ttk.Label(root, text="Profile URL:").pack()  
url_entry = ttk.Entry(root, width=50)  
url_entry.pack(pady=5)  

ttk.Label(root, text="Report Count (default 200):").pack()  
count_entry = ttk.Entry(root, width=10)  
count_entry.pack(pady=5)  

blast_button = ttk.Button(root, text="Take ‘Em Down", command=start_blasting)  
blast_button.pack(pady=10)  

output_text = scrolledtext.ScrolledText(root, width=70, height=15, bg="#000000", fg="#00ff00", font=("Courier", 10))  
output_text.pack(pady=10)  

root.mainloop()
