import tkinter as tk
from tkinter import Tk

def error():
    error_window = tk.Tk()
    error_window.title("ERROR")
    error_window.geometry("200x70")
    tryagain = tk.Button(error_window, text="Try again", command=error_window.destroy, font=("Arial",14),bg="#AF0B0B",fg="white",width=30,height=2)
    tryagain.pack(padx=10,pady=5)
    error_window.mainloop()

def login():
    global data_username_input
    global data_password_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat

    username = open("username.txt","r",encoding="utf-8")
    
    while True:

        data_username = (str(username.readline())).removesuffix("\n")
        print(data_username)

        if not data_username:
            print("Login unsuccessful")
            play_sound()
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()  

            messagebox.showerror("Login unsuccessful", "The username or password is incorrect.")

            root.mainloop()
            line()
            break

        elif data_username_input == data_username:
            username_check = True
            break

    if username_check == True:
        password = open("password.txt",encoding="utf-8")

        while True:
            data_password = str(((password.readline())).removesuffix("\n"))

            if str(data_username_input) +':'+ str(data_password_input) == data_password:
                print("Login successful")
                line()
                login_successful = True
                #play_sound()
                break

            if not data_password:
                print("Login unsuccessful") 
                line()
                play_sound()
                import tkinter as tk
                from tkinter import messagebox
                root = tk.Tk()
                root.withdraw() 

                messagebox.showerror("Login unsuccessful", "The username or password is incorrect.")

                root.mainloop()
                break

    username.close()
    if username_check == True:
        password.close()
    return login_successful



def register():

    def submit_register():

        username = username_entry.get()
        password = password_entry.get()
        
        if len(username) < 11:
            info_label.config(text="Username must have more than 10 characters.", fg="red")
            return
        
        with open("username.txt", encoding="utf-8") as f:
            for line in f:
                if username == line.strip():
                    info_label.config(text="This username already exists.", fg="red")
                    return
        
        if len(password) < 11:
            info_label.config(text="Password must have more than 10 characters.", fg="red")
            return
        
        password_confirm = confirm_password_entry.get()
        if password != password_confirm:
            info_label.config(text="Passwords don't match.", fg="red")
            return
        
        with open("password.txt", 'a+', encoding="utf-8") as f:
            f.write(f"{username}:{password}\n")
        
        with open("username.txt", 'a+', encoding="utf-8") as f:
            f.write(f"{username}\n")
        
        info_label.config(text="Register successful.", fg="green")

    register_window = Tk()
    register_window.title("Register")
    register_window.geometry("300x170")
    register_window.configure(bg="#FAC60B")
    
    username_label = Label(register_window, text="Username:", bg="#FAC60B")
    username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    
    username_entry = Entry(register_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)
    
    password_label = Label(register_window, text="Password:", bg="#FAC60B")
    password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    
    password_entry = Entry(register_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)
    
    confirm_password_label = Label(register_window, text="Confirm Password:", bg="#FAC60B")
    confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    
    confirm_password_entry = Entry(register_window, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)
    
    submit_button = Button(register_window, text="Register", bg="green", fg="white", command=submit_register)
    submit_button.grid(row=3, columnspan=2, padx=10, pady=10)
    
    info_label = Label(register_window, text="", bg="#FAC60B")
    info_label.grid(row=4, columnspan=2, padx=10, pady=5)
    
    register_window.mainloop()

import tkinter as tk
from tkinter import messagebox
def on_button_click():
    global data_username_input
    global data_password_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat
    global program_order
    response = messagebox.askquestion("เลือก", "Do you want to open camera?")
    if response == 'yes':
        program_order = True
        detecting()

def open_program():

    global data_username_input
    global data_password_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat

    if login_successful == True:
        print("You want to open 𝐏𝐫𝐨𝐠𝐫𝐚𝐦 𝐝𝐞𝐭𝐞𝐜𝐭𝐢𝐧𝐠 𝐬𝐚𝐟𝐞𝐭𝐲 𝐡𝐚𝐭 𝐛𝐲 𝐦𝐚𝐜𝐡𝐢𝐧𝐞 𝐥𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐢𝐧 𝐫𝐞𝐚𝐥 𝐭𝐢𝐦𝐞?")
        line()
        program_order_input = input("If you want, type y, but if you don't, type n. :")
        line()

        while True :

            
            if str(program_order_input) == "y":
                program_order = True
                break

            if str(program_order_input) == "n":
                program_order == False
                break
            
            else :
                print('You can only answer "y" and "n".')
                line()
                program_order_input = input("If you want, type y, but if you don't, type n. :")
                line()

        return program_order

