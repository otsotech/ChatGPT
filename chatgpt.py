import threading
import queue
import requests
import json
from tkinter import *

global request_in_progress
request_in_progress = False

# create a queue to store the result of the HTTP request
result_queue = queue.Queue()

def get_response(text, lang, queue):
    params = {'text': text, 'lang': lang}
    try:
        response = requests.get('https://api.pawan.krd/chat/gpt', params=params)
    except requests.exceptions.ConnectionError:
        print("Unable to connect to server")
    # store the result in the queue
    queue.put(response.json()['reply'])


def check_request_complete():
    global request_in_progress
    # check if a request is being made
    if request_in_progress:
        if thread is not None and not thread.is_alive():
            # get the result from the queue
            result = result_queue.get()
            # insert the result into the text widget
            txt.insert(END, "\n\n" + "ChatGPT:\n" + result)
            # set the flag to False to indicate that the request is complete
            request_in_progress = False

    # schedule this function to run again in 500 milliseconds
    root.after(500, check_request_complete)


def send():
    send = "You:\n" + e.get()
    txt.insert(END, "\n" + send)
    user = e.get().lower()
    e.delete(0, END)

    # set the flag to True to indicate that a request is being made
    global request_in_progress
    request_in_progress = True

    # create a new thread to perform the request
    global thread
    thread = threading.Thread(
        target=get_response, args=(user, 'en', result_queue)
    )

    # start the thread
    thread.start()

# GUI
root = Tk()
root.title("ChatGPT")
root.geometry("960x540")
root['background']='#282b30'

BG_COLOR = "#282b30"
TEXT_COLOR = "#fff"

FONT = "Arial"

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
txt.grid(row=1, column=0)

e = Entry(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
e.grid(row=2, column=0)

send = Button(
    root, text="Send", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, command=send
).grid(row=2, column=1)

# define the thread variable
global thread
thread = None

# start the check for request completion
check_request_complete()

root.mainloop()