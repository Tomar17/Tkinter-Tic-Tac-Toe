from tkinter import *
window=Tk()
window.title("TTT")
window.geometry('130x120')
window.resizable(False,False)
turn='o'
x_playspots=[]
o_playspots=[]
x_score=0
o_score=0



def pos(name):
    x_playspot=[]
    o_playspot=[]
    if turn=='x':
        if name=='b1':
            x_playspot.append(btn1.grid_info()['row'])
            x_playspot.append(btn1.grid_info()['column'])
        if name=='b2':
            x_playspot.append(btn2.grid_info()['row'])
            x_playspot.append(btn2.grid_info()['column'])
        if name=='b3':
            x_playspot.append(btn3.grid_info()['row'])
            x_playspot.append(btn3.grid_info()['column'])
        if name=='b4':
            x_playspot.append(btn4.grid_info()['row'])
            x_playspot.append(btn4.grid_info()['column'])
        if name=='b5':
            x_playspot.append(btn5.grid_info()['row'])
            x_playspot.append(btn5.grid_info()['column'])
        if name=='b6':
            x_playspot.append(btn6.grid_info()['row'])
            x_playspot.append(btn6.grid_info()['column'])
        if name=='b7':
            x_playspot.append(btn7.grid_info()['row'])
            x_playspot.append(btn7.grid_info()['column'])
        if name=='b8':
            x_playspot.append(btn8.grid_info()['row'])
            x_playspot.append(btn8.grid_info()['column'])
        if name=='b9':
            x_playspot.append(btn9.grid_info()['row'])
            x_playspot.append(btn9.grid_info()['column'])
        x_playspots.append(x_playspot)




    else:
        if name=='b1':
            o_playspot.append(btn1.grid_info()['row'])
            o_playspot.append(btn1.grid_info()['column'])
        if name=='b2':
            o_playspot.append(btn2.grid_info()['row'])
            o_playspot.append(btn2.grid_info()['column'])
        if name=='b3':
            o_playspot.append(btn3.grid_info()['row'])
            o_playspot.append(btn3.grid_info()['column'])
        if name=='b4':
            o_playspot.append(btn4.grid_info()['row'])
            o_playspot.append(btn4.grid_info()['column'])
        if name=='b5':
            o_playspot.append(btn5.grid_info()['row'])
            o_playspot.append(btn5.grid_info()['column'])
        if name=='b6':
            o_playspot.append(btn6.grid_info()['row'])
            o_playspot.append(btn6.grid_info()['column'])
        if name=='b7':
            o_playspot.append(btn7.grid_info()['row'])
            o_playspot.append(btn7.grid_info()['column'])
        if name=='b8':
            o_playspot.append(btn8.grid_info()['row'])
            o_playspot.append(btn8.grid_info()['column'])
        if name=='b9':
            o_playspot.append(btn9.grid_info()['row'])
            o_playspot.append(btn9.grid_info()['column'])
        o_playspots.append(o_playspot)

def check_win():
    global x_score
    global o_score
    global x_playspots
    global o_playspots
    count_hor_0 = 0
    count_hor_1 = 0
    count_hor_2 = 0
    count_ver_0 = 0
    count_ver_1 = 0
    count_ver_2 = 0
    count_slant_r = 0
    count_slant_l = 0

    if turn == 'x':
        for i in x_playspots:
            if i[0] == 0:
                count_hor_0 += 1
            elif i[0] == 1:
                count_hor_1 += 1
            elif i[0] == 2:
                count_hor_2 += 1

            if i[1] == 0:
                count_ver_0 += 1
            elif i[1] == 1:
                count_ver_1 += 1
            elif i[1] == 2:
                count_ver_2 += 1

            if i[0] == i[1]:
                count_slant_r += 1

            if i[0] + i[1] == 2:
                count_slant_l += 1

    else:
        for i in o_playspots:
            if i[0] == 0:
                count_hor_0 += 1
            elif i[0] == 1:
                count_hor_1 += 1
            elif i[0] == 2:
                count_hor_2 += 1

            if i[1] == 0:
                count_ver_0 += 1
            elif i[1] == 1:
                count_ver_1 += 1
            elif i[1] == 2:
                count_ver_2 += 1

            if i[0] == i[1]:
                count_slant_r += 1
            if i[0] + i[1] == 2:
                count_slant_l += 1

    win = [count_ver_2, count_ver_1, count_ver_0, count_hor_2, count_hor_1, count_hor_0, count_slant_l, count_slant_r]

    for i in win:
        if i == 3:
            if turn == 'x':
                print('x wins')
                x_score+=1
                score_label.config(text=f"(X:{x_score}) ({o_score}:O)")
                btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
                for i in btns:
                    i.config(text='',state=ACTIVE)
                x_playspots=[]
                o_playspots = []


            else:
                print("o wins")
                o_score+=1
                score_label.config(text=f"(X:{x_score}) ({o_score}:O)")
                btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
                for i in btns:
                    i.config(text='',state=ACTIVE)
                o_playspots=[]
                x_playspots = []


            for i in win:
                i=0
            return True



