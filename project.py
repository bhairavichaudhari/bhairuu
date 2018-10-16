

	
	

'''
Attachment auditclgfinal.ppt added.Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
python 
Click here to enable
desktop notifications for Gmail.   
Learn more
  
Hide

4 of about 68
python code
Inbox
x

Tejaswini Yeola
Attachments
Fri 12 Oct, 16:07 (3 days ago)
to me, Tejaswini, dipaleeghoderao


Attachments area
'''
'''
Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
Click here to enable
desktop notifications for Gmail.   
Learn more
  
Hide

5 of 1,502
Python
Inbox
x

DIPALEE GHODERAO
Attachments
14:52 (5 hours ago)
to me, Tejaswini


Attachments area
'''
from tkinter import *         #standard python interface to thr GUI toolkit
import random            #random no generation ----------betn 0 and 1-----ant random functions
import time;              #
import datetime            #
from tkinter import Tk, StringVar, ttk         #(tkinter.ttk=button,checkbutton,entry,frame,label....)
from tkinter.messagebox import showinfo         #use the function showinfo() where the parameters are the window title and text.


root=Tk()                       #Creating an instance of Tk initializes this interpreter and creates the root window.
root.geometry("1350x750+0+0")
root.title(" Food Ordering System")
#--------ithparyant screen tayar hote-------------

Tops = Frame (root, width = 1350 , height=100, bd=6, relief="raise")#(bd=The size of the border around the indicator. Default is 2 pixels)
#relief=With the default value, relief=FLAT, the checkbutton does not stand out from its background. You may set this option to any of the other styles
#height=The vertical dimension of the new frame.
Tops.pack(side=TOP)                   #This geometry manager organizes widgets in blocks before placing them in the parent widget.
#-----------ithe vrchi frame tayar hote, ji fast food restayrant chya navakhali rahil--------------------

lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="\t Food Ordering System\t\t\t")
lblTitle.grid(row =0, column=0)
#------------ithe fast food restaurant as heading yet---------------------

BottomMainFrame = Frame (root, width = 1350 , height=650, bd=6, relief="raise")
BottomMainFrame.pack(side=BOTTOM)
#----------ithe right side chi frame tayar hote------------------

f1 = Frame (BottomMainFrame, width=450 , height=650, bd=2,relief="raise")
f1.pack(side=LEFT)

f2 = Frame (BottomMainFrame, width = 450 , height=650, bd=2, relief="raise")
f2.pack(side=LEFT)

f2TOP = Frame (f2, width=450 , height=350, bd= 2, relief="raise")
f2TOP.pack(side=TOP)

f2BOTTOM = Frame (f2, width = 450 , height=300, bd= 1, relief="raise")
f2BOTTOM.pack(side=BOTTOM)
#---------------F2 MADHE EK FRAME TAYAR ZALI----------------------

f3 = Frame (BottomMainFrame, width = 450 , height=650, bd= 0, relief="raise")
f3.pack(side=RIGHT)
#---------------madhe 2 ubhya frames tayar hotil---------------

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=StringVar()
var23=IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set("")
var23.set(0)


varFries =StringVar()
varSalad =StringVar()
varBurger =StringVar()
varPizza =StringVar()
varPasta =StringVar()
varMaggi =StringVar()
varOmelette =StringVar()
varChickenSandwich =StringVar()

varGulabJamun =StringVar()
varKajuKatli =StringVar()
varKulfi =StringVar()
varSoanPapdi =StringVar()
varRabri =StringVar()

varTea =StringVar()
varCola =StringVar()
varColdCoffee =StringVar()
varMangoJuice =StringVar()
varLassi =StringVar()

varOreoShake =StringVar()
varVanillaShake =StringVar()
varStrawberryShake =StringVar()

varChange =StringVar()
varSubTotal =StringVar()
varTotal =StringVar()
varVAT= StringVar()
varTax= StringVar()
varPayment =IntVar()




