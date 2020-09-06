import  requests
import json
from tkinter.messagebox import showerror,showinfo
from tkinter import *

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulk"

    prams = {
        "authorization" : "Your_API_key",
        "sender_id" : "sender_id",
        "route" : "p",
        "language" : "unicode",
        "numbers" : number,
        "message" : message
    }
    response = requests.get(url, params= prams)
    dic = response.json()
    print(dic)
    return dic.get('return')

def btn_clk():
    num = textNumber.get()
    msg = textMessage.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("msg info", "sent succesfully")
    else:
        showerror("msg info", "not sent")

shreya = Tk()
shreya.title("message sender")
shreya.geometry("450x550")

photo  = PhotoImage(file = "msgbot.png")

Label(shreya, image = photo).grid(row = 0, column = 1)
Label(shreya, text ="NUMBER", relief = RIDGE, width = 10).grid(row = 1, column = 0)
textNumber = Entry(shreya, relief = SUNKEN, font = ("Algerian", 20, "bold"), bg ="white", fg ="black", width = 20)
textNumber.insert(0, "number")
textNumber.configure(state = "normal")
textNumber.grid(row = 1, column = 1)

Label(shreya, text ="MESSAGE", relief = RIDGE, width = 10).grid(row = 3, column = 0)
textMessage = Text(shreya, relief = SUNKEN, font = ("Helvetica", 20, "bold"), height = 10, bg ="grey", fg ="white", width = 20)
textMessage.grid(row = 3, column =1)

sendbtm = Button(shreya, text ="SEND",relief = RIDGE, bg="green", fg ="white", command = btn_clk).grid(row = 4, column =2)
qtbtn = Button(shreya, text ="QUIT", bg ="red", fg ="white", command = quit).grid(row = 4, column = 0)

shreya.mainloop()
