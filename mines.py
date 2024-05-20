from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import *

global end, difficulty
difficulty=2
end=False
mines=10

def win():
    allopened=1
    for i in buttons:
        if i.opened==0:
            allopened=0
    if allopened==1 and flags==mines:
        if messagebox.askyesno("You Won", "Do you want to start a new game?"):
            new_game()


def open(i):
    global end
    #print("Hello!")
    buttons[i].config(relief=SUNKEN)
    if(True):
        buttons[i].opened=1
        if flags[i]==0:
            if mines[i]==0:
                if numbers[i]==0:
                    img1_file=Image.open("blank_open.png").resize((buttons_size, buttons_size))
                    if i==0:
                        k=i
                        linesforward=1
                        linesback=1
                        kend=i+width+1
                    elif i==width-1:
                        k=i-1
                        linesforward=1
                        linesback=1
                        kend=i+width
                    elif i==width*height-width:
                        k=i-width
                        linesforward=0
                        linesback=1
                        kend=i+1
                    elif i==width*height-1:
                        k=i-width-1
                        linesforward=0
                        linesback=1
                        kend=i
                    elif i<width:
                        k=i-1
                        linesback=1
                        linesforward=1
                        kend=i+width+1
                    elif i%width==0:
                        k=i-width
                        linesback=2
                        linesforward=1
                        kend=i+width+1
                    elif i>width*height-width:
                        k=i-width-1
                        linesback=1
                        linesforward=0
                        kend=i+1
                    elif i%width==width-1:
                        k=i-width-1
                        linesback=2
                        linesforward=1
                        kend=i+width
                    else:
                        k=i-width-1
                        linesforward=1
                        linesback=2
                        kend=i+width+1
                    if k!=i and buttons[k].opened==0:
                        #print(k)
                        open(k)
                    while k!=kend:
                        if k>=i+(linesforward*width)-1:
                            k=k-(linesback*width)+1
                        else:
                            k=k+width
                        if k!=i and buttons[k].opened==0:
                            #print(k)
                            open(k)
                else:
                    img1_file=Image.open(str(numbers[i])+".png").resize((buttons_size, buttons_size))
                img1=ImageTk.PhotoImage(img1_file)
                buttons[i].image=img1
                buttons[i].config(image=img1)
                buttons[i].config(bg="light grey")



            else:
                for j in range(width*height):
                    if mines[j]==1:
                        img1_file=Image.open("mine.png").resize((buttons_size, buttons_size))
                        img1=ImageTk.PhotoImage(img1_file)
                        buttons[j].image=img1
                        buttons[j].config(image=img1)
                    elif flags[j]==1:
                        buttons[j].config(bg="red")
                img1_file=Image.open("mine1.png").resize((buttons_size, buttons_size))
                img1=ImageTk.PhotoImage(img1_file)
                buttons[i].image=img1
                buttons[i].config(image=img1)
                print("Game Over")
                end=1
                if messagebox.askyesno("You Lost", "Do you want to start a new game?"):
                    new_game()
    print(i)




def leftClick(event, i):
    global end
    #win=Toplevel(root, bg="white")
    #win.title("Newer Window")
    #win.minsize(width=500, height=250)
    if not(end) and buttons[i].opened==0:
        open(i)
    win()
        

def rightClick(event, i):
    global end
    if not(end):
        if flags[i]==0 and buttons[i].opened==0:
            buttons[i].opened=1
            print("Bye!")
            img1_file=Image.open("flag.png").resize((buttons_size, buttons_size))
            img1=ImageTk.PhotoImage(img1_file)
            buttons[i].image=img1
            buttons[i].config(image=img1)
            buttons[i].config(bg="light grey")
            flags[i]=1
        elif flags[i]==1:
            buttons[i].opened=1
            flags[i]=2
            #print(flags[i])
            #print(buttons[i].opened)
            img1_file=Image.open("question.png").resize((buttons_size, buttons_size))
            img1=ImageTk.PhotoImage(img1_file)
            buttons[i].image=img1
            buttons[i].config(image=img1)
            buttons[i].config(bg="light grey")
        elif flags[i]==2:
            buttons[i].opened=0
            flags[i]=0
            #print(flags[i])
            #print(buttons[i].opened)
            img1_file=Image.open("blank.png").resize((buttons_size, buttons_size))
            img1=ImageTk.PhotoImage(img1_file)
            buttons[i].image=img1
            buttons[i].config(image=img1)
            buttons[i].config(bg="light grey")
        buttons[i].config(relief=SUNKEN)
    win()

