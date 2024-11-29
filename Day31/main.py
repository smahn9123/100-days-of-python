from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
word_dict_list = data.to_dict(orient="records")

timer = None

def next_card():
    global timer
    if timer:
        window.after_cancel(timer)

    card_chosen = random.choice(word_dict_list)
    french = card_chosen["French"]
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=french)

    english = card_chosen["English"]
    timer = window.after(3000, flip_card, english)

def flip_card(english):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=english)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
