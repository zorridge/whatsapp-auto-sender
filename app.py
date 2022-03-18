from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import csv
import threading
import webbrowser as web
from urllib.parse import quote
from platform import system
from pyautogui import click, press, hotkey, size
from sys import exit

WIDTH, HEIGHT = size()
sending = False
killing = False


def closeTab(waitTime: int = 2):
    time.sleep(waitTime)
    if system().lower() in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif system().lower() == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")
    press("enter")


def sendWhatsappMessage(
    number: str,
    message: str,
    waitTime: int = 15,
    tabClose: bool = False,
    closeTime: int = 3,
):
    if sending:
        web.open(f"https://web.whatsapp.com/send?phone={number}&text={quote(message)}")
        time.sleep(4)
        if sending:
            click(WIDTH / 2, HEIGHT / 2)
        time.sleep(waitTime - 4)
        if sending:
            click(WIDTH / 2, HEIGHT / 2)
        if sending:
            press("enter")
            if tabClose:
                closeTab(waitTime=closeTime)
        else:
            print("fn sendWhatsappMessage() stopped...")


def send():
    global sending
    message = text.get("1.0", "end")
    delay = int(timeEntry.get()) if timeEntry.get() else 15
    text["state"] = "disabled"
    sendStart["state"] = "disabled"
    timeEntry["state"] = "disabled"
    with open("merchantContact.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if sending:
                name = str(row["merchantName"])
                number = "+" + str(row["merchantNumber"])
                messageSent = f"Hi there owner of {name}!\n\n{message}"
                sendWhatsappMessage(number, messageSent, delay, True, 5)
            else:
                print("fn send() stopped...")
                break
    sending = False
    global killing
    killing = False
    text["state"] = "normal"
    sendStart["state"] = "normal"
    sendEnd["state"] = "disabled"
    timeEntry["state"] = "normal"
    status.set("Script stopped...")
    print("Script stopped...")


def sendThread():
    global sending
    sending = True
    global killing
    killing = False
    status.set("Script running...")
    print("Script running...")
    t1 = threading.Thread(target=send)
    t1.start()
    sendEnd["state"] = "normal"


def stop():
    global sending
    sending = False
    global killing
    killing = True
    sendEnd["state"] = "disabled"
    status.set("Kill request received...")
    print("Kill request received...")


def on_close():
    if sending or killing:
        close = messagebox.showwarning(
            title="Error",
            message="Can't close this app!",
            detail="Script is still running, please kill it before closing the app!",
        )
        if close:
            pass
    else:
        root.destroy()


root = Tk()
root.title("AutoWhatsApp")
root.iconbitmap("./whatsapp.ico")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)

textLabel = ttk.Label(mainframe, text="Enter your message here:")
textLabel.grid(column=0, row=0, pady=[10, 0])

text = Text(mainframe, width=40, height=10, relief="solid", wrap="word")
text.configure(font=("Tahoma", 10, "normal"))
text.grid(column=0, row=1, sticky=(N, S, E, W), padx=[18, 10], pady=10)

ys = ttk.Scrollbar(mainframe, orient="vertical", command=text.yview)
text["yscrollcommand"] = ys.set
ys.grid(column=1, row=1, sticky="ns")

timeLabel = ttk.Label(mainframe, text="Set delay (seconds):")
timeLabel.grid(column=0, row=2)

timeDelay = StringVar()
timeEntry = ttk.Entry(mainframe, textvariable=timeDelay, width=5, justify="center")
timeEntry.grid(column=0, row=3, pady=10)

sendStart = ttk.Button(mainframe, text="Submit", command=sendThread)
sendStart.grid(column=0, row=4, pady=5)

sendEnd = ttk.Button(mainframe, text="Kill", command=stop, state="disabled")
sendEnd.grid(column=0, row=5, pady=5)

status = StringVar()
statusLabel = ttk.Label(mainframe, textvariable=status, justify="center")
statusLabel.grid(column=0, row=6, pady=5)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