varFries.set("0")
varSalad.set("0")
varBurger.set("0")
varPizza.set("0")
varPasta.set("0")
varMaggi.set("0")
varOmelette.set("0")
varChickenSandwich.set("0")
varTotal.set("0")
varPayment.set(" ")

varGulabJamun.set("0")
varKajuKatli.set("0")
varKulfi.set("0")
varSoanPapdi.set("0")
varRabri.set("0")

varTea.set("0")
varCola.set("0")
varColdCoffee.set("0")
varMangoJuice.set("0")
varLassi.set("0")
varOreoShake.set("0")
varVanillaShake.set("0")
varStrawberryShake.set("0")


varVAT.set("")
varTax.set("0")
varTotal.set("0")
varChange.set("0")
varSubTotal.set("0")


def iExit():
    qExit= messagebox.askyesno("Fast Food","Do you want to Quit?")
    if qExit >0:
        root.destroy()
        return

def Reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)





    varFries.set("0")
    varSalad.set("0")
    varBurger.set("0")
    varPizza.set("0")
    varPasta.set("0")
    varMaggi.set("0")
    varOmelette.set("0")
    varChickenSandwich.set("0")
    varTotal.set("0")

    varGulabJamun.set("0")
    varKajuKatli.set("0")
    varKulfi.set("0")
    varSoanPapdi.set("0")
    varRabri.set("0")

    varTea.set("0")
    varCola.set("0")
    varColdCoffee.set("0")
    varMangoJuice.set("0")
    varLassi.set("0")
    varOreoShake.set("0")
    varVanillaShake.set("0")
    varStrawberryShake.set("0")

    #varChange.set("0")
    #varSubTotal.set("0")

#=======================
    varVAT.set("")
    varTax.set("0")
    varTotal.set("0")
    varChange.set(" ")
    varSubTotal.set("0")
    varPayment.set(" ")

#====================





    

    txtFries.configure(state =DISABLED)
    txtSalad.configure(state =DISABLED)
    txtBurger.configure(state =DISABLED)
    txtPizza.configure(state =DISABLED)
    txtPasta.configure(state =DISABLED)
    txtMaggi.configure(state =DISABLED)
    txtOmelette.configure(state =DISABLED)
    txtChickenSandwich.configure(state =DISABLED)
    txtGulabJamun.configure(state =DISABLED)
    txtKajuKatli.configure(state =DISABLED)
    txtKulfi.configure(state =DISABLED)
    txtSoanPapdi.configure(state =DISABLED)
    txtRabri.configure(state =DISABLED)
    txtTea.configure(state =DISABLED)
    txtCola.configure(state =DISABLED)
    txtColdCoffee.configure(state =DISABLED)
    txtMangoJuice.configure(state =DISABLED)
    txtLassi.configure(state =DISABLED)
    txtOreoShake.configure(state =DISABLED)
    txtVanillaShake.configure(state =DISABLED)
    txtStrawberryShake.configure(state =DISABLED)
    #txtPayment.configure(state =DISABLED)
    txtChange.configure(state =DISABLED)
    txtTax.configure(state =DISABLED)
    txtSubTotal.configure(state =DISABLED)
    txtTotal.configure(state =DISABLED)
    var8.get() == 0


def chkFries():
    if (var1.get() == 1):
        txtFries.configure(state = NORMAL)
        varFries.set("")
        
    elif (var1.get() == 0):
        txtFries.configure(state = DISABLED)
        varFries.set("0")
    
def chkSalad():
    if (var2.get() == 1):
        txtSalad.configure(state = NORMAL)
        varSalad.set("") 
        
    elif (var2.get() == 0):
        txtSalad.configure(state = DISABLED)
        varSalad.set("0")

def chkBurger():
    if (var3.get() == 1):
        txtBurger.configure(state = NORMAL)
        varBurger.set("")
        
    elif (var3.get() == 0):
        txtBurger.configure(state = DISABLED)
        varBurger.set("0")


