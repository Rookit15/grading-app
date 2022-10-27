import os
from tkinter import *
from PIL import ImageTk, Image


a_list=[] ## set to global so I can access it in different methods
root = Tk() ## root window set
root.title('Grade this')
root.geometry("500x600")


def main():
    
    global count

    path= os.getcwd()
    root.iconbitmap(path)
    Descritpion= Label(root, text="Grade product show with buttons below").grid(row=0, columnspan=7)
    makelists()
    count= len(list_images)
    imgLabel= Label(image=list_images[0])
    imgLabel.grid(row=1,columnspan=7)
        
    Goodbutton= Button(root, text="S tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(2)).grid(row=2,column=0)

    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(2)).grid(row=2,column=1)

    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(2)).grid(row=2, column=2)

    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(2)).grid(row=2, column=3)

    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(2)).grid(row=2, column=4)

    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(2)).grid(row=2, column=5)

    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(2)).grid(row=2, column=6)

def makelists():
    global list_images
    global small_images
    my_image1= ImageTk.PhotoImage(Image.open("pics/longdrink.jpg").resize((500,500), Image.Resampling.LANCZOS))

    my_image2=ImageTk.PhotoImage(Image.open("pics/banana.jpg").resize((500,500), Image.Resampling.LANCZOS))
    my_image3=ImageTk.PhotoImage(Image.open("pics/karhu.jfif").resize((500,500), Image.Resampling.LANCZOS))
    my_image4=ImageTk.PhotoImage(Image.open("pics/breezer.png").resize((500,500), Image.Resampling.LANCZOS))
    my_image5=ImageTk.PhotoImage(Image.open("pics/cider.jpg").resize((500,500), Image.Resampling.LANCZOS))
    my_image6=ImageTk.PhotoImage(Image.open("pics/sandels.jpg").resize((500,500), Image.Resampling.LANCZOS))
    my_image7=ImageTk.PhotoImage(Image.open("pics/longdrinkKoff.jpg").resize((500,500), Image.Resampling.LANCZOS))
    list_images = [my_image1,my_image2, my_image3, my_image4,my_image5,my_image6,my_image7]

    small_image2=ImageTk.PhotoImage(Image.open("pics/banana.jpg").resize((55,55), Image.Resampling.LANCZOS))
    small_image1= ImageTk.PhotoImage(Image.open("pics/longdrink.jpg").resize((55,55), Image.Resampling.LANCZOS))
    small_image3=ImageTk.PhotoImage(Image.open("pics/karhu.jfif").resize((55,55), Image.Resampling.LANCZOS))
    small_image4=ImageTk.PhotoImage(Image.open("pics/breezer.png").resize((55,55), Image.Resampling.LANCZOS))
    small_image5=ImageTk.PhotoImage(Image.open("pics/cider.jpg").resize((55,55), Image.Resampling.LANCZOS))
    small_image6=ImageTk.PhotoImage(Image.open("pics/sandels.jpg").resize((55,55), Image.Resampling.LANCZOS))
    small_image7=ImageTk.PhotoImage(Image.open("pics/longdrinkKoff.jpg").resize((55,55), Image.Resampling.LANCZOS))
    
    small_images= [small_image1, small_image2, small_image3, small_image4, small_image5, small_image6, small_image7]





