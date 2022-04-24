from distutils.spawn import spawn
import random
from cProfile import label
from sqlite3 import Row
from tkinter import *
from traceback import FrameSummary
from turtle import width
from tkinter import ttk
import ttkthemes

#importing all the classes and methods of this module

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x735+200+10')#window width and height created here
root.resizable(0,0)#it disable the maximize of the window 

#lets create frame
mainframe=Frame(root,bd=4)
mainframe.grid()#This is our mainframe all things added to this frame only

titleframe=Frame(mainframe,bg='black')
titleframe.grid()
#we create label for adding text to the frame

titlelabel=Label(titleframe,text='Welcome to Typing Master',font=('algerian',28,'bold'),bg='goldenrod3',fg='white',
width=38)
titlelabel.grid(pady=5,padx=3)

#After title frame we are adding paragraph frame
#now we will create a paragrapgh frame 
paragraph_frame=Frame(mainframe)
paragraph_frame.grid(row=1,column=0)
paragraph_List=['Cows, also known as ruminants, are four-legged terrestrial animals. They have two horns, one long tail, and their soft skin with or without fur. They are mammals and give birth to calves. Cows are often referred to as ‘mother’ as they provide human beings with irreplaceable commodities.',
' School is the place where we start our learning. Apart from learning to read, write, and excel in academics, the school also teaches us valuable life lessons that we can incorporate in our daily lives. It is the place where the foundation of our knowledge and morals are laid. So let’s look at some of the things that are worth remembering about our schools.',
'Water is the only molecule because of which life is possible on Earth. In outer space, the conditions are so hostile that Water cannot be found in its natural form- liquid. This liquid Water has been giving us sustenance throughout billions of years.',
'The living organisms that are eukaryotes and formed of numerous cells and those who sexually reproduce are called animals. Animals play a unique role in maintaining the balance of nature. Several animal species exist in both land and water, and each has a purpose for their existence.']
random.shuffle(paragraph_List)
#use random module to select any random para from list
#now crete lable
label_paragrapgh=Label(paragraph_frame,text=paragraph_List[0],wraplength=912,justify=LEFT,font=('arial',14,'bold'))
label_paragrapgh.grid(row=0,column=0)
textarea_frame=Frame(mainframe)
textarea_frame.grid()
textarea=Text(textarea_frame,font=('arial',12,'bold'),width=100,height=7,bd=4,relief=GROOVE,wrap='word',state=DISABLED)
textarea.grid()
frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text='60',font=('Tahoma',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_label=Label(frame_output,text='Wpm',font=('Tahoma',12,'bold'),fg='red')
wpm_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wpm_count_label.grid(row=0,column=5,padx=5)

accuracy_label=Label(frame_output,text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_label.grid(row=0,column=6,padx=5)

accuracy_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
accuracy_count_label.grid(row=0,column=7,padx=5)

totalwords_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='red')
totalwords_label.grid(row=0,column=8,padx=5)

totalwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
totalwords_count_label.grid(row=0,column=9,padx=5)

wrongwords_label=Label(frame_output,text='Wrong Words',font=('Tahoma',12,'bold'),fg='red')
wrongwords_label.grid(row=0,column=10,padx=5)

wrongwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wrongwords_count_label.grid(row=0,column=11,padx=5)

buttons_Frame=Frame(mainframe)
buttons_Frame.grid(row=4,column=0)

startButton=ttk.Button(buttons_Frame,text='Start')
startButton.grid(row=0,column=0,padx=20)

resetButton=ttk.Button(buttons_Frame,text='Reset',state=DISABLED)
resetButton.grid(row=0,column=1,padx=20)

exitButton=ttk.Button(buttons_Frame,text='Exit')
exitButton.grid(row=0,column=2,padx=20)

#window created till now
keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5,column=0)

frame1to0=Frame(keyboard_frame)
frame1to0.grid(row=0,column=0,pady=3)