def chkPizza():
    if (var4.get() == 1):
        txtPizza.configure(state = NORMAL)
        varPizza.set("")
        
    elif (var4.get() == 0):
        txtPizza.configure(state = DISABLED)
        varPizza.set("0")


def chkPasta():
    if (var5.get() == 1):
        txtPasta.configure(state = NORMAL)
        varPasta.set("")
        
    elif (var5.get() == 0):
        txtPasta.configure(state = DISABLED)
        varPasta.set("0")





def chkMaggi():
    if (var6.get() == 1):
        txtMaggi.configure(state = NORMAL)
        varMaggi.set("")
        
    elif (var6.get() == 0):
        txtMaggi.configure(state = DISABLED)
        varMaggi.set("0")

def chkOmelette():
    if (var7.get() == 1):
        txtOmelette.configure(state = NORMAL)
        varOmelette.set("")
        
    elif (var7.get() == 0):
        txtOmelette.configure(state = DISABLED)
        varOmelette.set("0")

def chkChickenSandwich():
    if (var8.get() == 1):
        txtChickenSandwich.configure(state = NORMAL)
        varChickenSandwich.set("")
        
    elif (var8.get() == 0):
        txtChickenSandwich.configure(state = DISABLED)
        varChickenSandwich.set("0")


def chkGulabJamun():
    if (var9.get() == 1):
        txtGulabJamun.configure(state = NORMAL)
        varGulabJamun.set("")
        
    elif (var9.get() == 0):
        txtGulabJamun.configure(state = DISABLED)
        varGulabJamun.set("0")


def chkKajuKatli():
    if (var10.get() == 1):
        txtKajuKatli.configure(state = NORMAL)
        varKajuKatli.set("")
        
    elif (var10.get() == 0):
        txtKajuKatli.configure(state = DISABLED)
        varKajuKatli.set("0")





def chkKulfi():
    if (var11.get() == 1):
        txtKulfi.configure(state = NORMAL)
        varKulfi.set("")
        
    elif (var11.get() == 0):
        txtKulfi.configure(state = DISABLED)
        varKulfi.set("0")



def chkSoanPapdi():
    if (var12.get() == 1):
        txtSoanPapdi.configure(state = NORMAL)
        varSoanPapdi.set("")
        
    elif (var12.get() == 0):
        txtSoanPapdi.configure(state = DISABLED)
        varSoanPapdi.set("0")

def chkRabri():
    if (var13.get() == 1):
        txtRabri.configure(state = NORMAL)
        varRabri.set("")
        
    elif (var13.get() == 0):
        txtRabri.configure(state = DISABLED)
        varRabri.set("0")

def chkTea():
    if (var14.get() == 1):
        txtTea.configure(state = NORMAL)
        varTea.set("")
        
    elif (var14.get() == 0):
        txtTea.configure(state = DISABLED)
        varTea.set("0")



def chkCola():
    if (var15.get() == 1):
        txtCola.configure(state = NORMAL)
        varCola.set("")
        
    elif (var15.get() == 0):
        txtCola.configure(state = DISABLED)
        varCola.set("0")




        

