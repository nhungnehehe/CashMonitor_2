from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("CASH MONITOR")
root.iconbitmap(r"logo.ico")
root.geometry("1000x650+300+300")
root.attributes('-topmost', True)

bg = ImageTk.PhotoImage(file="bgt1.png")
my_cv= Canvas(root, width=1000, height=650)
my_cv.pack(fill='both', expand=True)
my_cv.create_image(0,0, image=bg, anchor="nw")
def resizer(e):
    global bg1, resized_bg, new_bg
    bg1=Image.open(r"bgt1.png")
    resized_bg=bg1.resize((e.width, e.height), Image.LANCZOS)
    new_bg = ImageTk.PhotoImage(resized_bg)
    my_cv.create_image(0,0,image=new_bg, anchor='nw')

root.bind('<Configure>', resizer)
root.mainloop()
