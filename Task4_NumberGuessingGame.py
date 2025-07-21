from tkinter import *
import random

# Create the main window
ws = Tk()
ws.title('Number Guessing Game')
ws.geometry('600x400')
ws.config(bg='#5671A6')

# Initialize game values
ranNum = random.randint(0, 10)
chance = 3
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance

    usr_ip = var.get()

    if chance > 0:
        if usr_ip == ranNum:
            msg = f'🎉 You won! {ranNum} is the correct number.'
            disp.set(msg)
            entry_box.config(state='disabled')         # Disable input
            submit_btn.config(state='disabled')        # Disable button
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'🔻 {usr_ip} is too high. {chance} chances left.'
            disp.set(msg)
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'🔺 {usr_ip} is too low. {chance} chances left.'
            disp.set(msg)

        if chance == 0 and usr_ip != ranNum:
            msg = f'❌ You lost! The number was {ranNum}.'
            disp.set(msg)
            entry_box.config(state='disabled')         # Disable input
            submit_btn.config(state='disabled')        # Disable button
    else:
        disp.set(f'❌ Game over! The number was {ranNum}.')

# Display message
Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    fg='white',
    font=('sans-serif', 14)
).pack(pady=(20, 0))

# Input field (stored as reference for disabling)
entry_box = Entry(
    ws,
    textvariable=var,
    font=('sans-serif', 18),
    justify='center'
)
entry_box.pack(pady=(50, 10))

# Submit button (stored as reference for disabling)
submit_btn = Button(
    ws,
    text='Submit Guess',
    font=('sans-serif', 16),
    bg='#F0A500',
    fg='white',
    command=check_guess
)
submit_btn.pack()

# Run the GUI loop
ws.mainloop()