def makeTopLevel(): ## opens new window and makes your chart
    top = Toplevel()
    top.geometry("1000x900")
    top.title('Result')
    top.configure(bg='black')
    resultTitle= Label(top,fg='white', text="Results are shown here", font= 'Helvetica 20 bold', bg='black').grid(row=0, columnspan=8)
    
    tierS= Label(top, text="S tier", background='orange red',padx=15, pady=50, font=8, fg='black',width=10).grid(row=1,rowspan=2, column=0)
    tierA= Label(top, text="A tier", background='dark orange',padx=15, pady=50, font=8, fg='black', width=10).grid(row=3, rowspan=2, column=0)
    tierB= Label(top,text="B tier", background='yellow',padx=15, pady=50, font=8, fg='black', width=10).grid(row=5, rowspan=2, column=0)
    tierC= Label(top,text="C tier", background='green',padx=15, pady=50, font=8, fg='black', width=10).grid(row=7, rowspan=2, column=0)
    tierD= Label(top,text="D tier", background='cyan',padx=15, pady=50, font=8, fg='black', width=10).grid(row=9, rowspan=2, column=0)
    tierE= Label(top,text="E tier", background='SlateBlue1',padx=15, pady=50, font=8, fg='black', width=10).grid(row=11, rowspan=2, column=0)
    tierF= Label(top,text="F tier", background='maroon1',padx=15, pady=50, font=8, fg='black', width=10).grid(row=13, rowspan=2, column=0)

    sTierInfo=[1,1]
    aTierInfo=[3,1]
    bTierInfo=[5,1]
    cTierInfo=[7,1]
    dTierInfo=[9,1]
    eTierInfo=[11,1]
    fTierInfo=[13,1]
    for i in range(count):
        
        if a_list[i]==0:
            imgLabel= Label(top,image=small_images[i]).grid(row=sTierInfo[0],column=sTierInfo[1])
            sTierInfo[0]=sTierInfo[0]+1
            if sTierInfo[0]==3:
                sTierInfo[0]=1
                sTierInfo[1]=sTierInfo[1]+1
        elif a_list[i]==1:
            imgLabel= Label(top,image=small_images[i]).grid(row=aTierInfo[0],column=aTierInfo[1])
            aTierInfo[0]=aTierInfo[0]+1
            if aTierInfo[0]==5:
                aTierInfo[0]=3
                aTierInfo[1]=aTierInfo[1]+1
        elif a_list[i]==2:
            imgLabel= Label(top,image=small_images[i]).grid(row=bTierInfo[0],column=bTierInfo[1])
            bTierInfo[0]=bTierInfo[0]+1
            if bTierInfo[0]==7:
                bTierInfo[0]=5
                bTierInfo[1]=bTierInfo[1]+1
        elif a_list[i]==3:
            imgLabel= Label(top,image=small_images[i]).grid(row=cTierInfo[0],column=cTierInfo[1])
            cTierInfo[0]=cTierInfo[0]+1
            if cTierInfo[0]==9:
                cTierInfo[0]=7
                cTierInfo[1]=cTierInfo[1]+1
        elif a_list[i]==4:
            imgLabel= Label(top,image=small_images[i]).grid(row=dTierInfo[0],column=dTierInfo[1])
            dTierInfo[0]=dTierInfo[0]+1
            if dTierInfo[0]==11:
                dTierInfo[0]=9
                dTierInfo[1]=dTierInfo[1]+1
        elif a_list[i]==5:
            imgLabel= Label(top,image=small_images[i]).grid(row=eTierInfo[0],column=eTierInfo[1])
            eTierInfo[0]=eTierInfo[0]+1
            if eTierInfo[0]==13:
                eTierInfo[0]=11
                eTierInfo[1]=eTierInfo[1]+1
        elif a_list[i]==6:
            imgLabel= Label(top,image=small_images[i]).grid(row=fTierInfo[0],column=fTierInfo[1])
            fTierInfo[0]=fTierInfo[0]+1
            if aTierInfo[0]==15:
                fTierInfo[0]=13
                fTierInfo[1]=fTierInfo[1]+1
        

    
    

def Good(number): ##Good button function
    global imgLabel
    
    if count == number-1:
        a_list.append(0)
        makeTopLevel()
        return
   
    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=7)
    
    Goodbutton= Button(root, text="S Tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(number+1)).grid(row=2, column=2)
    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(number+1)).grid(row=2, column=3)
    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(number+1)).grid(row=2, column=4)
    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(number+1)).grid(row=2, column=5)
    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(number+1)).grid(row=2, column=6)
    a_list.append(0)
    