label1=Label(frame1to0,text='1',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label1.grid(row=0,column=0,padx=5)

label2=Label(frame1to0,text='2',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label2.grid(row=0,column=1,padx=5)

label3=Label(frame1to0,text='3',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label3.grid(row=0,column=2,padx=5)

label4=Label(frame1to0,text='4',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label4.grid(row=0,column=3,padx=5)

label5=Label(frame1to0,text='5',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label5.grid(row=0,column=4,padx=5)

label6=Label(frame1to0,text='6',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label6.grid(row=0,column=5,padx=5)

label7=Label(frame1to0,text='7',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label7.grid(row=0,column=6,padx=5)

label8=Label(frame1to0,text='8',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label8.grid(row=0,column=7,padx=5)

label9=Label(frame1to0,text='9',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label9.grid(row=0,column=8,padx=5)

label0=Label(frame1to0,text='0',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
label0.grid(row=0,column=9,padx=5)

frameqtop=Frame(keyboard_frame)
frameqtop.grid(row=1,column=0,pady=3)

labelq=Label(frameqtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelq.grid(row=0,column=0,padx=5)

labelw=Label(frameqtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelw.grid(row=0,column=1,padx=5)

labele=Label(frameqtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labele.grid(row=0,column=2,padx=5)

labelr=Label(frameqtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelr.grid(row=0,column=3,padx=5)

labelt=Label(frameqtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelt.grid(row=0,column=4,padx=5)

labely=Label(frameqtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labely.grid(row=0,column=5,padx=5)

labelu=Label(frameqtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelu.grid(row=0,column=6,padx=5)

labeli=Label(frameqtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labeli.grid(row=0,column=7,padx=5)

labelo=Label(frameqtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelo.grid(row=0,column=8,padx=5)

labelp=Label(frameqtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelp.grid(row=0,column=9,padx=5)

frameatol=Frame(keyboard_frame)
frameatol.grid(row=2,column=0,pady=3)

labela=Label(frameatol,text='A',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labela.grid(row=0,column=0,padx=5)

labels=Label(frameatol,text='S',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labels.grid(row=0,column=1,padx=5)

labeld=Label(frameatol,text='D',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labeld.grid(row=0,column=2,padx=5)

labelf=Label(frameatol,text='F',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelf.grid(row=0,column=3,padx=5)

labelg=Label(frameatol,text='G',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelg.grid(row=0,column=4,padx=5)

labelh=Label(frameatol,text='H',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelh.grid(row=0,column=5,padx=5)

labelj=Label(frameatol,text='J',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelj.grid(row=0,column=6,padx=5)

labelk=Label(frameatol,text='K',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelk.grid(row=0,column=7,padx=5)

labell=Label(frameatol,text='L',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labell.grid(row=0,column=8,padx=5)

frameztom=Frame(keyboard_frame)
frameztom.grid(row=3,column=0,pady=3)

labelz=Label(frameztom,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelz.grid(row=0,column=0,padx=5)

labelx=Label(frameztom,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelx.grid(row=0,column=1,padx=5)

labelc=Label(frameztom,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelc.grid(row=0,column=2,padx=5)

labelv=Label(frameztom,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelv.grid(row=0,column=3,padx=5)

labelb=Label(frameztom,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelb.grid(row=0,column=4,padx=5)

labeln=Label(frameztom,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labeln.grid(row=0,column=5,padx=5)

labelm=Label(frameztom,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelm.grid(row=0,column=6,padx=5)

space_frame=Frame(keyboard_frame)
space_frame.grid(row=4,column=0,pady=3)

labelspace=Label(space_frame,bg='black',fg='white',font=('arial',10,'bold'),width=40,height=2,bd=10,relief=GROOVE)
labelspace.grid(row=0,column=0)

def changeBG(widget):
    widget.config(bg='blue')
    widget.after(100,lambda :widget.config(bg='black'))
label_numbers=[label1,label2,label3,label4,label5,label6,label7,label7,label8,label9,label0]
label_alphabets=[labela,labelb,labelc,labeld,labele,labelf,labelg,labelh,labeli,labelj,labelk,labell,labelm,labeln,labelo,labelp,labelq,labelr,labels,labelt,labelu,labelv,labelw,labelx,labely,labelz]
space_label=[labelspace]
binding_numbers=['1','2','3','4','5','6','7','8','9','0']
binding_capital_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

binding_small_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers],lambda event,label=label_numbers[numbers]:changeBG(label))

for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets],lambda event,label=label_alphabets[capital_alphabets]:changeBG(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets],lambda event,label=label_alphabets[small_alphabets]:changeBG(label))

root.bind('<space>',lambda event :changeBG(space_label[0]))

root.mainloop()
