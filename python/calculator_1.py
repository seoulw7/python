import tkinter as tk #1 UI만들기

win=tk.Tk() #1
win.title('계산기') #1
disValue=0 #1
str_value=tk.StringVar() #1
str_value.set(str(disValue)) #set  자동변경
dis=tk.Entry(win, textvariable=str_value, justify='right')
dis.grid(column=0, row=0, columnspan=4, ipadx=70, ipady=30) #1

tk.Button(win, text='1', width=10, height=5).grid(column=0, row=1) #pack 아니고 그리드
tk.Button(win, text='2', width=10, height=5).grid(column=1, row=1)
tk.Button(win, text='3', width=10, height=5).grid(column=2, row=1)
tk.Button(win, text='4', width=10, height=5).grid(column=3, row=1)
tk.Button(win, text='5', width=10, height=5).grid(column=0, row=2) #pack 아니고 그리드
tk.Button(win, text='6', width=10, height=5).grid(column=1, row=2)
tk.Button(win, text='7', width=10, height=5).grid(column=2, row=2)
tk.Button(win, text='8', width=10, height=5).grid(column=3, row=2)
tk.Button(win, text='9', width=10, height=5).grid(column=0, row=3) #pack 아니고 그리드
tk.Button(win, text='0', width=10, height=5).grid(column=1, row=3)
tk.Button(win, text='+', width=10, height=5).grid(column=2, row=3)
tk.Button(win, text='-', width=10, height=5).grid(column=3, row=3)
tk.Button(win, text='*', width=10, height=5).grid(column=0, row=4) #pack 아니고 그리드
tk.Button(win, text='/', width=10, height=5).grid(column=1, row=4)
tk.Button(win, text='c', width=10, height=5).grid(column=2, row=4)
tk.Button(win, text='=', width=10, height=5).grid(column=3, row=4)


win.mainloop() #1
