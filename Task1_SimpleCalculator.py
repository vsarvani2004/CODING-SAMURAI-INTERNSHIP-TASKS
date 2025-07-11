import tkinter as tk
def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text == "=":
        try:
            result=eval(scvalue.get())
            scvalue.set(result)
        except Exception as e:
            scvalue.set("Error")
    elif text=="C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get()+text)
    screen.update()

root=tk.Tk() 
root.geometry("400x550")
root.title("Simple Calculator")

scvalue=tk.StringVar()
scvalue.set("")
screen=tk.Entry(root, textvar=scvalue, font="Arial 20", bd=8, relief=tk.RIDGE, justify="right")
screen.pack(fill=tk.BOTH,ipadx=8, pady=10, padx=10)

buttons=[
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    f=tk.Frame(root)
    f.pack()
    for btn_text in row:
        b=tk.Button(f, text=btn_text, padx=20, pady=20, font="Arial 18", bd=5)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>",click)
root.mainloop()      