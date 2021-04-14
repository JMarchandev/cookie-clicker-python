from tkinter import *
from model.counter import Counter


# Tkinter
width = 500
height = 500
window = Tk()
window.title("Cookie Clicker")
window.minsize(width, height)
window.config(background="white", padx=20, pady=20)


# Variables
counter = Counter(0)

counter_text = StringVar()
counter_text.set("coins: " + str(counter.get_value()))

bonus_price_text = StringVar()
bonus_price_text.set(counter.get_bonus_price())

error_text = StringVar()
error_text.set("")


# defs
def on_click_increment_counter():
    counter.increment()
    counter_text.set("coins: " + str(counter.get_value()))


def on_click_set_new_bonus():
    counter_value = counter.get_value()
    bonus_price = counter.get_bonus_price()

    if counter_value >= bonus_price:
        error_text.set("")

        new_bonus = counter.get_bonus() * 2
        counter.set_bonus(new_bonus)

        counter_text.set("coins: " + str(counter.get_value()))

        bonus_price_text.set(counter.get_bonus_price())
    else:
        error_text.set("You need to click yet !!")


# Frames
# Main frame
main_frame = Frame(window, width=width, height=height, bg="white")

# Menu frame
menu_frame = Frame(main_frame, width=width, height=height * 0.10)
menu_frame.pack()

# Buttons
button = Button(menu_frame, text="Buy bonus: x2", font=("Helvetica", 10), bg="white", fg="black",
                command=on_click_set_new_bonus)
button.pack()

# Price label
price_label = Label(menu_frame, textvariable=bonus_price_text, font=("Helvetica", 10), bg="white", fg="black")
price_label.pack()

# Game frame
game_frame = Frame(main_frame, width=width, height=height * 0.90, bg="white")
game_frame.pack()

# Cookie button
cookie_button = Button(game_frame, text="click me", font=("Helvetica", 20), bg="white", fg="black",
                       command=on_click_increment_counter)
cookie_button.pack(expand=YES)

# Dynamic title counter
counter_title = Label(game_frame, textvariable=counter_text, font=("Helvetica", 20), bg="white", fg="black")
counter_title.pack()

# Error label
error_label = Label(game_frame, textvariable=error_text, font=("Helvetica", 20), bg="white", fg="red")
error_label.pack()

# Pack main frame
main_frame.pack()

# Launch
window.mainloop()
