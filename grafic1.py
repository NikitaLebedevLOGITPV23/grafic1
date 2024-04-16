from tkinter import *
from tkinter import messagebox as mb

def save_user_data_to_file(username, password):
    with open("userdata.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

def tehtudvalik(var, nimi, text):
    f = var.get()
    if f:
        text.configure(show="")
        nimi.configure(image=pilt1)
    else:
        text.configure(show="*")
        nimi.configure(image=pilt2)

def autoriseerimine():
    kasutajanimi = kasutaja.get()
    parool = texbox.get() 
    if (kasutajanimi, parool) in kasutajad:
        mb.showinfo("Autentimine", f"Tere tulemast, {kasutajanimi}!")
    else:
        mb.showerror("Autentimine", "Kasutajanimi ei ole registreeritud!")

def registreerimine():
    kasutajanimi2 = kasutaja2.get()
    parool2 = texbox2.get()
    if (kasutajanimi2, parool2) not in kasutajad:
        kasutajad.append((kasutajanimi2, parool2))
        mb.showinfo("Registreerimine", f"Kasutaja {kasutajanimi2} registreeritud!")
        save_user_data_to_file(kasutajanimi2, parool2)
    else:
        mb.showerror("Registreerimine", "Kasutajanimi on juba registreeritud!")

def muuda():
    vana_kasutajanimi = kasutaja_muuda.get()
    vana_parool = texbox_muuda.get()
    uus_kasutajanimi = uus_kasutaja.get()
    uus_parool = uus_texbox.get()
    kasutaja_info = (vana_kasutajanimi, vana_parool)
    if kasutaja_info in kasutajad:
        kasutajad.remove(kasutaja_info)
        kasutajad.append((uus_kasutajanimi, uus_parool))
        mb.showinfo("Muuda nime ja paroolit", "Kasutaja andmed edukalt muudetud!")
    else:
        mb.showerror("Muuda nime ja paroolit", "Sellist kasutajat ei leitud!")

aken = Tk()
aken.geometry("900x600")
aken.title("Autoriseerimine või registreerimine")
aken.configure(bg="#000000")
aken.iconbitmap("icon.ico")

kasutajad = []

pealkiri = Label(aken, text="Autoriseerimine", 
                 bg="#f5f0f2", fg="#141414", 
                 cursor="spider", 
                 font="Impact 16", 
                 justify=CENTER, 
                 height=2, 
                 width=50)
raam = Frame(aken)
kasutaja_label = Label(raam, 
                       text="Kasutajanimi:", 
                       bg="#f5f0f2",
                      fg="#141414", 
                      font="Impact 16")
kasutaja = Entry(raam, 
                 bg="#f5f0f2", 
                 fg="#141414", 
                 cursor="spider", 
                 font="Impact 16", 
                 width=16)
parool_label = Label(raam, 
                     text="Parool:", 
                     bg="#f5f0f2", 
                     fg="#141414", 
                     font="Impact 16")
texbox = Entry(raam, bg="#f5f0f2", 
               fg="#141414", 
               cursor="spider", 
               font="Impact 16", 
               width=16,
              show="*")
pilt1 = PhotoImage(file="pyimage1.png")
pilt2 = PhotoImage(file="pyimage1.png")
var1 = BooleanVar()
valik = Checkbutton(raam, image=pilt2, variable=var1, onvalue=True, offvalue=False, command=lambda: tehtudvalik(var1, valik, texbox))
nupp = Button(raam, text="Sisenema", 
              bg="#f5f0f2", 
              fg="#141414", 
              cursor="spider", 
              width=16, 
              font="Impact 16",
              command=autoriseerimine)

pealkiri2 = Label(aken, 
                  text="Registreerimine", 
                  bg="#f5f0f2", 
                  fg="#141414", 
                  cursor="spider", 
                  font="Impact 16", 
                  justify=CENTER, 
                  height=2, 
                  width=50)
raam2 = Frame(aken)
kasutaja2_label = Label(raam2, 
                        text="Kasutajanimi:",
                       bg="#f5f0f2", 
                       fg="#141414",
                      font="Impact 16")
kasutaja2 = Entry(raam2, 
                  bg="#f5f0f2", 
                  fg="#141414", 
                  cursor="spider", 
                  font="Impact 16", 
                  width=16)
parool2_label = Label(raam2, 
                      text="Parool:",
                     bg="#f5f0f2", 
                     fg="#141414", 
                     font="Impact 16")
texbox2 = Entry(raam2, 
                bg="#f5f0f2", 
                fg="#141414", 
                cursor="spider", 
                font="Impact 16", 
                width=16, show="*")
var2 = BooleanVar()
valik2 = Checkbutton(raam2, 
                     image=pilt2,
                    variable=var2, 
                    onvalue=True,
                   offvalue=False,
                  command=lambda: tehtudvalik(var2, valik2, texbox2))
nupp2 = Button(raam2, 
               text="Registreerima", 
               bg="#f5f0f2", 
               fg="#141414", 
               cursor="spider", 
               width=16,
               font="Impact 16",
               command=registreerimine)

pealkiri3 = Label(aken, 
                  text="Muuda nime ja paroolit",
                 bg="#f5f0f2", 
                 fg="#141414", 
                 cursor="spider", 
                 font="Impact 16", 
                 justify=CENTER, 
                 height=2, 
                 width=50)
raam3 = Frame(aken)
kasutaja_muuda_label = Label(raam3, 
                             text="Kasutajanimi:", 
                             bg="#f5f0f2", 
                             fg="#141414", 
                             font="Impact 16")
kasutaja_muuda = Entry(raam3, 
                       bg="#f5f0f2", 
                       fg="#141414", 
                       cursor="spider", 
                       font="Impact 16",
                      width=16)
parool_muuda_label = Label(raam3, 
                           text="Parool:", 
                           bg="#f5f0f2", 
                           fg="#141414", 
                           font="Impact 16")
texbox_muuda = Entry(raam3, 
                     bg="#f5f0f2", 
                     fg="#141414",
                    cursor="spider", 
                    font="Impact 16", 
                    width=16, 
                    show="*")
uus_kasutaja_label = Label(raam3, 
                           text="Uus kasutajanimi:",
                          bg="#f5f0f2", 
                          fg="#141414", 
                          font="Impact 16")
uus_kasutaja = Entry(raam3,
                    bg="#f5f0f2", 
                    fg="#141414", 
                    cursor="spider", 
                    font="Impact 16",
                   width=16)
uus_parool_label = Label(raam3,
                        text="Uus parool:",
                       bg="#f5f0f2", 
                       fg="#141414", 
                       font="Impact 16")
uus_texbox = Entry(raam3, 
                   bg="#f5f0f2",
                  fg="#141414", 
                  cursor="spider", 
                  font="Impact 16", 
                  width=16, 
                  show="*")
nupp_muuda = Button(raam3, 
                    text="Muudab nime ja paroolit", 
                    bg="#f5f0f2",
                    fg="#141414", 
                    cursor="spider", 
                    font="Impact 16",
                    width=30,
                   command=muuda)
pealkiri2.pack()
raam2.pack()
kasutaja2_label.grid(row=0, column=0)
kasutaja2.grid(row=1, column=0)
parool2_label.grid(row=0, column=1)
texbox2.grid(row=1, column=1)
valik2.grid(row=1, column=2)
nupp2.grid(row=1, column=3)

pealkiri.pack()
raam.pack()
kasutaja_label.grid(row=0, column=0)
kasutaja.grid(row=1, column=0)
parool_label.grid(row=0, column=1)
texbox.grid(row=1, column=1)
valik.grid(row=1, column=2)
nupp.grid(row=1, column=3)

pealkiri3.pack()
raam3.pack()
kasutaja_muuda_label.grid(row=0, column=0)
kasutaja_muuda.grid(row=1, column=0)
parool_muuda_label.grid(row=0, column=1)
texbox_muuda.grid(row=1, column=1)
uus_kasutaja_label.grid(row=2, column=0) 
uus_kasutaja.grid(row=3, column=0)
uus_parool_label.grid(row=2, column=1)
uus_texbox.grid(row=3, column=1)  
nupp_muuda.grid(row=4, columnspan=2)

aken.mainloop()