def chkColdCoffee():
    if (var16.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        varColdCoffee.set("")
        
    elif (var16.get() == 0):
        txtColdCoffee.configure(state =DISABLED)
        varColdCoffee.set("0")



def chkMangoJuice():
    if (var17.get() == 1):
        txtMangoJuice.configure(state = NORMAL)
        varMangoJuice.set("")
        
    elif (var17.get() == 0):
        txtMangoJuice.configure(state = DISABLED)
        varMangoJuice.set("0")



def chkLassi():
    if (var18.get() == 1):
        txtLassi.configure(state = NORMAL)
        varLassi.set("")
        
    elif (var18.get() == 0):
        txtLassi.configure(state = DISABLED)
        varLassi.set("0")



def chkOreoShake():
    if (var19.get() == 1):
        txtOreoShake.configure(state = NORMAL)
        varOreoShake.set("")
        
    elif (var19.get() == 0):
        txtOreoShake.configure(state = DISABLED)
        varOreoShake.set("0")




def chkVanillaShake():
    if (var20.get() == 1):
        txtVanillaShake.configure(state = NORMAL)
        varVanillaShake.set("")
        
    elif (var20.get() == 0):
        txtVanillaShake.configure(state = DISABLED)
        varVanillaShake.set("0")


def chkStrawberryShake ():
    if (var21.get() == 1):
        txtStrawberryShake.configure(state = NORMAL)
        varStrawberryShake.set("")
        
    elif (var21.get() == 0):
        txtStrawberryShake.configure(state = DISABLED)
        varStrawberryShake.set("0")


def costofmeal():
   meal1 = float(varFries.get())
   meal2 = float(varSalad.get())
   meal3 = float(varBurger.get())
   meal4 = float(varPizza.get())
   meal5 = float(varPasta.get())
   meal6 = float(varMaggi.get())
   meal7 = float(varOmelette.get())
   meal8 = float(varChickenSandwich.get())
   meal9 = float(varGulabJamun.get())
   meal10 = float(varKajuKatli.get())
   meal11 = float(varKulfi.get())
   meal12 = float(varSoanPapdi.get())
   meal13 = float(varRabri.get())
   meal14 = float(varTea.get())
   meal15 = float(varCola.get())
   meal16 = float(varColdCoffee.get())
   meal17 = float(varMangoJuice.get())
   meal18 = float(varLassi.get())
   meal19 = float(varOreoShake.get())
   meal20 = float(varVanillaShake.get())
   meal21 = float(varStrawberryShake.get())

   iTotal1=((meal1 * 50) + (meal2 * 40) + (meal3 * 100) + (meal4 * 70))
   iTotal2=((meal5 * 50) + (meal6 * 30) + (meal7 * 40) + (meal8 * 80))
   iTotal3=((meal9 * 140) + (meal10 * 250) + (meal11 * 20) + (meal12 * 40))
   iTotal4=((meal13 * 60) + (meal14 * 25) + (meal15 * 30) + (meal16 * 40))
   iTotal5=((meal17 * 50) + (meal18 * 50) + (meal19 * 80) + (meal20 * 90)+ (meal21 *60))
   


   if (var22.get() == "Cash"):
       iChange = float(varPayment.get())
       iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
       iTax = (iCost * 3.4)/100
       iTaxq="Rs.", str('%.2f'%(iTax))
       varTax.set(iTaxq)

       iCostq="Rs.", str('%.2f'%(iCost))
       varSubTotal.set(iCostq)
       iTotalq="Rs.", str('%.2f'%((iCost + iTax)))
       varTotal.set(iTotalq)
       cChange = (iChange - (iCost + iTax))
       cChangeq = "Rs.", str('%.2f'%(cChange))
       varChange.set(cChangeq)
   elif(var22.get() == "Master Card" or "Visa Master Card" or "Debit Card"):
       varPayment.set("")
       iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
       iTax= (iCost * 3.4)/100
       iTaxq="Rs.", str('%.2f'(iTax))
       varTax.set(iTaxq)
       iCostq="Rs.", str('%.2f'%(iCost))
       varSubTotal.set(iCostq)
       iTotalq="Rs.", str('%.2f'((iCost + iTax)))
       varTotal.set(iTotalq)
       varChange.set("")


       


    

#-------------------------------frame1-----------------------------------------------------------
lblmeal = Label(f1, font=('arial', 20, 'bold'), text="Fast  meal and vagetarian\t\n")
lblmeal.grid(row =0, column=0)

Fries =Checkbutton(f1, text="Fries\t\tRs.50", variable=var1, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkFries).grid(row=1, column=0,sticky=W)
txtFries =Entry(f1,font=('arial',18,'bold'), textvariable =varFries, width =6, justify ='right', state =DISABLED )
txtFries.grid(row =1 , column =1)

Salad =Checkbutton(f1, text="Salad\t\tRs.40", variable=var2, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkSalad).grid(row=2, column=0,sticky=W)
txtSalad =Entry(f1,font=('arial',18,'bold'), textvariable =varSalad, width =6, justify ='right', state =DISABLED)
txtSalad.grid(row =2 , column =1)

Burger =Checkbutton(f1, text="Burger\t\tRs.100", variable=var3, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkBurger).grid(row=3, column=0,sticky=W)
txtBurger =Entry(f1,font=('arial',18,'bold'), textvariable =varBurger, width =6, justify ='right', state =DISABLED)
txtBurger.grid(row =3 , column =1)

Pizza =Checkbutton(f1, text="Pizza\t\tRs.70", variable=var4, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkPizza).grid(row=4, column=0,sticky=W)
txtPizza =Entry(f1,font=('arial',18,'bold'), textvariable =varPizza, width =6, justify ='right', state =DISABLED)
txtPizza.grid(row =4 , column =1)


Pasta =Checkbutton(f1, text="Pasta\t\tRs.50", variable=var5, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkPasta).grid(row=5, column=0,sticky=W)
txtPasta =Entry(f1,font=('arial',18,'bold'), textvariable =varPasta, width =6, justify ='right', state =DISABLED)
txtPasta.grid(row =5 , column =1)

#----------------------------------------------------------------------------------
#lblMeal = Label(f1, font=('arial',20,'bold'), text="\nSandwiches\n")
#lblMeal.grid(row =6, column=0)
#----------------------------------------------------------------------------------

Maggi =Checkbutton(f1, text="Maggi\t\tRs.30", variable=var6, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkMaggi).grid(row=6, column=0,sticky=W)
txtMaggi =Entry(f1,font=('arial',18,'bold'), textvariable =varMaggi, width =6, justify ='right', state =DISABLED)
txtMaggi.grid(row =6 , column =1)


Omelette =Checkbutton(f1, text="Omelette\t\tRs.40", variable=var7, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkOmelette).grid(row=7, column=0,sticky=W)
txtOmelette =Entry(f1,font=('arial',18,'bold'), textvariable =varOmelette, width =6, justify ='right', state =DISABLED)
txtOmelette.grid(row =7 , column =1)


ChickenSandwich =Checkbutton(f1, text="ChickenSandwich\tRs.80", variable=var8, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkChickenSandwich).grid(row=8, column=0,sticky=W)
txtChickenSandwich =Entry(f1,font=('arial',18,'bold'), textvariable =varChickenSandwich, width =6, justify ='right', state =DISABLED)
txtChickenSandwich.grid(row =8, column =1)

lblspace=Label( f1, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row =10 ,column=0)


#------------------------frame2------------------------------------


lblMeal = Label(f2TOP, font=('arial', 18, 'bold'), text="Desserts\n")
lblMeal.grid(row =0, column=0)

GulabJamun =Checkbutton(f2TOP, text="GulabJamun\tRs.140", variable=var9, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkGulabJamun).grid(row=1, column=0,sticky=W)
txtGulabJamun =Entry(f2TOP,font=('arial',18,'bold'), textvariable =varGulabJamun, width =6, justify ='right', state =DISABLED)
txtGulabJamun.grid(row =1 , column =1)

KajuKatli =Checkbutton(f2TOP, text="KajuKatli\tRs.250", variable=var10, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkKajuKatli).grid(row=2, column=0,sticky=W)
txtKajuKatli =Entry(f2TOP,font=('arial',18,'bold'), textvariable =varKajuKatli, width =6, justify ='right', state =DISABLED)
txtKajuKatli.grid(row =2 , column =1)

Kulfi =Checkbutton(f2TOP, text="Kulfi\t\tRs.20", variable=var11, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkKulfi).grid(row=3, column=0,sticky=W)
txtKulfi =Entry(f2TOP,font=('arial',18,'bold'), textvariable =varKulfi, width =6, justify ='right', state =DISABLED)
txtKulfi.grid(row =3 , column =1)

SoanPapdi =Checkbutton(f2TOP, text="SoanPapdi\tRs.40", variable=var12, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkSoanPapdi).grid(row=4, column=0,sticky=W)
txtSoanPapdi =Entry(f2TOP,font=('arial',18,'bold'), textvariable =varSoanPapdi, width =6, justify ='right', state =DISABLED)
txtSoanPapdi.grid(row =4 , column =1)


Rabri =Checkbutton(f2TOP, text="Rabri\t\tRs.60", variable=var13, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkRabri).grid(row=5, column=0,sticky=W)
txtRabri =Entry(f2TOP,font=('arial',18,'bold'), textvariable =varRabri, width =6, justify ='right', state =DISABLED)
txtRabri.grid(row =5 , column =1)


#--------------------------------frame3--------------------------------------------------------------------------

lblMeal = Label(f3, font=('arial', 18, 'bold'), text="Drinks\n")
lblMeal.grid(row =0, column=0)

Tea =Checkbutton(f3, text="Tea\t\tRs.25", variable=var14, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkTea).grid(row=1, column=0,sticky=W)
txtTea =Entry(f3,font=('arial',18,'bold'), textvariable =varTea, width =6, justify ='right', state =DISABLED)
txtTea.grid(row =1 , column =1)

Cola =Checkbutton(f3, text="Cola\t\tRs.30", variable=var15, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkCola).grid(row=2, column=0,sticky=W)
txtCola =Entry(f3,font=('arial',18,'bold'), textvariable =varCola, width =6, justify ='right', state =DISABLED)
txtCola.grid(row =2 , column =1)

ColdCoffee =Checkbutton(f3, text="ColdCoffee\tRs.40", variable=var16, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkColdCoffee).grid(row=3, column=0,sticky=W)
txtColdCoffee =Entry(f3,font=('arial',18,'bold'), textvariable =varColdCoffee, width =6, justify ='right', state =DISABLED)
txtColdCoffee.grid(row =3 , column =1)

MangoJuice =Checkbutton(f3, text="MangoJuice\tRs.50", variable=var17, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkMangoJuice).grid(row=4, column=0,sticky=W)
txtMangoJuice =Entry(f3,font=('arial',18,'bold'), textvariable =varMangoJuice, width =6, justify ='right', state =DISABLED)
txtMangoJuice.grid(row =4 , column =1)


Lassi =Checkbutton(f3, text="Lassi\t\tRs.50", variable=var18, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkLassi).grid(row=5, column=0,sticky=W)
txtLassi =Entry(f3,font=('arial',18,'bold'), textvariable =varLassi, width =6, justify ='right', state =DISABLED)
txtLassi.grid(row =5 , column =1)

#------------------------------------------------------------------------------------
lblShakes = Label(f3, font=('arial',20,'bold'), text="\nShakes\n")
lblShakes.grid(row =6, column=0)

OreoShake =Checkbutton(f3, text="Oreo Shake\tRs.80", variable=var19, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkOreoShake).grid(row=7, column=0,sticky=W)
txtOreoShake = Entry(f3,font=('arial',18,'bold'), textvariable =varOreoShake, width =6, justify ='right', state =DISABLED)
txtOreoShake.grid(row =7 , column =1)

VanillaShake = Checkbutton(f3, text="Vanilla Shake\tRs.90", variable=var20, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkVanillaShake).grid(row=8, column=0,sticky=W)
txtVanillaShake= Entry(f3,font=('arial',18,'bold'), textvariable =varVanillaShake, width =6, justify ='right', state =DISABLED)
txtVanillaShake.grid(row =8 , column =1)




StrawberryShake=Checkbutton(f3, text="Strawberry Shake\tRs.60", variable=var21, onvalue =1, offvalue=0,
                   font=('arial',18,'bold'),command=chkStrawberryShake).grid(row=9, column=0, sticky=W)
txtStrawberryShake = Entry(f3,font=('arial',18,'bold'), textvariable =varStrawberryShake, width =6, justify ='right', state =DISABLED)
txtStrawberryShake.grid(row =9 , column =1)

lblspace=Label( f3, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row=10, column =0)

#-------------------------------------------------------------------------------------------------------------------------

lblPaymentMethod = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Payment Method", bd=10, width= 16, anchor='w')
lblPaymentMethod.grid(row=0,column=0)

lblChange = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Change", bd=10, anchor='w')
lblChange.grid(row=0,column=1)
txtChange= Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varChange, width =6, justify='right', state =DISABLED)
txtChange.grid(row =0 , column=2)


