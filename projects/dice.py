import tkinter as tk
from Pillow import Image, ImageTk
import random


root = tk.Tk()
root.geometry('500x360')
window.title('Dice Roll')


# def roll_dice:
#     a = random.random(5,6)
#     label = tk.Label(root, text=a).pack()
    
# button = tk.button(root, text='Click', command=roll_dice)
# button.pack()


dice = ['1','2','3','4','5','6' ]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(root, image=image1)
label2 = tk.Label(root, image=image2)

label1.image = image1
label1.image = image2

label1.place(x = 5,y=55)
label2.place(x = 55, y = 555 )

root.mainloop()