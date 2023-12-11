import time
import os
import math
import traceback 
import tkinter as tk


## Functions ##
def relayOn(relay):
    if relay == 1:
        os.system('./Desktop/relay'+str(relay)+'On.sh')
        STATUS_relay.itemconfig(STATUS_relay_rect, fill="green")
    elif relay == 2:
        os.system('./Desktop/relay'+str(relay)+'On.sh')
        STATUS_relay2.itemconfig(STATUS_relay2_rect, fill="green")
    elif relay == 3:
        os.system('./Desktop/relay'+str(relay)+'On.sh')
        STATUS_relay3.itemconfig(STATUS_relay3_rect, fill="green")
    elif relay == 4:
        os.system('./Desktop/relay'+str(relay)+'On.sh')
        STATUS_relay4.itemconfig(STATUS_relay4_rect, fill="green")

def relayOff(relay):         
    if relay == 1:
        os.system('./Desktop/relay'+str(relay)+'Off.sh')
        STATUS_relay.itemconfig(STATUS_relay_rect, fill="red")
    elif relay == 2:
        os.system('./Desktop/relay'+str(relay)+'Off.sh')
        STATUS_relay2.itemconfig(STATUS_relay2_rect, fill="red")
    elif relay == 3:
        os.system('./Desktop/relay'+str(relay)+'Off.sh')
        STATUS_relay3.itemconfig(STATUS_relay3_rect, fill="red")
    elif relay == 4:
        os.system('./Desktop/relay'+str(relay)+'Off.sh')
        STATUS_relay4.itemconfig(STATUS_relay4_rect, fill="red")

def relayAllOff():
     relayOff(1)
     relayOff(2)
     relayOff(3)
     relayOff(4)

def relayAllOn():
     relayOn(1)
     relayOn(2)
     relayOn(3)
     relayOn(4)

def relayTest():
    relayAllOff()

    time.sleep(1)
    relayOn(1)
    time.sleep(1)
    relayOn(2)
    time.sleep(1)
    relayOn(3)
    time.sleep(1)
    relayOn(4)
    time.sleep(1)

    relayAllOff()
    time.sleep(1)

    relayAllOn()
    time.sleep(1)

    relayAllOff()
    time.sleep(1)

def setText(tb, text):
    tb.delete(0, tk.END)
    tb.insert(0,text)

def resetStartTime():
    global START_TIME
    global UPDATE_FILE

    START_TIME = time.time()

    UPDATE_FILE = True

def minusTimer():
    global TIMER_CYCLE
    global INCREMENT
    global UPDATE_FILE

    TIMER_CYCLE = str(max(int(TIMER_CYCLE) - int(INCREMENT),0))

    UPDATE_FILE = True

def plusTimer():
    global TIMER_CYCLE
    global INCREMENT
    global UPDATE_FILE

    TIMER_CYCLE = str(int(TIMER_CYCLE) + int(INCREMENT))

    UPDATE_FILE = True

def minusIncrement():
    global INCREMENT
    global UPDATE_FILE

    INCREMENT = str(max(int(INCREMENT) - 1,1))

    UPDATE_FILE = True

def plusIncrement():
    global INCREMENT
    global UPDATE_FILE

    INCREMENT = str(int(INCREMENT) + 1)

    UPDATE_FILE = True


def minus(relay, is_on):
    global RELAY1_ON
    global RELAY2_ON
    global RELAY3_ON
    global RELAY4_ON

    global RELAY1_OFF
    global RELAY2_OFF
    global RELAY3_OFF
    global RELAY4_OFF

    global UPDATE_FILE

    global INCREMENT

    if relay == 1:
        if is_on:
            RELAY1_ON = str(max(int(RELAY1_ON) - int(INCREMENT),0))
        else:
            RELAY1_OFF = str(max(int(RELAY1_OFF) - int(INCREMENT),0))
    elif relay == 2:
        if is_on:
            RELAY2_ON = str(max(int(RELAY2_ON) - int(INCREMENT),0))
        else:
            RELAY2_OFF = str(max(int(RELAY2_OFF) - int(INCREMENT),0))
    elif relay == 3:
        if is_on:
            RELAY3_ON = str(max(int(RELAY3_ON) - int(INCREMENT),0))
        else:
            RELAY3_OFF = str(max(int(RELAY3_OFF) - int(INCREMENT),0))
    elif relay == 4:
        if is_on:
            RELAY4_ON = str(max(int(RELAY4_ON) - int(INCREMENT),0))
        else:
            RELAY4_OFF = str(max(int(RELAY4_OFF) - int(INCREMENT),0))

    UPDATE_FILE = True

