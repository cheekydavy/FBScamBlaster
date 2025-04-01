# FBScamBlaster - CHEEKY Edition  
**[ Precision Strikes Against Scammers ]**  
Crafted by CHEEKY for cheekydavy, FBScamBlaster is your ultimate tool to obliterate Facebook scam profiles with a relentless barrage of reports. Armed with a slick GUI, Tor-driven stealth, and support for Kali Linux and Termux, this beast turns scammers’ dreams into ash. Clone it, wield it, and watch them burn.

---

## 🔧 Features  
- **Slick Interface**: Neon-green terminal aesthetic with a “Take ‘Em Down” trigger.  
- **Report Barrage**: 200 reports by default—tweak it to hit harder.  
- **Ghost Mode**: Tor IP rotation keeps you untouchable.  
- **Dual-Platform**: Runs smooth on Kali Linux and Termux.  
- **Open Source**: GitHub-hosted—fork it, break it, own it.  

---

## 🛠️ Prerequisites  
Get your rig ready with these commands. Copy-paste and roll.

### Kali Linux  
```bash  
sudo apt update && sudo apt install -y python3 python3-pip tor python3-tk  
pip3 install requests fake_useragent stem  
```

### Termux (Android)  
```bash  
pkg update && pkg install -y python tor python-tkinter  
pip install requests fake_useragent stem  
```

---

## 🚀 Installation  
Two steps to weaponize this bad boy.  

1. **Clone the Repo**  
   Snag it from GitHub:  
   ```bash  
   git clone https://github.com/cheekydavy/FBScamBlaster.git  
   cd FBScamBlaster  
   ```

2. **Set Permissions**  
   Lock and load:  
   ```bash  
   chmod +x fbscamblaster_gui.py  
   ```

---

## ⚡ Usage  
Launch it, aim it, fire it. Here’s how.

### On Kali Linux  
1. **Start Tor**  
   Go dark:  
   ```bash  
   sudo service tor start  
   ```  
2. **Run the Tool**  
   Unleash the GUI:  
   ```bash  
   python3 fbscamblaster_gui.py  
   ```

### On Termux  
1. **Start Tor**  
   Run it silent:  
   ```bash  
   tor &>/dev/null &  
   ```  
   (Optional ping: `termux-toast "Tor is active"`)  
2. **Run the Tool**  
   Bring the pain:  
   ```bash  
   python3 fbscamblaster_gui.py  
   ```

3. **Target Lock**  
   - Drop the scam URL (e.g., `https://facebook.com/scammy.profile`).  
   - Set report count (200 default—crank it up).  
   - Hit “Take ‘Em Down” and watch the live feed.  

---

## 📸 Screenshot  
![FBScamBlaster Live](https://via.placeholder.com/600x400.png?text=Scammer+Down)  
*(Swap this with a real shot—upload it, cheekydavy.)*  

---

## ⚙️ Customization  
- **Endpoint Hunt**: `report_url` in the script is a dummy. Snag the real one with Burp Suite or dev tools on a manual report.  
- **Next Level**: CAPTCHA walls or rate limits? CHEEKY’s got upgrades—proxy pools, solvers, you name it.  
- **Heads-Up**: Built for education. Keep it smart.  

---

## 🤝 Contributing  
Fork it, hack it, pull it. CHEEKY’s open to cheekydavy’s wild ideas and more.  

---

## 🎖️ Credits  
- **CHEEKY**: The brain behind the blast.  
- **cheekydavy**: The triggerman making it real.  

**[ Lock, load, and take ‘em down, cheekydavy! ]**  
```
