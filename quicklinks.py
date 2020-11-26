#! /usr/bin/env python3
import webbrowser, subprocess, os, pyautogui, time, threading
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def getData():
    with open(os.path.join(os.path.expanduser("~/Documents"),'data.config'), 'r') as source:
        rawSource = eval(source.readline())
    return rawSource

# --- Button 1 ---
# opens all work related websites in one button click

def workSites():
    for items in (getData()[0]):
        webbrowser.open(items)

# --- Button 2 ---
# opens all work related apps/tools in one button click

def workApps():
    for items in (getData()[1]):
        app = "/Applications/" + items + ".app/"
        os.chdir(".")
        subprocess.Popen(['open', app])

# --- Button 3 ---
# quick access internal or external search queries

def quickLink():
    while True:
        searchEntry = simpledialog.askstring("Search", "Enter search keywords:")
        if searchEntry == "":
            messagebox.showinfo(" ", "No keyword entered.")
            continue
        if searchEntry == None:
            return
        quickLink = 'https://www.google.com/search?q=' + searchEntry # you can use replace this with internal knowledge base or repository
        webbrowser.open(quickLink)
        return

# --- Button 4 ---
# quick access to scheduled weekly/monthly meetings

def meetings():
    def getlink():
        link = linklist.curselection()
        pos = 0
        for items in link:
            indx = int(items) - pos
            meetinglink = ((getData()[2])[indx])
            webbrowser.open(meetinglink)
            pop.destroy()

    counter = 0

    pop = tk.Toplevel()
    pop.title("Meeting links")
    pop.geometry("+150+178")

    topframe = tk.Frame(pop)
    topframe.pack(pady = 5)
    botframe = tk.Frame(pop)
    botframe.pack()
    linklist = tk.Listbox(topframe, height=3, width=21, bd=0)
    for items in getData()[3]:
        linklist.insert(counter, ("  " + items))
        counter += 1
    linklist.pack(fill="y", side=LEFT)
    sb = tk.Scrollbar(topframe)
    sb.pack(side=LEFT)
    linklist.config(yscrollcommand=sb.set)
    sb.config(command=linklist.yview)
    cancel = tk.Button(botframe, text="Cancel", command=pop.destroy, height=1, width=9)
    cancel.pack(side=RIGHT, padx=8, pady=8)
    okbtn = tk.Button(botframe, text="OK", command=getlink, height=1, width=9)
    okbtn.pack(side=RIGHT, pady=8)

# --- Button 5 ---