def plus(relay, is_on):
    global RELAY1_ON
    global RELAY2_ON
    global RELAY3_ON
    global RELAY4_ON

    global RELAY1_OFF
    global RELAY2_OFF
    global RELAY3_OFF
    global RELAY4_OFF

    global UPDATE_FILE

    global INCREMENT

    if relay == 1:
        if is_on:
            RELAY1_ON = str(min(int(RELAY1_ON) + int(INCREMENT),int(TIMER_CYCLE)))
        else:
            RELAY1_OFF = str(min(int(RELAY1_OFF) + int(INCREMENT),int(TIMER_CYCLE)))
    elif relay == 2:
        if is_on:
            RELAY2_ON = str(min(int(RELAY2_ON) + int(INCREMENT),int(TIMER_CYCLE)))
        else:
            RELAY2_OFF = str(min(int(RELAY2_OFF) + int(INCREMENT),int(TIMER_CYCLE)))
    elif relay == 3:
        if is_on:
            RELAY3_ON = str(min(int(RELAY3_ON) + int(INCREMENT),int(TIMER_CYCLE)))
        else:
            RELAY3_OFF = str(min(int(RELAY3_OFF) + int(INCREMENT),int(TIMER_CYCLE)))
    elif relay == 4:
        if is_on:
            RELAY4_ON = str(min(int(RELAY4_ON) + int(INCREMENT),int(TIMER_CYCLE)))
        else:
            RELAY4_OFF = str(min(int(RELAY4_OFF) + int(INCREMENT),int(TIMER_CYCLE)))

    UPDATE_FILE = True

def refreshUI():
    try:
        global START_TIME
        global CURRENT_TIME
        global UPDATE_FILE
        global INCREMENT

        setText(tb_timer, TIMER_CYCLE)
        setText(tb_increment, INCREMENT)

        if CURRENT_TIME != str(int(math.floor(time.time()-START_TIME)/60)) :
            UPDATE_FILE = True
        CURRENT_TIME = str(int(math.floor(time.time()-START_TIME)/60))
        # If we're over timer cycle, restart
        if int(CURRENT_TIME) > int(TIMER_CYCLE):
            resetStartTime()
            CURRENT_TIME = str(int(math.floor(time.time()-START_TIME)/60))
            UPDATE_FILE = True
        setText(tb_current_time, CURRENT_TIME)

        setText(tb_relay1On, RELAY1_ON)
        setText(tb_relay2On, RELAY2_ON)
        setText(tb_relay3On, RELAY3_ON)
        setText(tb_relay4On, RELAY4_ON)

        setText(tb_relay1Off, RELAY1_OFF)
        setText(tb_relay2Off, RELAY2_OFF)
        setText(tb_relay3Off, RELAY3_OFF)
        setText(tb_relay4Off, RELAY4_OFF)

        #RELAY1
        if int(CURRENT_TIME) >= int(RELAY1_ON) and int(CURRENT_TIME) < int(RELAY1_OFF):
            relayOn(1)
        else:
            relayOff(1)
        #RELAY2
        if int(CURRENT_TIME) >= int(RELAY2_ON) and int(CURRENT_TIME) < int(RELAY2_OFF):
            relayOn(2)
        else:
            relayOff(2)
        #RELAY3
        if int(CURRENT_TIME) >= int(RELAY3_ON) and int(CURRENT_TIME) < int(RELAY3_OFF):
            relayOn(3)
        else:
            relayOff(3)
        #RELAY4
        if int(CURRENT_TIME) >= int(RELAY4_ON) and int(CURRENT_TIME) < int(RELAY4_OFF):
            relayOn(4)
        else:
            relayOff(4)

        if UPDATE_FILE:
            saveState()
            UPDATE_FILE = False
    except:
        traceback.print_exc() 

    tb_timer.after(100, refreshUI)                                 ##-Attend 0.1 sec

