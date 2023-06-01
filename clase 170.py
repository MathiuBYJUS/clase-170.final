from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("400x400")
root.config(bg="lightgreen")


a=["Boton","Etiqueta","Combobox"]

class clase():
    def __init__(self):
        print("Vamoss a estar ocupando clases para generar elementos de dieño")
        
    def etqueta1(self):
        label_2=Label(root,text="Label creado")
        label_2.pack()
        
    def buton2(self):
        buton_2=Button(root,text="Button creado",command=self.message)
        buton_2.pack(padx=20,pady=20)
        
    def combobox1(self):
        b=["Creaste un combobox usando clases","Hola"]
        combobox1=ttk.Combobox(root,state="readonly",values=b)
        combobox1.pack()
        
    def message(self):
        messagebox.showinfo("Hola!")
        
    def elegir(self):
        global dropdown
        c=combobox.get()
        if (c=="Etiqueta"):
            self.etqueta1()
            
        elif(c=="Boton"):
            self.buton2()
            
        elif(c=="Combobox"):
            self.combobox1()
        
        
 
f=clase()


label_1=Label(root,text="Crea elementos de diseños utilizando clases")
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)
combobox=ttk.Combobox(root,state="readonly",values=a)
combobox.place(relx=0.5,rely=0.3,anchor=CENTER)
button_1=Button(root,text="Dame lick para generar el elemento de diseño deseado",command=f.elegir)
button_1.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()