def settings():
    try:
        with open(os.path.join(os.path.expanduser("~/Documents"),'data.config'), 'r') as source:
            rawSource = eval(source.readline())
    except FileNotFoundError:
        rawSource = [[],[],[],[]]

    websites = rawSource[0]
    apps = rawSource[1]
    meeting = rawSource[2]
    alias = rawSource[3]

    counter = 0

    def addSite():
        site = entry1.get()
        websites.append(site)
        sitelist1.insert(END, websites[-1])
        entry1.delete(0, 'end')

    def addApps():
        site = entry2.get()
        apps.append(site)
        sitelist2.insert(END, apps[-1])
        entry2.delete(0, 'end')

    def addLink():
        while True:
            site = entry3.get()
            if site == "":
                messagebox.showinfo("", "No link entered.")
                break
            while True:
                answer = simpledialog.askstring("Meeting Name", "Create a name for this link:")
                if answer == None:
                    return
                if answer != "":
                    meeting.append(site)
                    alias.append(answer)
                    sitelist3.insert(END, alias[-1])
                    entry3.delete(0, 'end')
                    return
                else:
                    messagebox.showinfo("", "Name required.")
                    continue

    def deleteSite():
        sites = sitelist1.curselection()
        pos = 0
        for items in sites:
            indx = int(items) - pos
            sitelist1.delete(indx, indx)
            websites.pop(indx)
            pos =+ 1

    def deleteApp():
        sites = sitelist2.curselection()
        pos = 0
        for items in sites:
            indx = int(items) - pos
            sitelist2.delete(indx, indx)
            apps.pop(indx)
            pos =+ 1

    def deleteLink():
        sites = sitelist3.curselection()
        pos = 0
        for items in sites:
            indx = int(items) - pos
            sitelist3.delete(indx, indx)
            meeting.pop(indx)
            alias.pop(indx)
            pos =+ 1

    def exportData():
        rawData = [websites, apps, meeting, alias]
        with open(os.path.join(os.path.expanduser("~/Documents"),'data.config'), 'w') as configFile:
            configFile.write(str(rawData))
        if save['text'] == "SAVE":
            messagebox.showinfo("", "Config File created in Documents folder.")
        else:
            messagebox.showinfo("", "Config File successfully updated.")
        settings.destroy()

    def clearEntry1(event):
        entry1.delete(0, END)
        entry1.config(fg="black")
        return

    def clearEntry2(event):
        entry2.delete(0, END)
        entry2.config(fg="black")
        return

    #--- Parent ---

    settings = tk.Toplevel()
    settings.title("SETTINGS")
    settings.geometry("540x510+450+100")

    #--- 1st Row ---

    labelFrame = tk.LabelFrame(settings, text="Work Sites")
    labelFrame.pack(fill="both", padx = 10, pady = 5)
    bottomframe = Frame(labelFrame)
    bottomframe.pack(side=BOTTOM, ipady=5)
    label1 = tk.Label(labelFrame, text="Add work sites:")
    label1.pack(side=LEFT)
    entry1 = tk.Entry(labelFrame, bd=3, width=31, fg="gray")
    entry1.insert(0, " Sample: https://cash.bitaccessbtm.com/")
    entry1.pack(side=LEFT)
    entry1.bind('<Button-1>', clearEntry1)
    addbtn1 = tk.Button(labelFrame, text="+", command=addSite, height=1, width=2)
    addbtn1.pack(side=LEFT)
    sitelist1 = tk.Listbox(bottomframe, height=5, width=32)
    for items in websites:
        sitelist1.insert(counter, items)
        counter += 1
    sitelist1.pack(side=LEFT)
    sb1 = tk.Scrollbar(bottomframe)
    sb1.pack(side=LEFT)
    sitelist1.config(yscrollcommand=sb1.set)
    sb1.config(command=sitelist1.yview)
    rmwbtn1 = tk.Button(labelFrame, text="-", command=deleteSite, height=1, width=2)
    rmwbtn1.pack(side=LEFT)

    #--- 2nd Row ---

    labelFrame = tk.LabelFrame(settings, text="Work Apps")
    labelFrame.pack(fill="both", padx = 10, pady = 5)
    bottomframe = Frame(labelFrame)
    bottomframe.pack(side=BOTTOM, ipady=5)
    label2 = tk.Label(labelFrame, text="Add work apps:")
    label2.pack(side=LEFT)
    entry2 = tk.Entry(labelFrame, bd=3, width=31, fg="gray")
    entry2.insert(0, " Sample: Slack, VNC Viewer")
    entry2.pack(side=LEFT)
    entry2.bind('<Button-1>', clearEntry2)
    addbtn2 = tk.Button(labelFrame, text="+", command=addApps, height=1, width=2)
    addbtn2.pack(side=LEFT)
    sitelist2 = tk.Listbox(bottomframe, height=5, width=32)
    for items in apps:
        sitelist2.insert(counter, items)
        counter += 1
    sitelist2.pack(side=LEFT)
    sb2 = tk.Scrollbar(bottomframe)
    sb2.pack(side=LEFT)
    sitelist2.config(yscrollcommand=sb2.set)
    sb2.config(command=sitelist2.yview)
    rmwbtn2 = tk.Button(labelFrame, text="-", command=deleteApp, height=1, width=2)
    rmwbtn2.pack(side=LEFT)

    #--- 3rd Row ---

    labelFrame = tk.LabelFrame(settings, text="Meeting Links")
    labelFrame.pack(fill="both", padx = 10, pady = 5)
    bottomframe = Frame(labelFrame)
    bottomframe.pack(side=BOTTOM, ipady=5)
    label3 = tk.Label(labelFrame, text=" Add link:           ")
    label3.pack(side=LEFT)
    entry3 = tk.Entry(labelFrame, bd=3, width=31)
    entry3.pack(side=LEFT)
    addbtn3 = tk.Button(labelFrame, text="+", command=addLink)
    addbtn3.pack(side=LEFT)
    sitelist3 = tk.Listbox(bottomframe, height=5, width=33)
    sitelist3.pack(side=LEFT)
    for items in alias:
        sitelist3.insert(counter, items)
        counter += 1
    sitelist3.pack(side=LEFT)
    sb3 = tk.Scrollbar(bottomframe)
    sb3.pack(side=LEFT)
    sitelist3.config(yscrollcommand=sb3.set)
    sb3.config(command=sitelist3.yview)
    rmwbtn3 = tk.Button(labelFrame, text="-", command=deleteLink, height=1, width=2)
    rmwbtn3.pack(side=LEFT)
    
    #--- Apply/Cancel ---

    finalFrame = Frame(settings)
    finalFrame.pack(side=RIGHT)
    cancel = tk.Button(finalFrame, text="CANCEL", command=settings.destroy)
    cancel.pack(side=RIGHT, padx = 15, pady = 10)
    save = tk.Button(finalFrame, text="SAVE", command=exportData)
    save.pack(side=RIGHT)
    if os.path.exists(os.path.expanduser("~/Documents/data.config")):
        save.config(text= "UPDATE")

    settings.mainloop()

# --- Button 6 ---
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
btn5 = tk.Button(text="SETTINGS", command=settings, width=22, height=1, fg='orange')
btn5.pack(expand=True, padx=40, pady=10)
btn6 = tk.Button(text="EXIT", command=exit, width=22, height=1, fg='blue')
btn6.pack(expand=True, padx=40, pady=10)

if os.path.exists(os.path.expanduser("~/Documents/data.config")):
    main.mainloop()
else:
    settings()