def saveState():
    global TIMER_CYCLE
    global CURRENT_TIME

    global RELAY1_ON
    global RELAY2_ON
    global RELAY3_ON
    global RELAY4_ON

    global RELAY1_OFF
    global RELAY2_OFF
    global RELAY3_OFF
    global RELAY4_OFF

    global INCREMENT

    #Only save if something changed


    os.system("> /home/pi/Desktop/save.txt")
    with open("/home/pi/Desktop/save.txt", 'a') as file:
        file.write(TIMER_CYCLE + "\n" +
                   CURRENT_TIME + "\n" +
                   
                   RELAY1_ON + "\n" +
                   RELAY2_ON + "\n" +
                   RELAY3_ON + "\n" +
                   RELAY4_ON + "\n" +
                   
                   RELAY1_OFF + "\n" +
                   RELAY2_OFF + "\n" +
                   RELAY3_OFF + "\n" +
                   RELAY4_OFF + "\n" +

                   INCREMENT  + "\n"
                   )

def loadState():
    global START_TIME
    global TIMER_CYCLE
    global CURRENT_TIME

    global RELAY1_ON
    global RELAY2_ON
    global RELAY3_ON
    global RELAY4_ON

    global RELAY1_OFF
    global RELAY2_OFF
    global RELAY3_OFF
    global RELAY4_OFF

    global INCREMENT

    try:
        with open("/home/pi/Desktop/save.txt") as file:
            TIMER_CYCLE = file.readline().split("\n")[0]
            CURRENT_TIME = file.readline().split("\n")[0]

            RELAY1_ON = file.readline().split("\n")[0]
            RELAY2_ON = file.readline().split("\n")[0]
            RELAY3_ON = file.readline().split("\n")[0]
            RELAY4_ON = file.readline().split("\n")[0]

            RELAY1_OFF = file.readline().split("\n")[0]
            RELAY2_OFF = file.readline().split("\n")[0]
            RELAY3_OFF = file.readline().split("\n")[0]
            RELAY4_OFF = file.readline().split("\n")[0]

            INCREMENT = file.readline().split("\n")[0]
    except:
        pass

    if TIMER_CYCLE == "":
        TIMER_CYCLE = DEFAULT_TIMER_CYCLE
    if CURRENT_TIME == "":
        CURRENT_TIME = DEFAULT_CURRENT_TIME
    
    if RELAY1_ON == "":
        RELAY1_ON   = DEFAULT_RELAY1_ON
    if RELAY2_ON == "":
        RELAY2_ON   = DEFAULT_RELAY2_ON
    if RELAY3_ON == "":
        RELAY3_ON   = DEFAULT_RELAY3_ON
    if RELAY4_ON == "":
        RELAY4_ON   = DEFAULT_RELAY4_ON

    if RELAY1_OFF == "":
        RELAY1_OFF  = DEFAULT_RELAY1_OFF
    if RELAY2_OFF == "":
        RELAY2_OFF  = DEFAULT_RELAY2_OFF
    if RELAY3_OFF == "":
        RELAY3_OFF  = DEFAULT_RELAY3_OFF
    if RELAY4_OFF == "":
        RELAY4_OFF  = DEFAULT_RELAY4_OFF
    if INCREMENT == "":
        INCREMENT = DEFAULT_INCREMENT

    START_TIME = time.time() - (60 * int(CURRENT_TIME))   
    
##Global variables
string_font_family                = "Helvetica"
int_font_size                     = 15
int_last_time                     = ""
UPDATE_FILE                       = False

#Default values
DEFAULT_TIMER_CYCLE = "25"
DEFAULT_CURRENT_TIME = "0"

DEFAULT_RELAY1_ON   = "0"
DEFAULT_RELAY2_ON   = "5"
DEFAULT_RELAY3_ON   = "10"
DEFAULT_RELAY4_ON   = "15"

DEFAULT_RELAY1_OFF  = "5"
DEFAULT_RELAY2_OFF  = "10"
DEFAULT_RELAY3_OFF  = "15"
DEFAULT_RELAY4_OFF  = "20"

DEFAULT_INCREMENT = "5"

TIMER_CYCLE = DEFAULT_TIMER_CYCLE
CURRENT_TIME = DEFAULT_CURRENT_TIME

RELAY1_ON   = DEFAULT_RELAY1_ON
RELAY2_ON   = DEFAULT_RELAY2_ON
RELAY3_ON   = DEFAULT_RELAY3_ON
RELAY4_ON   = DEFAULT_RELAY4_ON

RELAY1_OFF  = DEFAULT_RELAY1_OFF
RELAY2_OFF  = DEFAULT_RELAY2_OFF
RELAY3_OFF  = DEFAULT_RELAY3_OFF
RELAY4_OFF  = DEFAULT_RELAY4_OFF

INCREMENT = DEFAULT_INCREMENT

#turn off wifi so the time dosent change on boot
os.system('rfkill block wifi') 

