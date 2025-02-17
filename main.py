from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

crnt_card={}
try:
    data=pandas.read_csv("data/remaining_words.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def know():
    to_learn.remove(crnt_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/remaining_words.csv")
    next_card()

def next_card():
    global crnt_card,filp_timer
    window.after_cancel(filp_timer)
    crnt_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=crnt_card["French"],fill="black")
    canvas.itemconfig(card_bg,image=imj)
    flip_timer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=crnt_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=card_bimg)

window=Tk()
window.title("Flash Card")
window.config(padx=70,pady=70,bg=BACKGROUND_COLOR)
filp_timer=window.after(3000,func=flip_card)


canvas=Canvas(height=600,width=800)
card_bimg=PhotoImage(file="images/card_back.png")
wrong_img=PhotoImage(file="images/wrong.png")
right_img=PhotoImage(file="images/right.png")
imj=PhotoImage(file="images/card_front.png")
card_bg=canvas.create_image(400,264,image=imj)
card_title=canvas.create_text(400,100,text="",font=("Ariel",20,"italic"))
card_word=canvas.create_text(400,230,text="",font=("Ariel",20,"bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2)

unknown_button=Button(image=wrong_img,command=next_card)
unknown_button.grid(row=1,column=0)

know_button=Button(image=right_img,command=know)
know_button.grid(row=1,column=1)

next_card()

window.mainloop()
