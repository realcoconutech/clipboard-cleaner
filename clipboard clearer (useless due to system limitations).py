import tkinter as tk
from tkinter import *
import time
import ctypes
from ctypes import *

interval = 300
running = True

def start_cleaning():
    global running
    running = True
    print("Cleaning Starting...")
    windll.user32.OpenClipboard(0)
    windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()
    print("Clipboard Cleared.")
    time.sleep(interval)

def stop_cleaning():
    global running
    running = False
    print("Stop cleaning loop.")

def clean_now():
    windll.user32.OpenClipboard(0)
    windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()
    print("Clipboard Cleared.")

root = tk.Tk()
root.title("Throttle Clipboard Cleaner")
root.geometry("600x400")
info_label = tk.Label(root, text="Choose an action")
info_label.pack()
btn = tk.Button(root, text="Start", command=start_cleaning)
btn.pack()
btn1 = tk.Button(root, text="Stop", command=stop_cleaning)
btn1.pack()
btn2 = tk.Button(root, text="Clear Now", command=clean_now)
btn2.pack()
root.mainloop()