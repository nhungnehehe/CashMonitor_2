from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("CASH MONITOR")
root.iconbitmap(r"logo.ico")
root.geometry("1000x650")
root.attributes('-topmost', True)
def show_frame(frame):
    frame.tkraise()

page0 = Frame(root)
page1 = Frame(root)
page2 = Frame(root)
for i in (page0, page1, page2):
    i.grid(row=0, column=0, sticky='nsew')
show_frame(page0)
lg_bg0_img=PhotoImage(file="bg_login.png")
lg_bg0= Label(page0, image=lg_bg0_img)
lg_bg0.pack(fill='both', expand=True)

show_frame(page0)
#-------Background thứ nhất ---------
lg_bg_img= ImageTk.PhotoImage(file="login_bg2.png")
lg_bg=Label(page0, image=lg_bg_img)
lg_bg.place(x=180, y=75)

#-----Text-----------
text1=Label(lg_bg, text="Welcome Back!", bg="black", fg="#FFFFFF", font=("Times", 15))
text1.place(x=250, y = 20)
text2=Label(lg_bg, text="We're excited to see you again!", bg="black", fg= '#FFFFFF', font=("Times", 15))
text2.place(x=200, y=50)
text3= Label(lg_bg, text="EMAIL OR PHONE NUMBER", bg= "black", fg="#FFFFFF", font=("Times", 12))
text3.place(x=30, y=100)




# --------Entry----------
email_lg_img = PhotoImage(file="email.png")
email_lg= Label(lg_bg, image=email_lg_img, bg="black")
email_lg.place(x=25, y=140)
email_lg_entry=Entry(lg_bg, bd=0, highlightthickness=0,bg="#3D404B",fg="#FFFFFF", width= 30,font=("Times", 13))
email_lg_entry.place(x=35, y=150)
root.mainloop()