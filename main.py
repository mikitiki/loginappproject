
from tkinter import *
import os



def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("dane")
    register_screen.geometry("500x500")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Proszę wpisz swoje dane", bg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Użytkownik * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Hasło * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    password_lable = Label(register_screen, text="Proszę powtórz hasło * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Zarejestruj", width=10, height=1, bg="white", command=register_user).pack()



def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x400")
    Label(login_screen, text="Wpisz dane do logowania").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Nazwa użytkownika * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Hasło * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()



def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Zalogowano pomyślnie", fg="white", font=("arial", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()
    else:
        user_not_found()
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Sukces")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Zalogowano pomyślnie").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Sukces")
    password_not_recog_screen.geometry("220x180")
    Label(password_not_recog_screen, text=" ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Zalogowanie powiodło się")
    user_not_found_screen.geometry("150x150")
    Label(user_not_found_screen, text="Użytkownik nie został znaleziony"),
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Aplikacja do Logowania")
    Label(text="Wybierz swoją formę logowania", bg="white", width="200", height="4", font=("Arial", 10)).pack()
    Label(text="").pack()
    Button(text="Zaloguj zarejestrowanego użytkownika", height="3", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Zarejestruj nowego użytkownika", height="3", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