def Mines(mines_count):
    i=0
    while(i<mines_count):
        j=randint(0, (width*height)-1)
        if mines[j]==0:
            img2_file=Image.open("blank.png").resize((buttons_size, buttons_size))
            img2=ImageTk.PhotoImage(img2_file)
            buttons[j].image=img2
            buttons[j].config(image=img2)
            mines[j]=1
            i+=1
            if j==0:
                k=j
                linesforward=1
                linesback=1
                kend=j+width+1
            elif j==width-1:
                k=j-1
                linesforward=1
                linesback=1
                kend=j+width
            elif j==width*height-width:
                k=j-width
                linesforward=0
                linesback=1
                kend=j+1
            elif j==width*height-1:
                k=j-width-1
                linesforward=0
                linesback=1
                kend=j
            elif j<width:
                k=j-1
                linesback=1
                linesforward=1
                kend=j+width+1
            elif j%width==0:
                k=j-width
                linesback=2
                linesforward=1
                kend=j+width+1
            elif j>width*height-width:
                k=j-width-1
                linesback=1
                linesforward=0
                kend=j+1
            elif j%width==width-1:
                k=j-width-1
                linesback=2
                linesforward=1
                kend=j+width
            else:
                k=j-width-1
                linesforward=1
                linesback=2
                kend=j+width+1
            numbers[k]+=1
            while k!=kend:
                if k>=j+(linesforward*width)-1:
                    k=k-(linesback*width)+1
                else:
                    k=k+width
                if k!=j and mines[k]==0:
                    numbers[k]+=1
    print(i)


def start_game():
    global width, height, bx, by, mines, numbers, buttons, flags, end, buttons_size
    end=0
    width=difficulty*10
    height=difficulty*10
    by=0
    bx=0
    buttons=[]
    mines=[]
    numbers=[]
    flags=[]
    print("Start")
    for i in range(width*height):
        buttons_size=200
        img_file=Image.open("blank.png").resize((buttons_size, buttons_size))
        img=ImageTk.PhotoImage(img_file)
        buttons.append(Label(root, relief=RAISED, image=img, width=buttons_size, height=buttons_size))
        mines.append(0)
        numbers.append(0)
        flags.append(0)
        if((i)%width==0 and i!=0):
            by=by+1
            bx=0
        buttons[i].bind("<Button-1>", lambda event, i1=i: leftClick(event, i1))
        buttons[i].bind("<Button-3>", lambda event, i2=i: rightClick(event, i2))
        buttons[i].image=img
        buttons[i].place(x=bx*buttons_size+bx*int(buttons_size/10), y=by*buttons_size+by*int(buttons_size/10))
        buttons[i].opened=0
        bx=bx+1
    Mines(difficulty*10)

def new_game():
    for i in mines:
        i=0
    print(mines)
    for i in buttons:
        i.destroy()
    start_game()
            


root=Tk()

start_game()

#fra=Frame(root, width=500, height=250, bg="lightblue")
#fra.place(x=300, y=100)

#button=Button(root, width=50, height=25, bg="black", fg="green")
#button["text"]="Hello!"
#button.bind("<Button-1>", printing)
#button.bind("<Button-3>", printing1)
#button.place(x=50, y=70)

root.title("Mines")
rx=width*(buttons_size+int(buttons_size/10))
ry=height*(buttons_size+int(buttons_size/10))
root.geometry(str(rx)+'x'+str(ry))



#name=Entry(root, width=100)
#name.place(x=50, y=500)
#name.bind("#\n", printing)
#text=Text(root, width=50, bd=10, wrap=WORD, font="Arial 25")
#text.place(x=500, y=170)

#t=Label(root, text="Mines Game\nFind all mines", font="Arial 32")
#t.place(x=500, y=70)



#button.pack()
root.mainloop()