def detecting():

    global data_username_input
    global data_password_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat
    __ = True
    from ultralyticsplus import YOLO 
    from datasets import load_dataset
    import cv2
    from gtts import gTTS as tts
    #from playsound import playsound
    import os
    line()
    #dataset = load_dataset("keremberke/hard-hat-detection","full")
    model = YOLO('keremberke/yolov8n-hard-hat-detection')
    num_hardhat = 0
    num_no_hardhat = 0
    cap = cv2.VideoCapture(0)
    
    while __ and login_successful and program_order == True:
        __ , flame = cap.read()
        model_use = model.track(flame,persist=True)
        flame_ = model_use[0].plot()
        cv2.imshow("output",flame_)

        if str(model_use[0].boxes.cls) == 'tensor([0.])':
            num_hardhat = num_hardhat+1
            if num_hardhat == 50:
                num_hardhat = 0
                sefty_hardhat = True
                Text_Sound_03 = "Hardhat"
                from gtts import gTTS as tts
                #from playsound import playsound
                import os
                Languagecode = "en"
                File_Name = "Text_Sound.mp3"
                Play = tts(Text_Sound_03 , lang_check= False , lang = Languagecode)
                Play.save(File_Name)
                #playsound(File_Name)
                os.remove(File_Name)
                line()
                response = messagebox.askquestion("เลือก", "Do you want to save the photo?")
                if response == 'yes':
                    save_order_2 = True
                if response == 'no':
                    save_order_2 = False
                line()

                while True :
                    line()
                    import datetime
                    import os
                    if os.path.exists(str(datetime.datetime.now().date())+"_"+"img_detecting_Have"):
                        True
                    else :
                        os.mkdir(str(datetime.datetime.now().date())+"_"+"img_detecting_Have")

                    if save_order_2 == True:
                        cv2.imwrite("C:\\Users\\user\\Desktop\\newcomprofinal\\"+str(datetime.datetime.now().date())+"_"+"img_detecting_Have"
                                    +"\\img"+str(data_username_input)+".png",flame)
                        break

                    if save_order_2 == False:
                        detecting()
                        break

                    else:
                        print('You can only answer "y" and "n".')
                        line()
                        save_order = input("Do you want to save the photo? If so press 'y'"+
                                           ". If not and take a new photo press 'n'. ")
                        line()
                
                break


        if str(model_use[0].boxes.cls) == 'tensor([1.])' :
            num_no_hardhat = num_no_hardhat+1
            if num_no_hardhat == 50:
                Text_Sound_04 = "NO-Hardhat"
                from gtts import gTTS as tts
                #from playsound import playsound
                import os
                Languagecode = "en"
                File_Name = "Text_Sound.mp3"
                Play = tts(Text_Sound_04 , lang_check= False , lang = Languagecode)
                Play.save(File_Name)
                #playsound(File_Name)
                os.remove(File_Name)
                num_no_hardhat = 0
                sefty_hardhat = False
                response = messagebox.askquestion("เลือก","Do you want to save the photo?")
                if response == 'yes':
                    save_order_2 = True
                if response == 'no':
                    save_order_2 = False
                line()

                while True :
                    line()
                    import datetime
                    import os
                    if os.path.exists(str(datetime.datetime.now().date())+"_"+"img_detecting_No-Have"):
                        True
                    else :
                        os.mkdir(str(datetime.datetime.now().date())+"_"+"img_detecting_No-Have")

                    if save_order_2 == True:
                        cv2.imwrite("C:\\Users\\user\\Desktop\\newcomprofinal\\"+str(datetime.datetime.now().date())+"_"+"img_detecting_No-Have"
                                        +"\\img"+str(data_username_input)+".png",flame)
                        break

                    if save_order_2 == False:
                        detecting()
                        break

                    else:
                        print('You can only answer "y" and "n".')
                        line()
                        save_order = input("Do you want to save the photo? If so press 'y'"+
                                            ". If not and take a new photo press 'n'. ")
                        line()  
                break

        if cv2.waitKey(1) & 0xFF == ord(" "):
            break

    cap.release()
    cv2.destroyAllWindows