def Bad(number): ##bad button function
    global imgLabel
    if count == number-1:
        a_list.append(1)
        makeTopLevel()
        return

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=7)
    
    Goodbutton= Button(root, text="S Tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(number+1)).grid(row=2, column=2)
    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(number+1)).grid(row=2, column=3)
    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(number+1)).grid(row=2, column=4)
    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(number+1)).grid(row=2, column=5)
    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(number+1)).grid(row=2, column=6)
    a_list.append(1)
    
def bTier(number):
    global imgLabel
    if count == number-1:
        a_list.append(2)
        makeTopLevel()
        return

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=7)
    
    Goodbutton= Button(root, text="S Tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(number+1)).grid(row=2, column=2)
    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(number+1)).grid(row=2, column=3)
    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(number+1)).grid(row=2, column=4)
    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(number+1)).grid(row=2, column=5)
    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(number+1)).grid(row=2, column=6)
    a_list.append(2)

def cTier(number):
    global imgLabel
    if count == number-1:
        a_list.append(3)
        makeTopLevel()
        return

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=7)
    
    Goodbutton= Button(root, text="S Tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(number+1)).grid(row=2, column=2)
    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(number+1)).grid(row=2, column=3)
    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(number+1)).grid(row=2, column=4)
    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(number+1)).grid(row=2, column=5)
    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(number+1)).grid(row=2, column=6)
    a_list.append(3)

def dTier(number):
    global imgLabel
    if count == number-1:
        a_list.append(4)
        makeTopLevel()
        return

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=7)
    
    Goodbutton= Button(root, text="S Tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(number+1)).grid(row=2, column=2)
    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(number+1)).grid(row=2, column=3)
    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(number+1)).grid(row=2, column=4)
    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(number+1)).grid(row=2, column=5)
    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(number+1)).grid(row=2, column=6)
    a_list.append(4)

def eTier(number):
    global imgLabel
    if count == number-1:
        a_list.append(5)
        makeTopLevel()
        return

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=7)
    
    Goodbutton= Button(root, text="S Tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(number+1)).grid(row=2, column=2)
    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(number+1)).grid(row=2, column=3)
    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(number+1)).grid(row=2, column=4)
    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(number+1)).grid(row=2, column=5)
    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(number+1)).grid(row=2, column=6)
    a_list.append(5)

def fTier(number):
    global imgLabel
    if count == number-1:
        a_list.append(6)
        makeTopLevel()
        return

    imgLabel= Label(image=list_images[number-1]).grid(row=1,columnspan=7)
    
    Goodbutton= Button(root, text="S Tier", fg='black', bg='orange red',padx=10, pady=5 , command=lambda: Good(number+1)).grid(row=2,column=0)
    badButton=Button(root, text="A tier", fg='black', bg='dark orange', padx=10, pady=5,command=lambda: Bad(number+1)).grid(row=2,column=1)
    BTier= Button(root, text='B tier',fg = 'black', bg='yellow', padx= 10, pady= 5, command=lambda: bTier(number+1)).grid(row=2, column=2)
    CTier= Button(root, text='C tier',fg = 'black', bg='green', padx= 10, pady= 5, command=lambda: cTier(number+1)).grid(row=2, column=3)
    DTier= Button(root, text='D tier',fg = 'black', bg='cyan', padx= 10, pady= 5, command=lambda: dTier(number+1)).grid(row=2, column=4)
    ETier= Button(root, text='E tier',fg = 'black', bg='SlateBlue1', padx= 10, pady= 5, command=lambda: eTier(number+1)).grid(row=2, column=5)
    DTier= Button(root, text='F tier',fg = 'black', bg='maroon1', padx= 10, pady= 5, command=lambda: fTier(number+1)).grid(row=2, column=6)
    a_list.append(6)


main()
root.mainloop()
