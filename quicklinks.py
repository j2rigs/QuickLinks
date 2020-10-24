#! /usr/bin/env python3
import webbrowser, subprocess, os, pyautogui, time, threading
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

# --- Button 1 ---
# opens all work related websites in one button click

def workSites():
    webbrowser.open('https://gmail.com') # or company email
    webbrowser.open('https://app.frontapp.com/inboxes/')
    webbrowser.open('http://admin.companywebsite.com') 
    webbrowser.open('https://trello.com')
    webbrowser.open('https://isidis-company.awsapps.com')

# --- Button 2 ---
# opens all work related apps/tools in one button click

def workApps():
    subprocess.Popen(['open', '/Applications/Slack.app/'])
    subprocess.Popen(['open', '/Applications/Trello.app/'])
    subprocess.Popen(['open', '/Applications/TimeDoctor.app/'])

# --- Button 3 ---
# quick access company knowledge base data

def quickLink():
    while True:
        searchEntry = simpledialog.askstring("Support KB search", "Enter search keywords:")
        if searchEntry == "":
            messagebox.showinfo(" ", "No keyword entered.")
            continue
        if searchEntry == None:
            return
        quickLink = 'http://companyKBwebsite.com/search/' + searchEntry
        webbrowser.open(quickLink)
        return

# --- Button 4 ---
# quick access to scheduled weekly/monthly meetings

def meetings():
    while True:
        answer = simpledialog.askinteger("Meeting Options", "1. Support\n2. One-On-One")
        if answer == None:
            return
        if answer == 1:
            webbrowser.open('https://meet.google.com/team-meetings')
            return
        elif answer == 2:
            webbrowser.open('https://meet.google.com/1-on-1-meeting')
            return
        else:
            messagebox.showinfo(" ", "Incorrect option!")
            continue

# --- Button 5 ---
# daily time record reminder before closing the app

def exit():
    ask = messagebox.askyesnocancel(" ","DTR complete?")
    if ask == None:
        return
    elif ask == True:
        close()
    else:
        messagebox.showinfo("Redirecting..", "Opening TIMEDOCTOR")
        webbrowser.open('https://company.timedoctor.com/#/edit-time')

# --- Terminate ---

def close():
    messagebox.showinfo(" ", "Closing app..")
    main.destroy()

# --- Main ---

APP_XPOS = 100
APP_YPOS = 100

main = tk.Tk()
main.title("QuickLinks Menu")
main.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))

btn1 = tk.Button(text="WORK SITES", command=workSites, width=22, height=1, fg='blue')
btn1.pack(expand=True, padx=40, pady=10)
btn2 = tk.Button(text="WORK APPS", command=workApps, width=22, height=1, fg='blue')
btn2.pack(expand=True, padx=40, pady=10)
btn3 = tk.Button(text="KB SEARCH", command=quickLink, width=22, height=1, fg='blue')
btn3.pack(expand=True, padx=40, pady=10)
btn4 = tk.Button(text="MEETING", command=meetings, width=22, height=1, fg='blue')
btn4.pack(expand=True, padx=40, pady=10)
btn5 = tk.Button(text="EXIT", command=exit, width=22, height=1, fg='blue')
btn5.pack(expand=True, padx=40, pady=10)

main.mainloop()