def line():

    global data_username_input
    global data_password_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat

    print("═════════════════════════════════════════════════════════════════")

def play_sound():

    global data_username_input
    global data_password_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat

    from gtts import gTTS as tts
    #from playsound import playsound
    import os

    Languagecode = "en"
    Text_Sound_01 = "login successful"
    Text_Sound_02 = "Login unsuccessful"
    File_Name = "Text_Sound.mp3"

    if login_successful == False:
        Play = tts(Text_Sound_02 , lang_check= False , lang = Languagecode)
        Play.save(File_Name)
        #playsound(File_Name)
        os.remove(File_Name)

    if login_successful == True:
        Play = tts(Text_Sound_01 , lang_check= False , lang = Languagecode)
        Play.save(File_Name)
        #playsound(File_Name)
        os.remove(File_Name)

def check_time():

    global data_username_input
    global data_password_input
    global data_username_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat

    if login_successful == True:

        import datetime
        time_login = datetime.datetime.now().time().strftime('%H:%M:%S')
        check_time_input = open(str(datetime.datetime.now().date())+"_"+"check_time.txt",'a+',encoding="utf-8")
        check_time_input.write(str(data_username_input)+"_"+str(time_login)+"\n")
        check_time_input.close()

class status:

    global data_username_input
    global data_password_input
    global data_username_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat
    global data_username_status

    def __init__(self ,data_username_status):

        self.data_username_status = data_username_status

    def login_check (self) :

        username = open("username.txt",encoding="utf-8")
        while True:
            
            data_username = (str(username.readline())).removesuffix("\n")
            if not data_username:
                print("Username is not correct")
                line()
                break
            elif str(self.data_username_status) == data_username:
                username_status = True
                break

        if username_status == True:
            import datetime
            check_time_input_1 = open(str(datetime.datetime.now().date())+"_"+"check_time.txt",'r',encoding="utf-8")
            for username_status_time_1 in check_time_input_1:
                username_status_time_1 = (str(check_time_input_1.readline())).removesuffix("\n")
                username_status_time_check = username_status_time_1.split("_")[0]
                if not username_status_time_1:
                    data_username_status_check = "Haven't logged in yet."
                    line()
                    break
                elif str(self.data_username_status) == username_status_time_check:
                    import tkinter as tk

                    data_username_status_check = "Already logged in"

                    log = tk.Tk()
                    log.title("login")
                    lbn1 = tk.Label(log, text=data_username_status_check, fg="white", font=('Terminal', 15, 'bold'), bg="#335B8F")
                    lbn1.pack()
                    log.geometry("200x100")

                    log.mainloop()
                    break

        if username_status == True:
            return data_username_status_check
        
    def login_time_check (self) :

        username = open("username.txt",encoding="utf-8")
        while True:
            data_username = (str(username.readline())).removesuffix("\n")
            if not data_username:
                import tkinter as tk
                from tkinter import messagebox
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror("Log in unsuccessfull","Username is not correct")
                root.mainloop()
                username_status = False
                line()
                break
            elif str(self.data_username_status) == data_username:
                username_status = True
                break
        
        if username_status == True:
            import datetime
            check_time_input_1 = open(str(datetime.datetime.now().date())+"_"+"check_time.txt",'r',encoding="utf-8")
            for username_status_time_1 in check_time_input_1:
                username_status_time_1 = (str(check_time_input_1.readline())).removesuffix("\n")
                username_status_time_check = username_status_time_1.split("_")[0]
                if not username_status_time_1:
                    data_username_status_check = "Haven't logged in yet."
                    line()
                    break
                elif str(self.data_username_status) == username_status_time_check:
                    data_username_status_check = "Already logged in"
                    data_username_time_status_check_1 = True
                    import tkinter as tk

                    data_username_status_check = "Already logged in"
                    log = tk.Tk()
                    log.title("login")
                    log.configure(bg="#FAC60B")
                    lbn1 = tk.Label(log, text=data_username_status_check+"\n"+username_status_time_1.split("_")[1], fg="black", font=('Terminal', 15, 'bold'), bg="#FAC60B")
                    lbn1.pack()
                    log.geometry("200x50")

                    log.mainloop()

                    break
            
        check_time_input_1.close()
    
    def headhat_check(self):
        username = open("username.txt","r",encoding="utf-8")
        while True:
            data_username = (str(username.readline())).removesuffix("\n")
            if not data_username:
                print("Username is not correct")
                line()
                break

            elif str(self.data_username_status) == data_username:
                username_status = True
                break
        
        while username_status == True:
            import datetime
            check_time_input = open(str(datetime.datetime.now().date())+"_"+"check_time.txt",'r',encoding="utf-8")
            username_status_time = (str(check_time_input.readline())).removesuffix("\n")
            username_status_time_check = username_status_time.split("_")[0]

            if not check_time_input:
                data_username_status_check = "Haven't logged in yet."
                line()
                break

            elif str(self.data_username_status) == username_status_time_check:
                data_username_status_check = "Already logged in"
                import os
                folder_1= str(datetime.datetime.now().date())+"_"+"img_detecting_Have"
                folder_2= str(datetime.datetime.now().date())+"_"+"img_detecting_No-Have"
                file_list_1= os.listdir(folder_1)
                file_list_2= os.listdir(folder_2)

                for file_name_1 in file_list_1:
                    username_img = file_name_1.split(".")[0]
                    if "img"+str(self.data_username_status) == username_img:
                        sefty_check = True
                        return sefty_check
                    break

                for file_name_2 in file_list_2:
                    username_img = file_name_2.split(".")[0]
                    if "img"+str(self.data_username_status) == username_img:
                        sefty_check = False
                        return sefty_check              
                    break
    
