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
lg_bg=Label(page0, image=lg_bg_img, bd=0)
lg_bg.place(x=180, y=75)

#-----Text-----------
text1=Label(lg_bg, text="Welcome Back!", bg="#AEE2FF", fg="black", font=("Times", 15))
text1.place(x=250, y = 20)
text2=Label(lg_bg, text="We're excited to see you again!", bg="#AEE2FF", fg= 'black', font=("Times", 15))
text2.place(x=200, y=50)
text3= Label(lg_bg, text="EMAIL OR PHONE NUMBER", bg= "#AEE2FF", fg="black", font=("Times", 12))
text3.place(x=30, y=100)
text4 = Label(lg_bg, text="PASSWORD", bg="#AEE2FF", fg="black", font=("Times", 12))
text4.place(x=30, y=210)
text5= Label(lg_bg, text="Forgot you password?", bg="#AEE2FF", fg= "brown", font=("Times", 12))
text5.place(x=30, y = 310)
text6= Label(lg_bg, text="Need an account?", bg="#AEE2FF", fg="black", font=("Times",13))
text6.place(x=30, y=400)

# --------Entry TĐN----------
email_lg_img = PhotoImage(file="email.png")
email_lg= Label(lg_bg, image=email_lg_img, bg="#AEE2FF")
email_lg.place(x=25, y=140)
email_lg_entry=Entry(lg_bg, bd=0, highlightthickness=0,bg="#E9F8F9",fg="black", width= 30,font=("Times", 13))
email_lg_entry.place(x=35, y=155)

#----------Entry MK----------
pass_lg_img= PhotoImage(file="email.png")
pass_lg=Label(lg_bg, image=pass_lg_img, bg="#AEE2FF")
pass_lg.place(x=25,y=250)
pass_lg_entry=Entry(lg_bg, bd=0, highlightthickness=0, bg="#E9F8F9", fg="black", width=30, font=("Times", 13), show="*")
pass_lg_entry.place(x=35, y=269)


# ---------Button Login----------
lg_bt_img=PhotoImage(file="button_login.png")
lg_bt = Button(lg_bg, bd=0,activebackground="#AEE2FF",bg="#AEE2FF",fg="black",  image=lg_bt_img)
lg_bt.place(x=200, y=340)


# ---------Button Register---------
rg_bt=Button(lg_bg, bd=0, text="Register", activebackground="#AEE2FF", bg="#AEE2FF", fg="brown", font=("Times", 13))
rg_bt.place(x=155, y=398)
root.mainloop()



