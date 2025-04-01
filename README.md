# FBScamBlaster - CHEEKY Edition
**Take down scammers with precision.**  
Created by CHEEKY for cheekydavy, FBScamBlaster is a powerful tool designed to target and report scam profiles on Facebook until they’re banned. Featuring a sleek GUI, Tor-powered anonymity, and cross-platform support for Kali Linux and Termux, this tool is your weapon against online fraud. Clone it, run it, and make scammers regret their choices.

---

## Features
- **Intuitive UI**: A sharp, neon-green interface with a bold “Take ‘Em Down” button.
- **Mass Reporting**: Defaults to 200 reports—adjustable for maximum impact.
- **Stealth Capabilities**: Tor integration rotates IPs to keep you under the radar.
- **Cross-Platform**: Fully compatible with Kali Linux and Termux.
- **Open Source**: Hosted on GitHub—clone, customize, and deploy.

---

## Prerequisites
Before you get started, install these dependencies. Copy and paste the commands below based on your platform.

### Kali Linux
```bash
sudo apt update && sudo apt install -y python3 python3-pip tor python3-tk
pip3 install requests fake_useragent stem
Termux (Android)
bash

Collapse

Wrap

Copy
pkg update && pkg install -y python tor python-tkinter
pip install requests fake_useragent stem
Installation
Set up the tool in a few simple steps.

Clone the Repository
Grab the code from GitHub:
bash

Collapse

Wrap

Copy
git clone https://github.com/cheekydavy/FBScamBlaster.git
cd FBScamBlaster
Set Permissions
Ensure the script is executable:
bash

Collapse

Wrap

Copy
chmod +x fbscamblaster_gui.py
Usage
Follow these steps to launch FBScamBlaster and target a scam profile.

On Kali Linux
Start Tor
Enable Tor for IP rotation:
bash

Collapse

Wrap

Copy
sudo service tor start
Run the Tool
Launch the GUI:
bash

Collapse

Wrap

Copy
python3 fbscamblaster_gui.py
On Termux
Start Tor
Run Tor in the background:
bash

Collapse

Wrap

Copy
tor &>/dev/null &
(Optional: Verify with termux-toast "Tor is active".)
Run the Tool
Launch the GUI:
bash

Collapse

Wrap

Copy
python3 fbscamblaster_gui.py
Using the Interface
Enter the scam profile URL (e.g., https://facebook.com/scammy.profile).
Specify the report count (defaults to 200—adjust as needed).
Click “Take ‘Em Down” to initiate the reporting process.
Monitor progress in the live output window.