#Serial Port : 9600 baud | Char Size : 8
os.system('stty -F /dev/ttyUSB0 speed 9600 cs8') 
time.sleep(1)

# Window
master = tk.Tk()
master.attributes("-fullscreen", True)

#ROW 1
lb_timer = tk.Label(master, text = "TIMER", font=(string_font_family, int_font_size))
lb_timer.grid(row = 1, column = 1, sticky = tk.W, padx = 2, pady = 10)

tb_timer = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_timer.grid(row = 1, column = 3, padx = 2, pady= 10)

b_timer_minus = tk.Button(text = "-", font=(string_font_family, int_font_size),command=lambda: minusTimer())
b_timer_minus.grid(row = 1, column = 4, padx = 2, pady = 10)
b_timer_plus = tk.Button(text = "+", font=(string_font_family, int_font_size),command=lambda: plusTimer())
b_timer_plus.grid(row = 1, column = 5, padx = 2, pady = 10)

tb_current_time = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_current_time.grid(row = 1, column = 7, padx = 2, pady = 10)
b_current_reset = tk.Button(text = "RESET", font=(string_font_family, int_font_size), width = 5, command=lambda: resetStartTime())
b_current_reset.grid(row = 1, column = 8, columnspan = 3, padx = 2, pady = 10)

#ROW 2 - EMPTY
lb_empty = tk.Label(master, text="", font=(string_font_family, int_font_size))
lb_empty.grid(row = 2, column = 1, columnspan=9, sticky = tk.W, padx = 2, pady = 10)
#INCREMENT
lb_increment = tk.Label(master, text = "INC.", font=(string_font_family, int_font_size))
lb_increment.grid(row = 2, column = 6, sticky = tk.W, padx = 2, pady = 2)
tb_increment = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_increment.grid(row = 2, column = 7, padx = 2, pady= 10)
b_increment_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minusIncrement())
b_increment_minus.grid(row = 2, column = 8, padx = 2, pady = 2)
b_increment_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plusIncrement())
b_increment_plus.grid(row = 2, column = 9, padx = 2, pady = 2)

#ROW 3
STATUS_relay = tk.Canvas(master,width=50,height=25)
master.update()
STATUS_relay.grid(row = 3, column = 1)
STATUS_relay_rect = STATUS_relay.create_rectangle(0,0,50,25,fill="red")
#ON
lb_relay1On = tk.Label(master, text = "(1) ON", font=(string_font_family, int_font_size))
lb_relay1On.grid(row = 3, column = 2, sticky = tk.W, padx = 2, pady = 2)
tb_relay1On = tk.Entry(master, font=(string_font_family,int_font_size), width = 5, justify="center")
tb_relay1On.grid(row = 3, column = 3, padx = 2, pady = 10)
b_relay1On_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(1,True))
b_relay1On_minus.grid(row = 3, column = 4, padx = 2, pady = 2)
b_relay1On_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(1,True))
b_relay1On_plus.grid(row = 3, column = 5, padx = 2, pady = 2)
#OFF
lb_relay1Off = tk.Label(master, text = "OFF", font=(string_font_family, int_font_size))
lb_relay1Off.grid(row = 3, column = 6, sticky = tk.W, padx = 2, pady = 2)
tb_relay1Off = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_relay1Off.grid(row = 3, column = 7, padx = 2, pady= 10)
b_relay1Off_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(1,False))
b_relay1Off_minus.grid(row = 3, column = 8, padx = 2, pady = 2)
b_relay1Off_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(1,False))
b_relay1Off_plus.grid(row = 3, column = 9, padx = 2, pady = 2)

#ROW 4 - EMPTY
lb_timer = tk.Label(master, text = "", font=(string_font_family, 2))
lb_timer.grid(row = 4, column = 1, sticky = tk.W, padx = 2, pady = 2)

