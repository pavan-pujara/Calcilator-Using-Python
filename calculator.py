from tkinter import *

def off_function():
   t1.delete(0, END)
   for b in x:
      b["state"]=DISABLED

def on_function():
   for b in x:
      b["state"]=NORMAL

def clear_all():
   t1.delete(0, END)

def backspace():
   n = len(t1.get())
   t1.delete(n-1, n)

def add_text(new_text):
   old_text = t1.get()
   t1.delete(0, END) #Why
   t1.insert(0, old_text+new_text)
   
   global choice
   if(new_text=='+' or new_text=='-' or new_text=='x' or new_text=='/'):
      choice = new_text
      
   
def find_answer():
   str1 = t1.get()
   i = str1.index(choice)
   left = str1[:i]
   right = str1[i+1:]

   if choice=='+':
      answer = float(left) + float(right)
   if choice=='-':
      answer = float(left) - float(right)
   if choice=='x':
      answer = float(left) * float(right)
   if choice=='/':
      answer = float(left) / float(right)

   t1.delete(0, END)
   t1.insert(0, str(answer))

master = Tk()
master.title('Calculator')
master.geometry('280x380+400+200')

t1 = Entry(master, width=23)
t1.place(x=23,y=20)

r = IntVar(value=2)
'''
In some cases one of the radiobuttons could be selected by default bcos of something called tristate mode.
value=2 makes sure that both the radio buttons will be deselected in the begining.
value=1 selects ON. value=0 selects OFF
Instead of value = 2, we could have given any value except 1 and 0
'''
r1 = Radiobutton(master, text="ON", variable=r, value=1, command=on_function)
r2 = Radiobutton(master, text="OFF", variable=r, value=0, command=off_function)
r1.place(x=20,y=50)
r2.place(x=20,y=80)
bt1 = Button(master, text='←', width=5, height=2, command=backspace)
bt1.place(x=80,y=55)
bt2 = Button(master, text='C', width=5, height=2, command=clear_all)
bt2.place(x=140,y=55)
bt3 = Button(master, text='+', width=5, height=2, command=lambda:add_text('+'))
bt3.place(x=200,y=55)

b7 = Button(master, text='7', width=5, height=2, command=lambda:add_text('7'))
b7.place(x=20,y=115)
b8 = Button(master, text='8', width=5, height=2, command=lambda:add_text('8'))
b8.place(x=80,y=115)
b9 = Button(master, text='9', width=5, height=2, command=lambda:add_text('9'))
b9.place(x=140,y=115)
bt4 = Button(master, text='-', width=5, height=2, command=lambda:add_text('-'))
bt4.place(x=200,y=115)

b4 = Button(master, text='4', width=5, height=2, command=lambda:add_text('4'))
b4.place(x=20,y=175)
b5 = Button(master, text='5', width=5, height=2, command=lambda:add_text('5'))
b5.place(x=80,y=175)
b6 = Button(master, text='6', width=5, height=2, command=lambda:add_text('6'))
b6.place(x=140,y=175)
bt5 = Button(master, text='x', width=5, height=2, command=lambda:add_text('x'))
bt5.place(x=200,y=175)

b1 = Button(master, text='1', width=5, height=2, command=lambda: add_text('1'))
b1.place(x=20,y=235)
b2 = Button(master, text='2', width=5, height=2, command=lambda:add_text('2'))
b2.place(x=80,y=235)
b3 = Button(master, text='3', width=5, height=2, command=lambda:add_text('3'))
b3.place(x=140,y=235)
bt6 = Button(master, text='/', width=5, height=2, command=lambda:add_text('/'))
bt6.place(x=200,y=235)

b0 = Button(master, text='0', width=5, height=2, command=lambda:add_text('0'))
b0.place(x=20,y=295)
bt7 = Button(master, text='.', width=5, height=2, command=lambda:add_text('.'))
bt7.place(x=80,y=295)
bt8 = Button(master, text='=', width=11, height=2, command=find_answer)
bt8.place(x=140,y=295)

x=[t1,b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8]
choice = ''

master.mainloop()
