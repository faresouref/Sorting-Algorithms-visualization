from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
import tkinter.font as font
from tkinter import messagebox
import time

def exit_application():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?', icon='warning')
    if msg_box == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1400, 800)
root.geometry("1370x800")
root.config(bg='#0054FB')
root.protocol('WM_DELETE_WINDOW', exit_application)

#variables
selected_alg = StringVar()
data = []

#function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 580
    c_width = 1330
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 5
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i]) #rectangles
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()


def Generate():
    global data

    spendTime.configure(state='normal')
    spendTime.delete(0, END)

    # minVal = int(minEntry.get())
    # maxVal = int(maxEntry.get())
    # size = int(sizeEntry.get())
    print('Alg Selected: ' + selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 10
    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    if minVal < 0 : minVal = 0
    if maxVal > 100 : maxVal = 100
    if size > 100 : size = 100

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['#001AFA' for x in range(len(data))]) #['blue', '#001AFA' ,....]


def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        start_time = time.time()
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        end_time = time.time()
        spendTime.insert(0, round(end_time - start_time, 2))
        spendTime.configure(state='readonly')
    elif algMenu.get() == 'Bubble Sort':
        start_time = time.time()
        bubble_sort(data, drawData, speedScale.get())
        end_time = time.time()
        spendTime.insert(0, round(end_time - start_time, 2))
        spendTime.configure(state='readonly')
    elif algMenu.get() == 'Merge Sort':
        start_time = time.time()
        merge_sort(data, drawData, speedScale.get())
        end_time = time.time()
        spendTime.insert(0, round(end_time - start_time, 2))
        spendTime.configure(state='readonly')
    
    drawData(data, ['#7EA2E9' for x in range(len(data))]) #['babyblue', '#7EA2E9' ,....]

#frame / base lauout
UI_frame = Frame(root, width= 1330, height=580, bg='#7EA2E9') #big box
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=1330, height=580, bg='#DCE1E9') #small box
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]

Label(UI_frame, text="Size ", bg='#7EA2E9').grid(row=0, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
sizeEntry.insert(0,10)

Label(UI_frame, text="Min Value ", bg='#7EA2E9').grid(row=0, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
minEntry.insert(0, 1)

Label(UI_frame, text="Max Value ", bg='#7EA2E9').grid(row=0, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=0, column=5, padx=5, pady=5, sticky=W)
maxEntry.insert(0, 10)

myFont = font.Font(family='Helvetica')
Button(UI_frame, text="Generate", command=Generate, bg='#001AFA', fg='white', font=myFont, activebackground='#CCD0F3').grid(row=0, column=6, padx=5, pady=5, sticky=W)

#Row[1]
Label(UI_frame, text="Algorithm: ", bg='#7EA2E9').grid(row=1, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=1, column=1, padx=5, pady=5, sticky=W)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.01, to=1.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Sort", command=StartAlgorithm, bg='#001AFA', fg='white', font=myFont, activebackground='#CCD0F3').grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text='Time spend : ', bg='#7EA2E9').grid(row=1, column=4, padx=5, pady=5, sticky=W)
spendTime = Entry(UI_frame)
spendTime.grid(row=1, column=5, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Seconds", bg='#7EA2E9').grid(row=1, column=6, padx=5, pady=5, sticky=W)

root.mainloop()



