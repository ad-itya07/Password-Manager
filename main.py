from tkinter import * # Using asterisk will only import all the classes
from tkinter import messagebox # messagebox is just another module hence it wasn't imported with *
from random import choice,randint,shuffle
import pyperclip

DEFAULT_EMAIL = "user@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbol_list = [choice(symbols) for char in range(randint(2, 4))]
    num_list = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letter_list + symbol_list + num_list
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0,string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure no fields are empty.")

    else:
        # MESSAGEBOX returns a boolean value True/False when "ask" methods are used
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered:\n Email: {email}\n"
                                                     f"Password: {password}\n\nIs it ok to save?")

        if is_ok:
            with open(file="data.txt", mode="a") as data:
                data.write(f"{website} - {email} - {password}\n")

            website_entry.delete(0,END)
            password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=80)

canvas = Canvas(width=200,height=200)

lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

# LABEL
website_label = Label(text="Website",pady=5,padx=10)
website_label.grid(row=1,column=0,sticky="w")

email_label = Label(text="Email/username",pady=5,padx=10)
email_label.grid(row=2,column=0,sticky="w")

password_label = Label(text="Password",pady=5,padx=10)
password_label.grid(row=3,column=0,sticky="w")

# ENTRY
website_entry = Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(index=0,string=DEFAULT_EMAIL) # INSET ke through Entry box me kuch bhi already fill karskte hai, Index me 0 / END LIKHTE HAI:
                                                            # 0 means ki entry box ke ekdm leftmost start point me likhna start hoga
                                                            # END means ki agar entry box me already kuch likha hua hai, to uss text ke baad likhayega

password_entry = Entry(width=31)
password_entry.grid(row=3,column=1,sticky = 'w')

# BUTTONS
generate_password = Button(text="Generate Password",width=14,command=gen_password)
generate_password.grid(row=3,column=1,columnspan=2,sticky='e')

add_button = Button(text="Add",width=42,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()