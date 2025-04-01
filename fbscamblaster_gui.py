#!/usr/bin/env python3
# fbscamblaster_gui.py
import tkinter as tk
from tkinter import ttk, scrolledtext
from fbscamblaster_core import report_profile

def start_blasting():
    """Kick off the reporting process from the GUI."""
    profile_url = url_entry.get()
    report_count = int(count_entry.get() or 200)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "[CHEEKY] Engaging target...\n")
    root.update()
    report_profile(profile_url, report_count, lambda msg: output_text.insert(tk.END, msg + "\n") or output_text.see(tk.END))

# Build the UI
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
