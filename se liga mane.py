
import tkinter
from tkinter import messagebox

count = 0

msg_box = messagebox.showwarning("TOMO PAPUDO!", "VOCÊ FOI HACKEADO")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("PERA AI!", "PARA SER DESHACKEADO PRECISO QUE ME RESPONDA UMA PERGUNTA...")

if msg_box == 'ok':
    msg_box = messagebox.askquestion("O QUE ACHA?", "vamo se ver hoje?")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("O QUE ACHA?", "não vai querer me ve hoje?")
    if (count == 5):
        msg_box = messagebox.showerror("TO INDO AI!", "SE VAI APANHAR OTARIO!")
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("BOA!", "ah sim, acho bom")