def close_window():
    global rootclose
    rootclose = True
    root.destroy()
    def on_login():

        global data_username_input
        global data_password_input
        global num_camera
        global num_hardhat
        global num_no_hardhat
        global data_password_input
        global data_username_input
        global login_successful
        global program_order
        global __
        global sefty_hardhat
        global entry_username
        global entry_password
        data_username_input = 0
        data_password_input = 1
        data_username_input = entry_username.get()
        data_password_input = entry_password.get()
        root.destroy()

login_successful = False
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Honor Program")

img = Image.open("image0.jpg")
img = img.resize((int(img.width*.4),int(img.height*.4)))
photo = ImageTk.PhotoImage(img)
lbl2 = Label(image=photo)
lbl2.place(x=0,y=0)

myLabel1 = Label(root,text="Program Detecting Safety Hat",fg="white",font=('Terminal', 15, 'bold'),bg="#EAA515").place(x=165,y=12)
myLabel2 = Label(root,text="By Machine Learning in Real Time",fg="white",font=('Terminal', 15, 'bold'),bg="#EAA515").place(x=140,y=40)
myLabel3 = Label(root,text="This program use for detecting",font=('Browallia New', 20),bg="#EDDBB5").place(x=20,y=100)
myLabel4 = Label(root,text="the safety hat in construction site",font=('Browallia New', 20),bg="#EDDBB5").place(x=20,y=130)
myLabel5 = Label(root,text="in real time.",font=('Browallia New', 20),bg="#EDDBB5").place(x=20,y=160)
myLabel6 = Label(root,text="Created by PHD",font=('Browallia New', 20),fg="black",bg="#EDDBB5").place(x=20,y=350)

btn1 = Button(root,text="START PROGRAM",fg="#AF0B0B",bg="#FFDE59",font=('Tahoma', 15, 'bold'),padx="30",pady=15,command = close_window).place(x=20,y=230)

root.geometry("600x400")
root.resizable(0,0)
root.mainloop()


def on_login():

    global data_username_input
    global data_password_input
    global num_camera
    global num_hardhat
    global num_no_hardhat
    global data_password_input
    global data_username_input
    global login_successful
    global program_order
    global __
    global sefty_hardhat\
    
    data_username_input = entry_username.get()
    data_password_input = entry_password.get()
    root.destroy()

