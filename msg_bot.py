import requests
import json
from tkinter import *
from tkinter.messagebox import showerror, showinfo
def send_sms(number, message):

    #header
    url =  "https://www.fast2sms.com/dev/bulk"
    #body

    params = {
        "authorization": "your_API_key",
        "language": "unicode",
        "sender_id": "FSTSMS",
        "message":message,
        "route": "p",
        "numbers": number
    }
    response = requests.get(url, params= params)
    dic = response.json()
    print(dic)
    return dic.get('return')

def btn_clk():
    num = textNumber.get()
    msg = textMessage.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Message information", "Message sent")
    else:
        showerror("Message information", "Message not sent")


#making gui for the message sending app
root = Tk()
root.title("message sender")
root.geometry("400x500")

#making entry for the mobile number input
Label(root, text = "Number", relief = RIDGE, width = 20).grid(row =0, column = 0)
textNumber = Entry(root, font = ("Algrian", 20, "bold"),relief =SUNKEN ,fg ="black", width = 20, bg ="light yellow")
textNumber.grid(row = 0, column = 1)

#making Text entry for the message to be sent
Label(root, text = "Message", relief = RIDGE,width = 12, height = 5).grid(row = 2, column = 0)
textMessage = Text(root, font = ("Helvetica", 20, "bold"), height = 18, width = 20, relief = SUNKEN, fg = "white", bg = "dark blue")
textMessage.grid(row =2, column= 1)

#making the buttons
sendBtn = Button(root, text = "SEND", fg = "white", bg = "green", command = btn_clk).grid(row = 3, column = 2)
quitBtn = Button(root, text = "QUIT", fg = "white", bg = "red", command = quit ).grid(row = 3, column = 0)

root.mainloop()

