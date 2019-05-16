# -*- coding: utf-8 -*-
import tkinter
little_array = ['`','1','2','3','4','5','6','7','8','9','0','-','=',
                'q','w','e','r','t','y','u','i','o','p','[' ,']',
                'a','s','d','f','g','h','j','k','l',';',
                'z','x','c','v','b','n','m',',','.','/','Space','Shift','Erase']
big_array = ['~','!','@','#','$','%','^','&','*','(',')','_','+',
             'Q','W','E','R','T','Y','U','I','O','P','{','}',
             'A','S','D','F','G','H','J','K','L',':',
             'Z','X','C','V','B','N','M','<','>','?','Space','Shift','Erase']



def Mapping(i):
    global target, Shift_flag
    if(i == 46):
        if(Shift_flag == 0):
            Shift_flag = 1
        else:
            Shift_flag = 0
    elif(i == 47):
        target.delete(len(target.get())-1,tkinter.END)
        Shift_flag = 0
    elif(i == 45):
        target.insert(tkinter.END," ")
        Shift_flag = 0
    else:
        if(Shift_flag == 0):
            target.insert(tkinter.END,little_array[i])
        if(Shift_flag == 1):
            target.insert(tkinter.END,big_array[i])
            Shift_flag = 0
    '''
    If you click "Shift" and then "Space" or "Erase",
    The count variable for "Shift"(that is Shift_flag) is set to 0, and "Space" and "Erase" respond normally.
    '''
            
def Make_button(Frame):
    temp_row = 0
    temp_col = 0
    for i in range(0,48):
        key_func = lambda x = i : Mapping(x)
        #Use lambda to mapping each button
        if(little_array[i] == 'q' or little_array[i] == 'a' or little_array[i] == 'z'):
            temp_row +=1
            if(temp_row >= 2):
                temp_col = 1
            else:
                temp_col = 0
        if(little_array[i] == 'Space'):
            tkinter.Button(Frame,text = 'Space', overrelief="solid",command = key_func, width=5,repeatdelay=500, repeatinterval=100).grid(row=2,column = 11)
        elif(little_array[i] == 'Shift'):
            tkinter.Button(Frame,text = 'Shift', overrelief="solid",command = key_func, width=5,repeatdelay=500, repeatinterval=100).grid(row=3,column = 11)
        elif(little_array[i] == 'Erase'):
            tkinter.Button(Frame,text = 'Erase', overrelief="solid",command = key_func, width=5,repeatdelay=500, repeatinterval=100).grid(row=1,column = 12)
        else:
            tkinter.Button(Frame,text = little_array[i] + '( '+ big_array[i] +' )', overrelief="solid",command = key_func, width=5,repeatdelay=500, repeatinterval=100).grid(row=temp_row,column = temp_col)
            temp_col += 1
        '''
        Create a button without declaring a variable and connect "key_func" to that button.
        This makes it a more nice code.
        At least that's what I think.
        '''
    
if __name__ == '__main__':
    Shift_flag = 0
    #"Shift" val
    window=tkinter.Tk()
    window.title("Sungmin_Joo")
    window.resizable(False, False)
    
    target = tkinter.Entry(window,width=83)
    target.grid(row=1)
    
    frame2=tkinter.Frame(window)
    Make_button(frame2)
    frame2.grid(row=2)
    
    window.mainloop()
else:
    print('Func_called - imported') 

