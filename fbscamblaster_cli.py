#!/usr/bin/env python3
# fbscamblaster_cli.py
from fbscamblaster_core import report_profile

if __name__ == "__main__":
    print("[CHEEKY] FBScamBlaster CLI - Ready to fuck up scammers.")
    profile_url = input("[CHEEKY] Drop the scam URL: ")
    report_count = int(input("[CHEEKY] Report count (default 200): ") or 200)
    print("[CHEEKY] Engaging target...")
    report_profile(profile_url, report_count, print)
