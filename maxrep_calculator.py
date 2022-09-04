from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("CAGE MAX REP CALC")

canvas = Canvas(master , height=600 , width=900)
canvas.pack()
frame_genel = Frame(master , bg="#8FFF00")
frame_genel.place(relx = 0.05 , rely = 0.05,  relwidth = 0.90 , relheight = 0.90)


yazi = Label(frame_genel , text = "Lutfen Agirlik Giriniz" , font = "Verdana 10 bold" , bg = "#8FFF00")
yazi.place(relx = 0.1 , rely = 0.1)

agirlik_entry = Entry(frame_genel)
agirlik_entry.place( relx = 0.1 , rely = 0.15 , relwidth = 0.05 , relheight= 0.05)

yazi1 = Label(frame_genel , text = "Lutfen Tekrar Sayisi Giriniz [0-6]" , font = "Verdana 10 bold" , bg = "#8FFF00")
yazi1.place(relx = 0.1 , rely = 0.21)

rep_entry = Entry(frame_genel)
rep_entry.place( relx = 0.1 , rely = 0.25 , relwidth = 0.05 , relheight= 0.05)

yazi2 = Label(frame_genel , text = "Lütfen RPE Değeri Seçiniz" , font = "Verdana 10 bold" , bg = "#8FFF00")
yazi2.place(relx = 0.45 , rely = 0.02)




def commands():
    if var.get():
        if var.get()== 6 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/86.3))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/83.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/81.1))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/78.6))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/76.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/73.9))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")

        elif var.get()== 7 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/87.8))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/85))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/82.4))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/79.9))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/77.4))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/75.1))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")

        elif var.get()== 8 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/89.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/86.3))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/83.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/81.1))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/78.6))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/76.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")

        elif var.get()== 9 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/90.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/87.8))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/85))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/82.4))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/79.9))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/77.4))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")

        elif var.get()== 10 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/92.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/89.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/86.3))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/83.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/81.1))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/78.6))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")

        elif var.get()== 11 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/93.9))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/90.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/87.8))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/85))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/82.4))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/79.9))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")

        elif var.get()== 12 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/95.5))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/92.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/89.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/86.3))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/83.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/81.1))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")

        elif var.get()== 13 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/97.8))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/93.9))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/90.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/87.8))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/85))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/82.4))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")


        elif var.get()== 14 : 
            i1 = int(rep_entry.get())
            i2 = int(agirlik_entry.get())
            if i1 == 1 : 
                sonuc = round(i2*(100/100))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 2 : 
                sonuc = round(i2*(100/95.5))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 3 : 
                sonuc = round(i2*(100/92.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 4 : 
                sonuc = round(i2*(100/89.2))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 5 : 
                sonuc = round(i2*(100/86.3))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)
            elif i1 == 6 : 
                sonuc = round(i2*(100/83.7))
                Label(frame_genel , text = "Max Tekrarınız : " , font = "Times 30 bold" , bg = "#8FFF00" ).place(relx = 0.1 , rely = 0.55 )
                Label(frame_genel , text = "{} kg".format(sonuc) , font= "Times 40 bold" , bg = "#8FFF00").place(relx = 0.1 , rely = 0.7 , relwidth= 0.2)

            else : 
                messagebox.showwarning("UYARI" ,"Lutfen Girdiğiniz Değerleri Kontrol Ediniz")
    else : 
        messagebox.showwarning("UYARI" ,"Lutfen RPE Değeri Giriniz")












buton = Button(frame_genel , text = "Max Rep hesapla" , command= commands)
buton.place(relx = 0.1 , rely = 0.32)
var = IntVar()
r6= Radiobutton(frame_genel , text = "6" , variable = var , value = 6 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r6.place(relx= 0.5 , rely = 0.1)    
r6h= Radiobutton(frame_genel , text = "6.5" , variable = var , value = 7 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r6h.place(relx= 0.55, rely = 0.1)  
r7= Radiobutton(frame_genel , text = "7" , variable = var , value = 8 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r7.place(relx= 0.5, rely = 0.15) 
r7h= Radiobutton(frame_genel , text = "7.5" , variable = var , value = 9,font = "Verdana 10 bold" , bg="#FFFFFF")
r7h.place(relx= 0.55, rely = 0.15)  
r8= Radiobutton(frame_genel , text = "8" , variable = var , value = 10 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r8.place(relx= 0.5, rely = 0.2) 
r8h= Radiobutton(frame_genel , text = "8.5" , variable = var , value = 11 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r8h.place(relx= 0.55, rely = 0.2) 
r9= Radiobutton(frame_genel , text = "9" , variable = var , value = 12 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r9.place(relx= 0.5, rely = 0.25) 
r9h= Radiobutton(frame_genel , text = "9.5" , variable = var , value = 13 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r9h.place(relx= 0.55, rely = 0.25) 
r10= Radiobutton(frame_genel , text = "10" , variable = var , value = 14 ,font = "Verdana 10 bold" , bg="#FFFFFF")
r10.place(relx= 0.525, rely = 0.3) 


master.mainloop()