root = tk.Tk()
root.title("Login")

img2 = Image.open("image2.JPG")
img2 = img2.resize((int(img2.width*.4),int(img2.height*.4)))
photo1 = ImageTk.PhotoImage(img2)
lbl2 = Label(image=photo1)
lbl2.place(x=0,y=0)

root.geometry("400x300")

frame = ttk.Frame(root, padding="20", borderwidth=2, relief="groove", style="My.TFrame")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

style = ttk.Style()
style.configure("My.TFrame", background="#FAC60B")

label_username = ttk.Label(frame, text="Username:")
label_username.grid(row=0, column=0, pady=(10, 5), sticky=tk.W)
label_username.configure(background="#FAC60B")

entry_username = ttk.Entry(frame, width=30)
entry_username.grid(row=0, column=1, pady=(10, 5))

label_password = ttk.Label(frame, text="Password:")
label_password.grid(row=1, column=0, pady=(10, 5), sticky=tk.W)
label_password.configure(background="#FAC60B")

entry_password = ttk.Entry(frame, show="*", width=30)
entry_password.grid(row=1, column=1, pady=(10, 5))

button_login = tk.Button(frame, text="Login", command=on_login, bg="green", fg="white")
button_login.grid(row=2, columnspan=2, pady=(20, 10))

root.mainloop()

login()
check_time()
want_login_time_check_= False
want_login_check_ = False

def want_login_check():
    global want_login_check_
    want_login_check_ = True
    root.destroy()

def want_login_time_check():
    global want_login_time_check_
    want_login_time_check_= True
    root.destroy()

if login_successful == True:
    root = tk.Tk()
    root.title("My Enhanced Application")
    root.geometry("390x165")

    img2 = Image.open("image2.JPG")
    img2 = img2.resize((int(img2.width*.4),int(img2.height*.4)))
    photo1 = ImageTk.PhotoImage(img2)
    lbl2 = Label(image=photo1)
    lbl2.place(x=0,y=0)

    root.configure(bg="darkorange")  

    button1 = tk.Button(root, text="register", command=register, font=("Arial", 14), bg="#FAC60B", width=15, height=2)
    button1.grid(row=0, column=0, padx=10, pady=10)

    button2 = tk.Button(root, text="open_program", command=on_button_click, font=("Arial", 14), bg="#FAC60B" ,width=15, height=2)
    button2.grid(row=0, column=1, padx=10, pady=10)

    button3 = tk.Button(root, text="login_check", command = want_login_check , font=("Arial", 14), bg="#FAC60B" ,width=15, height=2)
    button3.grid(row=1, column=0, padx=10, pady=10)

    button4 = tk.Button(root, text="LOG OUT", command= want_login_time_check , font=("Arial", 14), bg="#AF0B0B" ,width=15, height=2)
    button4.grid(row=1, column=1, padx=10, pady=10)

    root.mainloop()
import tkinter as tk

def status_time():
    global input_value
    global want_login_check_
    global want_login_time_check_
    
    if want_login_check_ == True:
        P = status(str(input_value))
        P.login_time_check()
    if want_login_time_check_ == True:
        P = status(str(input_value))
        print(P.login_time_check())


def status_id_input():
    global input_value
    input_value = entry.get()
    root.destroy()  

if want_login_check_ == True:
    input_value = 1
    root = tk.Tk()
    label = tk.Label(root, text="",bg="#FAC60B")
    label.pack()
    label2 = tk.Label(root, text="What's user that you want to check?",bg="#FAC60B")
    label2.pack()
    label3 = tk.Label(root, text=" ",bg="#FAC60B")
    label3.pack()
    entry = tk.Entry(root)
    entry.pack()
    label4 = tk.Label(root, text=" ",bg="#FAC60B")
    label4.pack()
    root.configure(bg="#FAC60B")  
    button = tk.Button(root, text="ENTER", command=status_id_input,bg="green",fg="white")
    button.pack()
    root.geometry("250x150")

    root.mainloop()

    status_time()

