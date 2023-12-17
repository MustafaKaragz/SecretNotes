import tkinter
from tkinter import messagebox
import base64
window=tkinter.Tk()
window.title("Secret Notes")
window.config(padx=30,pady=30)




                            # MUSTAFA KARAGÖZ



def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)



def save_decrypt_notes():
    title=title_entry.get()
    message=enter_secret_text.get("1.0",tkinter.END)
    master_sec=enter_masterkey_input.get()

    if len(title) ==0 or len(message) ==0 or len(master_sec)==0:
        messagebox.showinfo(title="Error!",message="Please enter all info.")
    else:
        message_encrypted=encode(master_sec,message)
        try:
            with open("mysecretnotes.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecretnotes.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0,tkinter.END)
            enter_masterkey_input.delete(0,tkinter.END)
            enter_secret_text.delete("1.0",tkinter.END)



def decrpyt_notes():
    message_encrpyted=enter_secret_text.get("1.0",tkinter.END)
    master_secret=enter_masterkey_input.get()

    if len(message_encrpyted)==0 or len(master_secret)==0:
        messagebox.showinfo(title="Error!",message="Please enter all info.")
    else:
        try:
            decrypt_message=decode(master_secret,message_encrpyted)
            enter_secret_text.delete("1.0",tkinter.END)
            enter_secret_text.insert("1.0",decrypt_message)
        except:
            messagebox.showerror(title="Error!",message="Please enter encrypt text!")



photo=tkinter.PhotoImage(file="photo.png")
photo_button=tkinter.Label(image=photo)
photo_button.pack()


title_info_label= tkinter.Label(text="Enter Your Title.",font=("Verdana"),pady=10)
title_info_label.pack()

title_entry=tkinter.Entry(width=30)
title_entry.pack()


enter_secret_title=tkinter.Label(text="Enter Your Secret.",font=("Verdana"),pady=10)
enter_secret_title.pack()

enter_secret_text=tkinter.Text(width=50,height=25)
enter_secret_text.pack()


enter_masterkey_title=tkinter.Label(text="Enter Master Key",font=("Verdana"),pady=10)
enter_masterkey_title.pack()

enter_masterkey_input=tkinter.Entry(width=30)
enter_masterkey_input.pack()


save_button=tkinter.Button(text="Save & Encrypt", command=save_decrypt_notes)
save_button.pack()


decrypt_button=tkinter.Button(text="Decrypt",command=decrpyt_notes)
decrypt_button.pack()

window.mainloop()