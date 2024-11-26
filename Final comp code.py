#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''If a ball is projected with a speed of 10m/s  at what time will the ball reach it's maximum height? 
| 1 second     | 2 seconds   | 10 minutes  | 1 minute    |   1'''


# In[2]:


import mysql.connector as mc
from tkinter import *
import webbrowser
from tkinter import messagebox as mb
mydb=mc.connect(host="localhost",user="root",password="root",database= "quiz")
mycursor=mydb.cursor()
q_no=0
def Interface():
    global root
    root=Tk()
    root.geometry('1200x1000')
    root.resizable(0,0)
    root.config(bg='black')
    label1=Label(root,text='WELCOME TO PHYSICS QUIZ',font=('Hadassah Friedlaender',36,'bold'),bg='#FF9899',
                 fg='black',width='100')
    label1.grid(row=1)
    label1.place(anchor='n', relx=0.5, rely=0.0)
    root.title('Physics Quiz')
    label2=Label(root,text='CHOOSE ANY OPTION',font=('Times New Roman',30,'bold'),bg='black',fg='#FF9899')
    label2.grid(row=4)
    label2.place(anchor='n', relx=0.5, rely=0.1)
    button1=Button(root,text='ENTER QUESTIONS',padx='25',pady='10',bg='#FF9899',fg='black',width='18',
                   font=('Times New Roman',20,'bold'),command=Question)
    button2=Button(root,text='ATTEMPT QUIZ',padx='25',pady='10',bg='#FF9899',fg='black',width='18',
                   font=('Times New Roman',20,'bold'),command=callpopup3)
    button3=Button(root,text='VIEW INFO',padx='25',pady='10',bg='#FF9899',fg='black',width='18',
                   font=('Times New Roman',20,'bold'),command=figure)
    button1.place(anchor='n', relx=0.5, rely=0.2)
    button2.place(anchor='n', relx=0.5, rely=0.4)
    button3.place(anchor='n', relx=0.5, rely=0.3)
    root.mainloop()


def Question():
    ques=Tk()
    qid=StringVar(ques)
    q=StringVar(ques)
    op1=StringVar(ques)
    op2=StringVar(ques)
    op3=StringVar(ques)
    op4=StringVar(ques)
    ans=IntVar(ques)
    
    ques.geometry('1200x1000')
    ques.resizable(0,0)
    ques.config(bg='black')
    label3=Label(ques,text='QUESTION PORTAL',font=('Optima',36,'bold'),
                 bg='#F6B092',fg='BLACK',width='100').place(anchor='n', relx=0.5, rely=0.0)
    label5=Label(ques,text='Enter question number',font=('Imperial',18),
                 bg='black',fg='#F6B092').place(anchor='n', relx=0.2, rely=0.15)
    label6=Label(ques,text='Enter question',font=('Imperial',18),
                 bg='black',fg='#F6B092').place(anchor='n', relx=0.2, rely=0.2)
    label7=Label(ques,text='Enter option 1',font=('Imperial',18),
                 bg='black',fg='#F6B092').place(anchor='n', relx=0.2, rely=0.25)
    label8=Label(ques,text='Enter option 2',font=('Imperial',18),
                 bg='black',fg='#F6B092').place(anchor='n', relx=0.2, rely=0.3)
    label9=Label(ques,text='Enter option 3',font=('Imperial',18),
                 bg='black',fg='#F6B092').place(anchor='n', relx=0.2, rely=0.35)
    label10=Label(ques,text='Enter option 4',font=('Imperial',18),
                  bg='black',fg='#F6B092').place(anchor='n', relx=0.2, rely=0.4)
    label11=Label(ques,text='Enter correct option',font=('Imperial',18),
                  bg='black',fg='#F6B092').place(anchor='n', relx=0.2, rely=0.45)
    ent6=Entry(ques,textvariable=q).place(anchor='n', relx=0.36, rely=0.21)
    ent7=Entry(ques,textvariable=op1).place(anchor='n', relx=0.36, rely=0.255)
    ent8=Entry(ques,textvariable=op2).place(anchor='n', relx=0.36, rely=0.31)
    ent9=Entry(ques,textvariable=op3).place(anchor='n', relx=0.36, rely=0.355)
    ent5=Entry(ques,textvariable=qid).place(anchor='n', relx=0.36, rely=0.155)
    ent10=Entry(ques,textvariable=op4).place(anchor='n', relx=0.36, rely=0.41)
    ent11=Entry(ques,textvariable=ans).place(anchor='n', relx=0.36, rely=0.455)

    def clearfields():
       
        op1.set("")
        op2.set("")
        op3.set("")
        op4.set('')
        ans.set(value=None)
        qid.set("")
        q.set('')
        popup2.destroy()
    def quit():
            popup2.destroy()
            ques.destroy()
    def callpopup2():
        def quit():
            popup2.destroy()
            ques.destroy()
        global popup2
        popup2= Tk()
        popup2.wm_title('')
        popup2.config(bg='black')
        popup2.eval('tk::PlaceWindow . center')
        label=Label(popup2, text="Do you want to add more questions?",bg='black',fg='white',font=("Arial Bold", 12))
        label.pack(side='top',fill="x", padx=10,pady=50)
        B1 = Button(popup2, text="Yes", bg='black',fg='white',font=('bold'),command =clearfields).place(relx=0.38, rely=0.7)
        B2 = Button(popup2, text="No", bg='black',fg='white',font=('bold'),command=quit).place(relx=0.5, rely=0.7)
        
    def insertvalues():
        qid1=qid.get()
        q1=q.get()
        op11=op1.get()
        op21=op2.get()
        op31=op3.get()
        op41=op4.get()
        ans1=ans.get()
        sql="INSERT INTO question VALUES (%s, %s, %s, %s, %s,%s,%s)"
        val=(qid1,q1,op11,op21,op31,op41,ans1)
        mycursor.execute(sql,val)
        mydb.commit()
        def callpopup1(title,msg1):
            popup1= Tk()
            popup1.wm_title(title)
            popup1.config(bg='black')
            popup1.eval('tk::PlaceWindow . center')
            label=Label(popup1, bg='black',fg='white',text=msg1,font=("Arial Bold", 12))
            label.pack(side="top", fill="x", pady=10)
            B1 = Button(popup1, text="Okay", bg='black',fg='white',font=('bold'),command = popup1.destroy)
            B1.pack()
            popup1.mainloop()
        msg1=str(mycursor.rowcount)+" Record inserted"
        callpopup1("Successful",msg1)
    btn1=Button(ques,text='Next',padx='15',pady='10',bg='#F6B092',fg='black',font=("Arial Bold", 14),
                command=callpopup2).place(anchor='n', relx=0.7, rely=0.5)
    btn2=Button(ques,text='Save',padx='15',pady='10',bg='#F6B-092',fg='black',font=("Arial Bold", 14),
                command=insertvalues).place(anchor='n', relx=0.8, rely=0.5)

def figure():
    def quit():
        global root
        root.destroy()
        anm.destroy()
    def callback(url):
        webbrowser.open_new_tab(url)
    anm=Tk()
    anm.title('view info')
    anm.config(bg='black')
    anm.resizable(0,0)
    label=Label(anm, text='''Welcome to the Quiz!
    This quiz is related to the motion of a bouncing ball on a fixed platform.
    Before attempting the quiz, it is recommended that you observe the ball's motion and some useful graphs related to it.
    Click on the given button below.''',bg='black',fg='white',font=('Helveticabold', 15))
    label.pack()
    button = Button(anm, text="Click here",bg='white',font=('Helveticabold', 15),command=quit)
    button.bind("<Button-1>", lambda e:
        callback("https://glowscript.org/#/user/aisv6/folder/MyPrograms/program/Motionofabouncingball"))
    button.pack()
    anm.mainloop()
    
def Quiz():
    global gui
    gui = Tk()
    gui.geometry("1200x1000")
    gui.resizable(0,0)
    gui.title("Quiz")
    gui.config(bg='black')
    global question,options,answer,q_no
    q_no=0
    question = (data['question'])
    options = (data['options'])
    answer = (data['answer'])
    display_title()
    display_question()
    r_b()
    buttons()
    global data_size
    data_size=len(question)
    global correct
    correct=0
    gui.mainloop()
    
def display_result():
    global correct
    wrong_count = data_size - correct
    correct1 = f"Correct: {correct}"
    wrong = f"Wrong: {wrong_count}"
    score = int((correct) / data_size * 100)
    result = f"Score: {score}%"
    mb.showinfo("Result", f"{result}\n{correct1}\n{wrong}")
def check_ans(q_no):
        print(q_no)
        print(opt_selected.get())
        print(answer[q_no])
        if opt_selected.get() == answer[q_no]:
            return True
def next_btn():
        global q_no,correct,data_size
        if check_ans(q_no):
            print('opt_selected is',opt_selected.get())
            correct += 1
        q_no += 1
        print(q_no)

        if q_no==data_size:

            display_result()
            gui.destroy()
        else:

            display_question()
            r_b()
            
def buttons():
        next_button = Button(gui, text="Next",command=next_btn,width=10,bg="#A4DE02",fg="black",font=("ariel",16,"bold"))
        next_button.place(x=1000,y=380)
        quit_button = Button(gui, text="Quit", command=gui.destroy,width=5,bg="blue", fg="white",font=("ariel",16," bold"))
        quit_button.place(x=900,y=380)

def display_question():
        Q_no = Label(gui, text=str(q_no+1)+') '+question[q_no], width=120,bg='black',fg='white',font=( 'ariel' ,15, 'bold' ),
                     anchor= 'nw' )
        Q_no.place(x=2, y=100)
        
def display_title():
        title = Label(gui, text="Physics QUIZ",width=40, bg="#A4DE02",fg="black", font=("ariel", 36, "bold"))
        title.place(x=0, y=2)
        
def checktry():
        print('You have selected'+str(opt_selected.get()))
        
def r_b():
    global opt_selected,opts
    opt_selected=IntVar(gui,value=None)
    y_pos=180
    opts=[]
    for option in options[q_no]:
        opts.append(str(option))
    print('opts is',opts)
    for Index,Text in enumerate(opts):
        print('index is',Index,'and text is',Text)
        radio_btn=Radiobutton(gui,text=(Text),width=20,variable=opt_selected,value=Index+1,bg='white',font = ("ariel",14),
                              command=checktry, state=NORMAL)
        radio_btn.place(anchor='w',x=100,y=y_pos)
        y_pos+=60
        print('selected option is',opt_selected)
          
def callpopup3():
        def quit1():
            popup.destroy()
            figure()
        def quit2():
        
            popup.destroy()
            quiz=Quiz()
        
        popup=Tk()
        popup.title('Recommendation')
        popup.config(bg='black')
        popup.eval('tk::PlaceWindow . center')
        popup.resizable(0,0)
        label=Label(popup,text='''Before you attempt the quiz,
        it is recommended that you view the animation of the bouncing ball, and graphs related to it.
        Click 'Take me there' to view.
       
        If you have already viewed, please click 'Already viewed'.  
       
        ''',bg='black',fg='white',font=("arial bold",14)).pack()
        ok=Button(popup, text="Take Me There",font=('arial bold',12),bg='black',fg='Cyan',width='15',command=quit1).pack()
        done=Button(popup, text="Already Viewed",font=('arial bold',12),bg='black',fg='Cyan',width='15',command=quit2).pack()
        popup.mainloop()

def obtques():
        q='select * from question'
        mycursor.execute(q)
        a=mycursor.fetchall()
        mydb.commit()
        d={}
        l1,l2,l3=[],[],[]
        for i in range(len(a)):
            l1.append(a[i][1])
            l2.append(int(a[i][6]))
            l=[]
            for j in range(4):
                l.append(a[i][j+2])
            l3.append(l)
        d['options']=l3
        d['question']=l1
        d['answer']=l2
        return d
data=obtques()
Interface()


# In[ ]:




