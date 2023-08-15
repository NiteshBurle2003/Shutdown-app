from tkinter import *
import os

def Restart():
	os.system("shutdown /r /t 1")

def Restart_Time():
	os.system("shutdown /r /t 20")
	
def Log_Out():
	os.system("shutdown -1")

def Shutdown():
	os.system("shutdown /r /t 1")
	
def Exit():
   exit()


st=Tk()   
st.title("ShutDown App")
st.geometry("600x600")
st.config(bg="grey")
screen_width=st.winfo_screenwidth()
screen_height=st.winfo_screenheight()
x=(screen_width-600)//2
y=(screen_height-600)//2
st.geometry(f"600x600+{x}+{y}")

button1=Button(st,text="Restart",bg="orange", width=20, height=1, font=("Arial",20,"bold"),
	highlightthickness=2,highlightcolor="black",cursor="plus",command=Restart)
button1.place(x=200,y=50,height=50,width=200)


button2=Button(st,text="Restart Time",bg="orange", width=20, height=1,font=("Arial",20,"bold"),
	highlightthickness=2,highlightcolor="black",cursor="plus",command=Restart_Time)
button2.place(x=200,y=150,height=50,width=200)


button3=Button(st,text="Log-Out",bg="orange", width=20, height=1,font=("Arial",20,"bold"),
	highlightthickness=2,highlightcolor="black",cursor="plus",command=Log_Out)
button3.place(x=200,y=250,height=50,width=200)


button4=Button(st,text="Shutdown",bg="orange", width=20, height=1,font=("Arial",20,"bold"),
	highlightthickness=2,highlightcolor="black",cursor="plus",command=Shutdown)
button4.place(x=200,y=350,height=50,width=200)

button5=Button(st,text="Exit",bg="orange", width=20, height=1,font=("Arial",20,"bold"),
	highlightthickness=2,highlightcolor="black",cursor="plus",command=Exit)
button5.place(x=200,y=450,height=50,width=200)

st.mainloop()