#ROW 5
STATUS_relay2 = tk.Canvas(master,width=50,height=25)
master.update()
STATUS_relay2.grid(row = 5, column = 1)
STATUS_relay2_rect = STATUS_relay2.create_rectangle(0,0,50,25,fill="red")
#ON
lb_relay2On = tk.Label(master, text = "(2) ON", font=(string_font_family, int_font_size))
lb_relay2On.grid(row = 5, column = 2, sticky = tk.W, padx = 2, pady = 2)
tb_relay2On = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_relay2On.grid(row = 5, column = 3, padx = 2, pady= 10)
b_relay2On_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(2,True))
b_relay2On_minus.grid(row = 5, column = 4, padx = 2, pady = 2)
b_relay2On_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(2,True))
b_relay2On_plus.grid(row = 5, column = 5, padx = 2, pady = 2)
#OFF
lb_relay2Off = tk.Label(master, text = "OFF", font=(string_font_family, int_font_size))
lb_relay2Off.grid(row = 5, column = 6, sticky = tk.W, padx = 2, pady = 2)
tb_relay2Off = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_relay2Off.grid(row = 5, column = 7, padx = 2, pady= 10)
b_relay2Off_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(2,False))
b_relay2Off_minus.grid(row = 5, column = 8, padx = 2, pady = 2)
b_relay2Off_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(2,False))
b_relay2Off_plus.grid(row = 5, column = 9, padx = 2, pady = 2)

#ROW 6 - EMPTY
lb_timer = tk.Label(master, text = "", font=(string_font_family, 2))
lb_timer.grid(row = 6, column = 1, sticky = tk.W, padx = 2, pady = 2)

#ROW 7
STATUS_relay3 = tk.Canvas(master,width=50,height=25)
master.update()
STATUS_relay3.grid(row = 7, column = 1)
STATUS_relay3_rect = STATUS_relay3.create_rectangle(0,0,50,25,fill="red")
#ON
lb_relay3On = tk.Label(master, text = "(3) ON", font=(string_font_family, int_font_size))
lb_relay3On.grid(row = 7, column = 2, sticky = tk.W, padx = 2, pady = 2)
tb_relay3On = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_relay3On.grid(row = 7, column = 3, padx = 2, pady= 10)
b_relay3On_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(3,True))
b_relay3On_minus.grid(row = 7, column = 4, padx = 2, pady = 2)
b_relay3On_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(3,True))
b_relay3On_plus.grid(row = 7, column = 5, padx = 2, pady = 2)
#OFF
lb_relay3Off = tk.Label(master, text = "OFF", font=(string_font_family, int_font_size))
lb_relay3Off.grid(row = 7, column = 6, sticky = tk.W, padx = 2, pady = 2)
tb_relay3Off = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_relay3Off.grid(row = 7, column = 7, padx = 2, pady= 10)
b_relay3Off_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(3,False))
b_relay3Off_minus.grid(row = 7, column = 8, padx = 2, pady = 2)
b_relay3Off_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(3,False))
b_relay3Off_plus.grid(row = 7, column = 9, padx = 2, pady = 2)

#ROW 8 - EMPTY
lb_timer = tk.Label(master, text = "", font=(string_font_family, 2))
lb_timer.grid(row = 8, column = 1, sticky = tk.W, padx = 2, pady = 2)

#ROW 9
STATUS_relay4 = tk.Canvas(master,width=50,height=25)
master.update()
STATUS_relay4.grid(row = 9, column = 1)
STATUS_relay4_rect = STATUS_relay4.create_rectangle(0,0,50,25,fill="red")
#ON
lb_relay4On = tk.Label(master, text = "(4) ON", font=(string_font_family, int_font_size))
lb_relay4On.grid(row = 9, column = 2, sticky = tk.W, padx = 2, pady = 2)
tb_relay4On = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_relay4On.grid(row = 9, column = 3, padx = 2, pady= 10)
b_relay4On_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(4,True))
b_relay4On_minus.grid(row = 9, column = 4, padx = 2, pady = 2)
b_relay4On_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(4,True))
b_relay4On_plus.grid(row = 9, column = 5, padx = 2, pady = 2)
#OFF
lb_relay4Off = tk.Label(master, text = "OFF", font=(string_font_family, int_font_size))
lb_relay4Off.grid(row = 9, column = 6, sticky = tk.W, padx = 2, pady = 2)
tb_relay4Off = tk.Entry(master, font=(string_font_family, int_font_size), width = 5, justify="center")
tb_relay4Off.grid(row = 9, column = 7, padx = 2, pady= 10)
b_relay4Off_minus = tk.Button(text = "-", font=(string_font_family, int_font_size), command=lambda: minus(4,False))
b_relay4Off_minus.grid(row = 9, column = 8, padx = 2, pady = 2)
b_relay4Off_plus = tk.Button(text = "+", font=(string_font_family, int_font_size), command=lambda: plus(4,False))
b_relay4Off_plus.grid(row = 9, column = 9, padx = 2, pady = 2)

loadState()

refreshUI()

master.config(cursor="none")

# infinite loop which can be terminated by keyboard
# or mouse interrupt
tk.mainloop()
