from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("CASH MONITOR")
root.iconbitmap(r"logo.ico")
root.geometry("1000x650+300+300")
root.attributes('-topmost', True)
# root.state('zoomed')   - full màn hình
page0= Frame(root)
page1 = Frame(root)
page2= Frame(root)
page3= Frame(root)
page4 = Frame(root)
page5 = Frame(root)
for i in (page1, page2, page3, page4):
    i.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()
# Trang 1
show_frame(page1)
bg = ImageTk.PhotoImage(file="bg1.png")
my_cv= Canvas(page1, width=1000, height=650)
my_cv.pack(fill='both', expand=True)
my_cv.create_image(0,0, image=bg, anchor="nw")

def click(event):
    entry1.config(state =NORMAL)
    entry1.delete(0, END)
entry1=Entry(page1, width = 25, font=('Times', 15))
entry1.place(x=53, y= 330)
entry1.insert(0, "User name")
entry1.config(state = DISABLED)
entry1.bind("<Button-1>", click)

login_img= ImageTk.PhotoImage(Image.open("button1.1.png").resize((277,70), Image.LANCZOS))
bt1 = Button(page1, image= login_img, bg="#CFEBF9", activebackground="#CFEBF9", borderwidth=0, command=lambda: show_frame(page2))
bt1.place(x=60, y=370)


 # Trang 2
bg2 = ImageTk. PhotoImage(file="bg2.png")
my_cv1= Canvas(page2, width=1000, height=650)
my_cv1.pack(fill='both', expand=True)
my_cv1.create_image(0,0, image=bg2, anchor="nw")
bt2_1_img=ImageTk.PhotoImage(Image.open("bt2.2.png").resize((180,137),Image.LANCZOS))
bt2_1= Button(page2, image= bt2_1_img, borderwidth=0, command= lambda: show_frame(page3))
bt2_1.place(x=60, y=300)
bt2_2_img= ImageTk.PhotoImage(Image.open("bt2.1.png").resize((180,137), Image.LANCZOS))
bt2_2=Button(page2, image=bt2_2_img, borderwidth=0, command=lambda: show_frame(page4))
bt2_2.place(x=400, y=300)
bt2_3_img = ImageTk.PhotoImage(Image.open("bt2.3.png").resize((180,137),Image.LANCZOS))
bt2_3 = Button(page2, image=bt2_3_img, borderwidth=0, command=lambda: show_frame(page5))
bt2_3.place(x=740, y=300)

# Trang 3:
bg3=ImageTk.PhotoImage(Image.open("bg3.png").resize((1000,650), Image.LANCZOS))
my_cv2= Canvas(page3, width=1000, height=650)
my_cv2.pack(fill="both", expand=True)
my_cv2.create_image(0,0, image = bg3, anchor='nw')
bt3_1_img= ImageTk.PhotoImage(Image.open("bt3.1.png").resize((150,126), Image.LANCZOS))
bt3_1= Button(page3, image=bt3_1_img, bd=0,  bg="#CFEBF9")
bt3_1.place(x=60, y = 200)

# Trang4

root.mainloop()

