
import tkinter
from tkinter import*
wind = Tk()
wind.geometry('400x300+500+200')
wind.title('fprekini')
tex= Label(wind, text='Ievadiet divus skaitlus')
tex.pack()
ent1 = Entry(wind, width=20)
ent1.pack()
ent2= Entry (wind, width=20)
ent2.pack()


btn_sum= Button(wind, bg='pink',fg='black', font=('',20), text='saskaitisana',command=lambda: ('+'))

btn_sum.place(x = 100, y = 100 , width = 200, heigh= 50)

btn_min= Button(wind, bg='pink',fg='black', font=('',20), text='atnemsana', command=lambda: ('-'))

btn_min.place(x = 100, y = 150 , width = 200, heigh= 50)

btn_dal= Button(wind, bg='pink',fg='black', font=('',20), text='dalisana', command=lambda: ('/'))

btn_dal.place(x = 100, y = 200 , width = 200, heigh= 50)

btn_reiz= Button(wind, bg='pink',fg='black', font=('',20), text='reizinasana', command=lambda: ('*'))

btn_reiz.place(x = 100, y = 250 , width = 200, heigh= 50)
wind.mainloop()