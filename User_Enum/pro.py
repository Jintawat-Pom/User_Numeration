from tkinter import *
import json
import os


def windows_alert(txt_data):
    app1 = Tk()
    # dir_path = os.path.dirname(os.path.abspath(__file__))
    app1.geometry("300x100")
    # p1 = PhotoImage(file='User_Enum/icons/false.png')
    # app1.iconphoto(False, p1)
    if txt_data == "Login success":
        app1.title("Success")
    else:
        app1.title("Error")
    txt = Label(app1, text=txt_data)
    txt.place(x=20, y=30)
    app1.minsize("300", "100")
    app1.maxsize("300", "100")
    app1.mainloop()


def check_login_noob():
    inp = inputusertxt.get(1.0, "end-1c")
    inp1 = inputpasstxt.get(1.0, "end-1c")
    c = 0
    out = ["There is no user account in the system.",
           "Password is wrong", "Login success"]
    Dir_P = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(Dir_P, "data.json"), encoding='utf-8') as data:
        dic = data.read()
    data_dic = json.loads(dic)
    data.close()
    for i in data_dic:
        # print(i)
        # print(data_dic[i]["Username"])
        # print(data_dic[i]["Password"])
        if inp == data_dic[i]["Username"] and inp1 != data_dic[i]["Password"]:
            c = 1
            break
        elif inp == data_dic[i]["Username"] and inp1 == data_dic[i]["Password"]:
            c = 2
            break
        else:
            pass
    windows_alert(out[c])
    # print(out[c])


def check_login_pro():
    inp = inputusertxt.get(1.0, "end-1c")
    inp1 = inputpasstxt.get(1.0, "end-1c")
    c = 0
    out = ["Username or Password is wrong.", "Login success"]
    Dir_P = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(Dir_P, "data.json"), encoding='utf-8') as data:
        dic = data.read()
    data_dic = json.loads(dic)
    data.close()
    for i in data_dic:
        if inp == data_dic[i]["Username"] and inp1 == data_dic[i]["Password"]:
            c = 1
            break
        else:
            pass
    windows_alert(out[c])
    # print(out[c])


# check_login_noob("pom000", "king010203")
# check_login_pro("pom000", "king010203")
# print(data_dic)


app = Tk()
app.title('User Enumeration')
app.geometry("300x150")
p1 = PhotoImage(file='User_Enum/icons/cyber-security.png')
app.iconphoto(False, p1)
app.config(bg="black")
l = Label(app, text="Username")
l1 = Label(app, text="Password")
inputusertxt = Text(app, height=1, width=23)
inputpasstxt = Text(app, height=1, width=23)
button = Button(app, text='Login Noob', command=check_login_noob)
button1 = Button(app, text='Login Pro', command=check_login_pro)
l.place(x=20, y=20)
l1.place(x=20, y=50)
inputusertxt.place(x=90, y=20)
inputpasstxt.place(x=90, y=50)
button.place(x=60, y=100)
button1.place(x=170, y=100)

app.minsize("300", "150")
app.maxsize("300", "150")
app.mainloop()