#--------------------------------------------------------------

'''

self.cmbBxMen1 = Combobox(self, values = data, width = 60)
self.cmbBxMen1.grid(row=0, column=1, padx = 4, pady = 20)

def __init__(self, master):
        
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
       
        

def create_widgets(self):
        
        data = Application.data
        
        self.cmbBxMen1 = Combobox(self, values = data, width = 60).grid(row=0, column=1, padx = 4, pady = 20)
        self.btnAdMen = Button(self, text = "Add to Menu", command = self.Add_To_Menu).grid(row=0, column=9, pady = 20, sticky = W)

def Add_To_Menu(self):

        menuItem1 = self.cmbBxMen1.get()

        '''
#----------------------------------------------------------------
cmbPaymentMethod = ttk.Combobox(f2BOTTOM , textvariable = var22, state='readonly', font=('arial',10, 'bold'), width= 20)
cmbPaymentMethod['value']=('Cash','Master Card','Visa Card','Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1,column=0)

lblTax = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Tax    ",bd=10, anchor='w')
lblTax.grid(row =1,column =1)
txtTax = Entry(f2BOTTOM,font=('arial',18, 'bold'), textvariable =varTax, width =6, justify='right',state =DISABLED)
#txtTax = Entry(f2BOTTOM,font=('arial',18, 'bold'), textvariable =var23, width =6, justify='left',state =DISABLED)
txtTax.grid(row =1 , column =2)

txtPayment = Entry(f2BOTTOM,font=('arial',18,'bold'), textvariable =varPayment, width =6, justify='right')#, state =DISABLED)
txtPayment.grid(row =2 , column =0)
lblSubTotal = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Sub Total", bd=10, width =8,anchor='w')
lblSubTotal.grid(row=2,column=1)
txtSubTotal = Entry(f2BOTTOM ,font=('arial',18, 'bold'), textvariable =varSubTotal,  width =6, justify='right', state =DISABLED)
txtSubTotal.grid(row =2 , column =2)

lblTotal = Label(f2BOTTOM , font=('arial',14, 'bold'), text="Total", bd=10, width =6,anchor='w')
lblTotal.grid(row=3,column=1)
txtTotal = Entry(f2BOTTOM ,font=('arial',18,'bold'), textvariable =varTotal,  width =6, justify='right', state =DISABLED)
txtTotal.grid(row =3 , column =2)

#------------------------------------------------------------------------------------------------------------------------------

btnTotal=Button(f2BOTTOM,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'), width=5,
                text="Total " , command = costofmeal).grid(row=4, column=0)
                #text="Total" , command = Total).grid(row=4, column=0)
btnReset=Button(f2BOTTOM,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Reset", command =Reset).grid(row=4, column=1)
btnExit=Button(f2BOTTOM,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'), width=5,
               text="Exit",command=lambda: iExit()).grid(row=4, column=2)
lblspace=Label( f2BOTTOM, text="\n\n\n\n\n\n\n")
lblspace.grid(row=5, column=0)

root.mainloop()
'''
menu.py
Displaying menu.py.

'''