def click(name):
    global turn
    if turn=='x':
        turn='o'
    else:
        turn='x'
    if turn=='x':
        if name=='b1':
            btn1.config(text='X',state=DISABLED,disabledforeground='black',)
        if name=='b2':
            btn2.config(text='X',state=DISABLED,disabledforeground='black')
        if name=='b3':
            btn3.config(text='X',state=DISABLED,disabledforeground='black')
        if name=='b4':
            btn4.config(text='X',state=DISABLED,disabledforeground='black')
        if name=='b5':
            btn5.config(text='X',state=DISABLED,disabledforeground='black')
        if name=='b6':
            btn6.config(text='X',state=DISABLED,disabledforeground='black')
        if name=='b7':
            btn7.config(text='X',state=DISABLED,disabledforeground='black')
        if name=='b8':
            btn8.config(text='X',state=DISABLED,disabledforeground='black')
        if name=='b9':
            btn9.config(text='X',state=DISABLED,disabledforeground='black')


    else:
        if name=='b1':
            btn1.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b2':
            btn2.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b3':
            btn3.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b4':
            btn4.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b5':
            btn5.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b6':
            btn6.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b7':
            btn7.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b8':
            btn8.config(text='0',state=DISABLED,disabledforeground='black')
        if name=='b9':
            btn9.config(text='0',state=DISABLED,disabledforeground='black')

    if turn == 'x':
        turn_label.config(text="(0)")

    else:
        turn_label.config(text="(X)")


#TODO:dk


if turn=='x':
    turn_label=Label(window,text="(O)")
else:
    turn_label = Label(window, text="(X)")
turn_label.grid(column=0,row=4)

score_label=Label(window,text=f"(X:{x_score}) ({o_score}:O)")
score_label.grid(column=1,row=4,columnspan=2)


btn1=Button(window, text='', command=lambda:[click('b1'),pos('b1'),check_win()])
btn1.grid(column=0,row=0)


btn2=Button(window, text='', command=lambda:[click('b2'),pos('b2'),check_win()])
btn2.grid(column=0,row=1)

btn3=Button(window,text='',command=lambda:[click('b3'),pos('b3'),check_win()])
btn3.grid(column=0,row=2)

btn4=Button(window,text='',command=lambda:[click('b4'),pos('b4'),check_win()])
btn4.grid(column=1,row=0)

btn5=Button(window,text='',command=lambda:[click('b5'),pos('b5'),check_win()])
btn5.grid(column=1,row=1)

btn6=Button(window,text='',command=lambda:[click('b6'),pos('b6'),check_win()])
btn6.grid(column=1,row=2)

btn7=Button(window,text='',command=lambda:[click('b7'),pos('b7'),check_win()])
btn7.grid(column=2,row=0)

btn8=Button(window,text='',command=lambda:[click('b8'),pos('b8'),check_win()])
btn8.grid(column=2,row=1)

btn9=Button(window,text='',command=lambda:[click('b9'),pos('b9'),check_win()])
btn9.grid(column=2,row=2)




window.mainloop()