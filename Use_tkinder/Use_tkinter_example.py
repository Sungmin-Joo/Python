# -*- coding: utf-8 -*-
import tkinter

if __name__ == '__main__':
    window=tkinter.Tk()
    window.title("Sungmin_Joo")
    window.geometry("300x250+100+100")
    window.resizable(False, False)
    
    frame1=tkinter.Frame(window)
    scrollbar=tkinter.Scrollbar(frame1)
    scrollbar.pack(side="right", fill="y")
    listbox=tkinter.Listbox(frame1, yscrollcommand = scrollbar.set)
    listbox.pack(side="left")
    scrollbar["command"]=listbox.yview
    frame1.pack()
    #Use scrollbar with listbox
    
    line = 0
    count=0
    def Up():
        global count,line
        count +=1
        label.config(text=str(count))
        listbox.insert(line, str(line))
        line+=1
        window.attributes("-fullscreen",True)
        #off fullscreen
    def Down():
        global count,line
        if count >0:
            count -=1
        if line >0:
            line -=1
        label.config(text=str(count))
        listbox.delete(line, str(line))
        window.attributes("-fullscreen",False)
        #off fullscreen
    
    label = tkinter.Label(window, text="0")
    label.pack()
    
    frame2=tkinter.Frame(window)
    button1 = tkinter.Button(frame2,text = "up_count", overrelief="solid", width=15, command=Up,repeatdelay=500, repeatinterval=100)
    button1.pack(side = "left")
    button2 = tkinter.Button(frame2,text = "down_count", overrelief="solid", width=15, command=Down,repeatdelay=500, repeatinterval=100)
    button2.pack(side = "right")
    frame2.pack()
    

        
    window.mainloop()
else:
    print('Func_called - imported')
    
'''
This code maybe confused because of "-fullscreen".
But that's no problem.
This code is just practice
'''

