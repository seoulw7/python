import tkinter as tk #2 UI간결하게

win=tk.Tk() 
win.title('계산기') 
disValue=0
str_value=tk.StringVar()
str_value.set(str(disValue)) #set  자동변경
dis=tk.Entry(win, textvariable=str_value, justify='right')
dis.grid(column=0, row=0, columnspan=4, ipadx=70, ipady=30)

calItems = [['1','2','3','4'], #2
['5','6','7','8'],
['9','0','+','-'],
['*','/','c','=']] 

for i,items in enumerate(calItems):
    for j,item in enumerate(items):
        try:
            num = int(item)
            color='orange'
        except:
            color='gray'
        btn = tk.Button(win,
        text=item,
        width=10,
        height=5,
        bg=color,
        fg='black',
        command=lambda cmd=item:click(cmd)
        )
        btn.grid(column=j, row=(i+1))

win.mainloop() 
