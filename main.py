import tkinter as ttk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#910A67"
RED = "#820300"
GREEN = "#294B29"
YELLOW = "#f7f5dd"
PURPLE = "#280274"
BLUE = "#5FBDFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
SECOND = 60
REPS = 0
LEVEL = 0
TOTAL_WORKING = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time ():
    global REPS
    global LEVEL
    global TOTAL_WORKING
    REPS = 0
    LEVEL = 0
    TOTAL_WORKING = 0
    window.after_cancel(TIMER)
    canvas.itemconfig(time_text,text="00:00")
    check_label.config(text="")
    timer_label.config(text='TIMER',fg=BLUE)
    worked_TIME.config(text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global REPS
    global LEVEL
    global TOTAL_WORKING
    REPS += 1
    
    
    if  REPS % 8 == 0:
        window.deiconify()
        LEVEL += 1
        check_label.config(text=f"{LEVEL * '✔'}")
        TOTAL_WORKING += WORK_MIN
        min = math.floor(TOTAL_WORKING /SECOND)
        sec = TOTAL_WORKING % SECOND
        if min < 10:
            min = f"0{min}"
        if sec < 10:
            sec = f"0{sec}"
        worked_TIME.config(text=f"{min}:{sec}")
        count_time(LONG_BREAK_MIN * SECOND)
        timer_label.config(text='Break',fg=RED)
    elif REPS % 2 == 0:
        window.deiconify()
        LEVEL += 1
        check_label.config(text=f"{LEVEL * '✔'}")
        TOTAL_WORKING += WORK_MIN
        min = math.floor(TOTAL_WORKING /SECOND)
        sec = TOTAL_WORKING % SECOND
        if min < 10:
            min = f"0{min}"
        if sec < 10:
            sec = f"0{sec}"
        worked_TIME.config(text=f"{min}:{sec}")        
        count_time(SHORT_BREAK_MIN * SECOND)
        timer_label.config(text='Break',fg=PINK)
    else :
        if LEVEL == 4:
            LEVEL = 0
        check_label.config(text=f"{LEVEL * '✔'}")
        count_time(WORK_MIN * SECOND)
        timer_label.config(text='Work',fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_time(count):
    count_min = math.trunc(count / SECOND)
    count_sec = count % SECOND

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'

    if count >= 0:
        global TIMER
        canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
        TIMER = window.after(1000,count_time, count - 1)
    else :
        start_time()

# ---------------------------- UI SETUP ------------------------------- #
window = ttk.Tk()
window.config(padx=100,pady=50, bg=YELLOW)
canvas = ttk.Canvas(width=400,height=300,bg=YELLOW,highlightthickness=0)
tomato_image = ttk.PhotoImage(file='tomato.png')
canvas.create_image(200,130,image=tomato_image)
time_text = canvas.create_text(200,150,text='00:00',fill='white',font=(FONT_NAME,28,'bold'))
canvas.grid(column=1,row=3)

# Label 
worked = ttk.Label(text='WORKED FOR',font=(FONT_NAME,20,'bold'),bg=YELLOW,fg=GREEN)
worked.grid(column=3,row=0)

worked_TIME = ttk.Label(text='00:00',font=(FONT_NAME,20,'bold'),bg=YELLOW,fg=PURPLE)
worked_TIME.grid(column=3,row=1)

timer_label = ttk.Label(text='Timer',font=(FONT_NAME,38,'bold'),bg=YELLOW,fg=BLUE)
timer_label.grid(column=1,row=2)

check_label = ttk.Label(text='',font=(FONT_NAME,20,'bold'),bg=YELLOW,fg=GREEN)
check_label.grid(column=1,row=5)


# button
start = ttk.Button(text='Start',font=(FONT_NAME,10),highlightthickness=0,command=start_time)
start.grid(column=0,row=4)

reset = ttk.Button(text='Reset',font=(FONT_NAME,10),highlightthickness=0,command=reset_time)
reset.grid(column=2,row=4)



window.mainloop()