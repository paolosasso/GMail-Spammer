# Python email spammer
# Libraries
import base64
import smtplib
import tkinter as tk
from threading import Thread
from tkinter import ttk


def spam2():
    global persona_spam
    global numerovero
    global progress_bar
    toaddress = persona_spam.get("1.0", "end-1c")
    print(toaddress)
    # Email vars
    passwords = base64.b64decode("Your email Password In Base64").decode("utf-8")
    cpstest = ["reciever", "sender's email", passwords]

    # Specificare i dati
    print("Don't use this for doing naughty things")


# Setting vars
    username = (cpstest[1])
    password = (cpstest[2])
    number = int(numerovero.get("1.0", "end-1c"))//2
    fromaddress = username

    # Message
    message = contenuto.get("1.0", "end-1c")

    # We connect to gmail
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)

    # We create a loop
    for i in range(0, number):
        server.sendmail(fromaddress, toaddress, message)
        print(i + 1, message)
        progress_bar['value'] += 10

    print("---------------------")
    print("mail inviate con successo.")
    # We quit the connection at gmail
    server.quit()


def spam():
    global persona_spam
    global numerovero
    global progress_bar
    toaddress = persona_spam.get("1.0", "end-1c")
    print(toaddress)
    # Variabili Email
    passwords = base64.b64decode("Your email Password In Base64").decode("utf-8")
    cpstest = ["reciever", "sender's email", passwords]

    print("Don't use this for doing naughty things")

    # Setting vars
    username = (cpstest[1])
    password = (cpstest[2])
    number = int(numerovero.get("1.0", "end-1c"))//2
    fromaddress = username

    # message
    message = contenuto.get("1.0", "end-1c")

    # we connect to gmail
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)

    # we create a loop
    for i in range(0, number):
        server.sendmail(fromaddress, toaddress, message)
        print(i + 1, message)
        progress_bar['value'] += 10

    print("---------------------")
    print("mail inviate con successo.")
    # quitting connection of gmail
    server.quit()


def spaminsieme():
    Thread(target=spam).start()
    Thread(target=spam2).start()

# GUI


window = tk.Tk()
window.title('GMail Spammer')
window.geometry('300x200')

persona_spammata = tk.Label(window, text='Reciever address:')
persona_spammata.pack(anchor=tk.N)

persona_spam = tk.Text(window, height=1)
persona_spam.pack(anchor=tk.N)


numero = tk.Label(window, text='Email number:')
numero.pack(anchor=tk.N)

numerovero = tk.Text(window, height=1)
numerovero.pack(anchor=tk.N)


contenutoask = tk.Label(window, text='Mail content:')
contenutoask.pack(anchor=tk.N)

contenuto = tk.Text(window, height=3)
contenuto.pack(anchor=tk.N)


btn_spam = tk.Button(window, text='Spam', width=50, command=Thread(target=spaminsieme).start)
btn_spam.pack(anchor=tk.S, expand=True)

progress_bar = ttk.Progressbar(window, orient="horizontal", mode="indeterminate", maximum=100, value=0)
progress_bar.pack(anchor=tk.SW, expand=True)

tk.mainloop()
