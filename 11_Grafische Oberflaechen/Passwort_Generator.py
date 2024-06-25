import customtkinter #pip install customtkinter
import random

def pwCreatorSimple(pwLength:int)->str:
    import string
    pwPool=string.hexdigits + string.punctuation
    return "".join(random.sample(pwPool, pwLength))

def pwCreatorPro1(lows:int, caps:int, nums:int, specs:int=0)->str:
    import string
    lowLetters=random.sample(string.ascii_lowercase, lows)
    capLetters=random.sample(string.ascii_uppercase, caps)
    numbers=random.sample(string.digits, nums)
    specChar=random.sample(string.punctuation, specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    random.shuffle(pw)
    return "".join(pw)

root=customtkinter.CTk()

radioVar=customtkinter.StringVar(value="other")
chooseGen=False #SimpleGen when False

root.title('Passwortgenerator')
root.geometry('400x400')

def chooseSimple():
        global chooseGen
        chooseGen=False
        lblLows.place_forget()
        lblCaps.place_forget()
        lblNums.place_forget()
        lblSpecs.place_forget()
        inLows.place_forget()
        inCaps.place_forget()
        inNums.place_forget()
        inSpecs.place_forget()
        lblGenSimple.place(relx=0.15, rely=0.3)
        inGenSimple.place(relx=0.45, rely=0.3)


def choosePro():
        global chooseGen
        chooseGen=True
        lblGenSimple.place_forget()
        inGenSimple.place_forget()
        lblLows.place(relx=0.1, rely=0.15)
        inLows.place(relx=0.6, rely=0.15)
        lblCaps.place(relx=0.1, rely=0.25)
        inCaps.place(relx=0.6, rely=0.25)
        lblNums.place(relx=0.1, rely=0.35)
        inNums.place(relx=0.6, rely=0.35)
        lblSpecs.place(relx=0.1, rely=0.45)
        inSpecs.place(relx=0.6, rely=0.45)

def chooseAction():  
    if chooseGen:
        lblPassword.configure(text=pwCreatorPro1(int(inLows.get()) if inLows.get() else 0, 
                                                 int(inCaps.get()) if inCaps.get() else 0,
                                                 int(inNums.get()) if inNums.get() else 0, 
                                                 int(inSpecs.get()) if inSpecs.get() else 0))  
    if not chooseGen and inGenSimple.get()!="":
        lblPassword.configure(text=pwCreatorSimple(int(inGenSimple.get())))

def copyClipboard():
     lblPassword.clipboard_clear()
     lblPassword.clipboard_append(lblPassword.cget('text'))

radGenSimple=customtkinter.CTkRadioButton(root, text="Einfacher Generator", variable=radioVar, command=chooseSimple)
radGenSimple.place(relx=0.1, rely=0.05)

radGenPro=customtkinter.CTkRadioButton(root, text="Parametrierter Generator", variable=radioVar, command=choosePro)
radGenPro.place(relx=0.5, rely=0.05)

lblGenSimple=customtkinter.CTkLabel(root, text_color='RED', text='Anzahl Zeichen:', font=('Helvetica', 15))
inGenSimple =customtkinter.CTkEntry(root, border_color='RED')

lblLows=customtkinter.CTkLabel(root, text_color='RED', text='Anzahl Kleinbuchstaben:', font=('Helvetica', 15))
inLows =customtkinter.CTkEntry(root, border_color='RED')

lblCaps=customtkinter.CTkLabel(root, text_color='RED', text='Anzahl Großbuchstaben:', font=('Helvetica', 15))
inCaps =customtkinter.CTkEntry(root, border_color='RED')

lblNums=customtkinter.CTkLabel(root, text_color='RED', text='Anzahl Zahlen:', font=('Helvetica', 15))
inNums =customtkinter.CTkEntry(root, border_color='RED')

lblSpecs=customtkinter.CTkLabel(root, text_color='RED', text='Anzahl Sondereichen:', font=('Helvetica', 15))
inSpecs =customtkinter.CTkEntry(root, border_color='RED')

btnGen=customtkinter.CTkButton(root, text="Generieren", command=chooseAction)
btnGen.place(relx=0.05, rely=0.6, relwidth=0.4)

btnGenCopy=customtkinter.CTkButton(root, text="Copy to Clipboard", command=copyClipboard)
btnGenCopy.place(relx=0.55, rely=0.6, relwidth=0.4)

lblPassword=customtkinter.CTkLabel(root, bg_color='RED', text="Passwort", text_color='BLACK', font=('Helvetica', 25))
lblPassword.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)




root.mainloop()