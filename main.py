from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    password_field.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#',  '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = ''.join(password_list)

    password_field.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_field.get()
    e = email_field.get()
    password = password_field.get()

    if website == '' and len(website) == 0:
        messagebox.showwarning(title=f'{website}', message='Please enter website')
        website_field.focus()
    elif password == '' and len(password) == 0:
        messagebox.showwarning(title=f'{password}', message='Please enter password')
        password_field.focus()
    elif e == '' and len(e) == 0:
        messagebox.showwarning(title=f'{e}', message='Please enter email')
        email_field.focus()
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n' 
                                                    f'Email: {e}' 
                                                    f'\nPassword: {password}\n' 
                                                    '\nIs it ok to save?')
        if is_ok:
            with open('pass.txt', 'a') as f:
                f.write(f'{website} | {e} | {password}\n')
                website_field.delete(0, END)
                password_field.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title('Password Manager')
windows.config(padx=50, pady=50)

#Image
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3) 

#Labels
website_text = Label(text='Website:', padx=3, pady=5)
website_text.grid(row=1, column=0) #sticky=E 
email = Label(text='Email/Username:') #padx=3, pady=5
email.grid(row=2, column=0) #sticky=E
password = Label(text='Password:') #padx=3, pady=5
password.grid(row=3, column=0) #sticky=E
test_label = Label()
test_label.grid(row=6, column=0)

#Fields
website_field = Entry(width=39)
website_field.grid(row=1, column=1, columnspan=2, sticky=W)
website_field.focus()
email_field = Entry(width=39)
email_field.grid(row=2, column=1, columnspan=2, sticky=W)
email_field.insert(0, 'r.serogka@gmail.com')
password_field = Entry(width=20, show='*')
password_field.grid(row=3, column=1, sticky=W) #sticky=W

#Buttons
password_generate = Button(text='Generate Password', command=generate)
password_generate.grid(row=3, column=1, sticky=E)
add = Button(text='Add', width=33, command=save)
add.grid(row=4, column=1, columnspan=1)

windows.mainloop()