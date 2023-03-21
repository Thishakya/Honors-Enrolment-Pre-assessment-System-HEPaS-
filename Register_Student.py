from struct import pack
from tkinter import *
from tkinter import ttk
import socket
import json

PORT = 5051
SERVER = "192.168.8.101"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

win = Tk()

entry_val1 =StringVar(value=0)
entry_val2 =StringVar(value=0)
entry_val3 =StringVar(value=0)#
entry_val4 =StringVar(value=0)
entry_val5 =StringVar(value=0)
entry_val6 =StringVar(value=0)#
entry_val7 =StringVar(value=0)
entry_val8 =StringVar(value=0)
entry_val9 =StringVar(value=0)#
entry_val10 =StringVar(value=0)
entry_val11 =StringVar(value=0)
entry_val12 =StringVar(value=0)#
entry_val13 =StringVar(value=0)
entry_val14 =StringVar(value=0)
entry_val15 =StringVar(value=0)#
entry_val16 =StringVar(value=0)
entry_val17 =StringVar(value=0)
entry_val18 =StringVar(value=0)#
entry_val19 =StringVar(value=0)
entry_val20 =StringVar(value=0)
entry_val21 =StringVar(value=0)#
entry_val22 =StringVar(value=0)
entry_val23 =StringVar(value=0)
entry_val24 =StringVar(value=0)#
entry_val25 =StringVar(value=0)
entry_val26 =StringVar(value=0)
entry_val27 =StringVar(value=0)#
entry_val28 =StringVar(value=0)
entry_val29 =StringVar(value=0)
entry_val30 =StringVar(value=0)#
entry_val31 =StringVar(value=0)
entry_val32 =StringVar(value=0)
entry_val33 =StringVar(value=0)#
entry_val34 =StringVar(value=0)
entry_val35 =StringVar(value=0)
entry_val36 =StringVar(value=0)#
entry_val37 =StringVar(value=0)
entry_val38 =StringVar(value=0)
entry_val39 =StringVar(value=0)#
entry_val40 =StringVar(value=0)
entry_val41 =StringVar(value=0)
entry_val42 =StringVar(value=0)#
entry_val43 =StringVar(value=0)
entry_val44 =StringVar(value=0)
entry_val45 =StringVar(value=0)#
entry_val46 =StringVar(value=0)
entry_val47 =StringVar(value=0)
entry_val48 =StringVar(value=0)#
entry_val49 =StringVar(value=0)
entry_val50 =StringVar(value=0)
entry_val51 =StringVar(value=0)#
entry_val52 =StringVar(value=0)
entry_val53 =StringVar(value=0)
entry_val54 =StringVar(value=0)#
entry_val55 =StringVar(value=0)
entry_val56 =StringVar(value=0)
entry_val57 =StringVar(value=0)#
entry_val58 =StringVar(value=0)
entry_val59 =StringVar(value=0)
entry_val60 =StringVar(value=0)#
entry_val61 =StringVar(value=0)
entry_val62 =StringVar(value=0)
entry_val63 =StringVar(value=90)#
entry_val64 =StringVar(value=0)
entry_val65 =StringVar(value=0)
entry_val66 =StringVar(value=0)#
entry_val67 =StringVar(value=0)
entry_val68 =StringVar(value=0)
entry_val69 =StringVar(value=0)#
entry_val70 =StringVar(value=0)
entry_val71 =StringVar(value=0)
entry_val72 =StringVar(value=0)#
entry_val73 =StringVar(value=0)
entry_val74 =StringVar(value=0)
entry_val75 =StringVar(value=0)#
entry_val76 =StringVar(value=0)
entry_val77 =StringVar(value=0)
entry_val78 =StringVar(value=0)#
entry_val79 =StringVar(value=0)
entry_val80 =StringVar(value=0)
entry_val81 =StringVar(value=0)#
entry_val82 =StringVar(value=0)
entry_val83 =StringVar(value=0)
entry_val84 =StringVar(value=0)#
entry_val85 =StringVar(value=0)
entry_val86 =StringVar(value=0)
entry_val87 =StringVar(value=0)#
entry_val88 =StringVar(value=0)
entry_val89 =StringVar(value=0)
entry_val90 =StringVar(value=0)#

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)


mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill=BOTH, expand=1)

def submit():
    try:
        
        global entry_val1 
        global entry_val2 
        global entry_val3 
        global entry_val4 
        global entry_val5 
        global entry_val6 
        global entry_val7 
        global entry_val8 
        global entry_val9 
        global entry_val10 
        global entry_val11 
        global entry_val12 
        global entry_val13 
        global entry_val14 
        global entry_val15 
        global entry_val16 
        global entry_val17 
        global entry_val18 
        global entry_val19 
        global entry_val20 
        global entry_val21 
        global entry_val22 
        global entry_val23 
        global entry_val24 
        global entry_val25 
        global entry_val26 
        global entry_val27 
        global entry_val28 
        global entry_val29 
        global entry_val30 
        global entry_val31 
        global entry_val32 
        global entry_val33 
        global entry_val34
        global entry_val35 
        global entry_val36 
        global entry_val37 
        global entry_val38 
        global entry_val39 
        global entry_val40 
        global entry_val41 
        global entry_val42 
        global entry_val43 
        global entry_val44 
        global entry_val45 
        global entry_val46 
        global entry_val47 
        global entry_val48 
        global entry_val49 
        global entry_val50 
        global entry_val51 
        global entry_val52 
        global entry_val53 
        global entry_val54 
        global entry_val55 
        global entry_val56 
        global entry_val57 
        global entry_val58 
        global entry_val59 
        global entry_val60 
        global entry_val61 
        global entry_val62 
        global entry_val63 
        global entry_val64 
        global entry_val65 
        global entry_val66 
        global entry_val67 
        global entry_val68 
        global entry_val69 
        global entry_val70 
        global entry_val71 
        global entry_val72 
        global entry_val73 
        global entry_val74 
        global entry_val75 
        global entry_val76 
        global entry_val77 
        global entry_val78 
        global entry_val79 
        global entry_val80 
        global entry_val81 
        global entry_val82 
        global entry_val83 
        global entry_val84 
        global entry_val85 
        global entry_val86 
        global entry_val87 
        global entry_val88 
        global entry_val89 
        global entry_val90 

        marks_table = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]

        subject_no = 0
        exception_entry = 0

        mark1 = float(entry_val1.get())
        exception_entry = exception_entry + 1
        if float(entry_val1.get()) > 100 or float(entry_val1.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[0][0] = mark1

        mark2 = float(entry_val2.get())
        exception_entry = exception_entry + 1
        if float(entry_val2.get()) > 100 or float(entry_val2.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[0][1] = mark2

        mark3 = float(entry_val3.get())
        exception_entry = exception_entry + 1
        if float(entry_val3.get()) > 100 or float(entry_val3.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[0][2] = mark3

        mark4 = float(entry_val4.get())
        exception_entry = exception_entry + 1
        if float(entry_val4.get()) > 100 or float(entry_val4.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[1][0] = mark4

        mark5 = float(entry_val5.get())
        exception_entry = exception_entry + 1
        if float(entry_val5.get()) > 100 or float(entry_val5.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[1][1] = mark5

        mark6 = float(entry_val6.get())
        exception_entry = exception_entry + 1
        if float(entry_val6.get()) > 100 or float(entry_val6.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
            marks_table[1][2] = mark6

        mark7 = float(entry_val7.get())
        exception_entry = exception_entry + 1
        if float(entry_val7.get()) > 100 or float(entry_val7.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[2][0] = mark7

        mark8 = float(entry_val8.get())
        exception_entry = exception_entry + 1
        if float(entry_val8.get()) > 100 or float(entry_val8.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[2][1] = mark8

        mark9 = float(entry_val9.get())
        exception_entry = exception_entry + 1
        if float(entry_val9.get()) > 100 or float(entry_val9.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[2][2] = mark9

        mark10 = float(entry_val10.get())
        exception_entry = exception_entry + 1
        if float(entry_val10.get()) > 100 or float(entry_val10.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[3][0] = mark10

        mark11 = float(entry_val11.get())
        exception_entry = exception_entry + 1
        if float(entry_val11.get()) > 100 or float(entry_val11.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[3][1] = mark11

        mark12 = float(entry_val12.get())
        exception_entry = exception_entry + 1
        if float(entry_val12.get()) > 100 or float(entry_val12.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[3][2] = mark12

        mark13 = float(entry_val13.get())
        exception_entry = exception_entry + 1
        if float(entry_val13.get()) > 100 or float(entry_val13.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[4][0] = mark13

        mark14 = float(entry_val14.get())
        exception_entry = exception_entry + 1
        if float(entry_val14.get()) > 100 or float(entry_val14.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[4][1] = mark14

        mark15 = float(entry_val15.get())
        exception_entry = exception_entry + 1
        if float(entry_val15.get()) > 100 or float(entry_val15.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[4][2] = mark15

        mark16 = float(entry_val16.get())
        exception_entry = exception_entry + 1
        if float(entry_val16.get()) > 100 or float(entry_val16.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[5][0] = mark16

        mark17 = float(entry_val17.get())
        exception_entry = exception_entry + 1
        if float(entry_val17.get()) > 100 or float(entry_val17.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[5][1] = mark17

        mark18 = float(entry_val18.get())
        exception_entry = exception_entry + 1
        if float(entry_val18.get()) > 100 or float(entry_val18.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[5][2] = mark18

        mark19 = float(entry_val19.get())
        exception_entry = exception_entry + 1
        if float(entry_val19.get()) > 100 or float(entry_val19.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[6][0] = mark19

        mark20 = float(entry_val20.get())
        exception_entry = exception_entry + 1
        if float(entry_val20.get()) > 100 or float(entry_val20.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[6][1] = mark20

        mark21 = float(entry_val21.get())
        exception_entry = exception_entry + 1
        if float(entry_val21.get()) > 100 or float(entry_val21.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[6][2] = mark21

        mark22 = float(entry_val22.get())
        exception_entry = exception_entry + 1
        if float(entry_val22.get()) > 100 or float(entry_val22.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[7][0] = mark22

        mark23 = float(entry_val23.get())
        exception_entry = exception_entry + 1
        if float(entry_val23.get()) > 100 or float(entry_val23.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[7][1] = mark23

        mark24 = float(entry_val24.get())
        exception_entry = exception_entry + 1
        if float(entry_val24.get()) > 100 or float(entry_val24.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[7][2] = mark24

        mark25 = float(entry_val25.get())
        exception_entry = exception_entry + 1
        if float(entry_val25.get()) > 100 or float(entry_val25.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[8][0] = mark25

        mark26 = float(entry_val26.get())
        exception_entry = exception_entry + 1
        if float(entry_val26.get()) > 100 or float(entry_val26.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[8][1] = mark26

        mark27 = float(entry_val27.get())
        exception_entry = exception_entry + 1
        if float(entry_val27.get()) > 100 or float(entry_val27.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[8][2] = mark27

        mark28 = float(entry_val28.get())
        exception_entry = exception_entry + 1
        if float(entry_val28.get()) > 100 or float(entry_val28.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[9][0] = mark28

        mark29 = float(entry_val29.get())
        exception_entry = exception_entry + 1
        if float(entry_val29.get()) > 100 or float(entry_val29.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[9][1] = mark29

        mark30 = float(entry_val30.get())
        exception_entry = exception_entry + 1
        if float(entry_val30.get()) > 100 or float(entry_val30.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[9][2] = mark30

        mark31 = float(entry_val31.get())
        exception_entry = exception_entry + 1
        if float(entry_val31.get()) > 100 or float(entry_val31.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[10][0] = mark31

        mark32 = float(entry_val32.get())
        exception_entry = exception_entry + 1
        if float(entry_val32.get()) > 100 or float(entry_val32.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[10][1] = mark32

        mark33 = float(entry_val33.get())
        exception_entry = exception_entry + 1
        if float(entry_val33.get()) > 100 or float(entry_val33.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[10][2] = mark33

        mark34 = float(entry_val34.get())
        exception_entry = exception_entry + 1
        if float(entry_val34.get()) > 100 or float(entry_val34.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[11][0] = mark34

        mark35 = float(entry_val35.get())
        exception_entry = exception_entry + 1
        if float(entry_val35.get()) > 100 or float(entry_val35.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[11][1] = mark35

        mark36 = float(entry_val36.get())
        exception_entry = exception_entry + 1
        if float(entry_val36.get()) > 100 or float(entry_val36.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[11][2] = mark36

        mark37 = float(entry_val37.get())
        exception_entry = exception_entry + 1
        if float(entry_val37.get()) > 100 or float(entry_val37.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[12][0] = mark37

        mark38 = float(entry_val38.get())
        exception_entry = exception_entry + 1
        if float(entry_val38.get()) > 100 or float(entry_val38.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[12][1] = mark38

        mark39 = float(entry_val39.get())
        exception_entry = exception_entry + 1
        if float(entry_val39.get()) > 100 or float(entry_val39.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[12][2] = mark39

        mark40 = float(entry_val40.get())
        exception_entry = exception_entry + 1
        if float(entry_val40.get()) > 100 or float(entry_val40.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[13][0] = mark40

        mark41 = float(entry_val41.get())
        exception_entry = exception_entry + 1
        if float(entry_val41.get()) > 100 or float(entry_val41.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[13][1] = mark41

        mark42 = float(entry_val42.get())
        exception_entry = exception_entry + 1
        if float(entry_val42.get()) > 100 or float(entry_val42.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[13][2] = mark42

        mark43 = float(entry_val43.get())
        exception_entry = exception_entry + 1
        if float(entry_val43.get()) > 100 or float(entry_val43.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[14][0] = mark43

        mark44 = float(entry_val44.get())
        exception_entry = exception_entry + 1
        if float(entry_val44.get()) > 100 or float(entry_val44.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[14][1] = mark44

        mark45 = float(entry_val45.get())
        exception_entry = exception_entry + 1
        if float(entry_val45.get()) > 100 or float(entry_val45.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[14][2] = mark45

        mark46 = float(entry_val46.get())
        exception_entry = exception_entry + 1
        if float(entry_val46.get()) > 100 or float(entry_val46.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[15][0] = mark46

        mark47 = float(entry_val47.get())
        exception_entry = exception_entry + 1
        if float(entry_val47.get()) > 100 or float(entry_val47.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[15][1] = mark47

        mark48 = float(entry_val48.get())
        exception_entry = exception_entry + 1
        if float(entry_val48.get()) > 100 or float(entry_val48.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[15][2] = mark48

        mark49 = float(entry_val49.get())
        exception_entry = exception_entry + 1
        if float(entry_val49.get()) > 100 or float(entry_val49.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[16][0] = mark49

        mark50 = float(entry_val50.get())
        exception_entry = exception_entry + 1
        if float(entry_val50.get()) > 100 or float(entry_val50.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[16][1] = mark50

        mark51 = float(entry_val51.get())
        exception_entry = exception_entry + 1
        if float(entry_val51.get()) > 100 or float(entry_val51.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[16][2] = mark51

        mark52 = float(entry_val52.get())
        exception_entry = exception_entry + 1
        if float(entry_val52.get()) > 100 or float(entry_val52.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[17][0] = mark52

        mark53 = float(entry_val53.get())
        exception_entry = exception_entry + 1
        if float(entry_val53.get()) > 100 or float(entry_val53.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[17][1] = mark53

        mark54 = float(entry_val54.get())
        exception_entry = exception_entry + 1
        if float(entry_val54.get()) > 100 or float(entry_val54.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[17][2] = mark54

        mark55 = float(entry_val55.get())
        exception_entry = exception_entry + 1
        if float(entry_val55.get()) > 100 or float(entry_val55.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[18][0] = mark55

        mark56 = float(entry_val56.get())
        exception_entry = exception_entry + 1
        if float(entry_val56.get()) > 100 or float(entry_val56.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[18][1] = mark56

        mark57 = float(entry_val57.get())
        exception_entry = exception_entry + 1
        if float(entry_val57.get()) > 100 or float(entry_val57.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[18][2] = mark57

        mark58 = float(entry_val58.get())
        exception_entry = exception_entry + 1
        if float(entry_val58.get()) > 100 or float(entry_val58.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[19][0] = mark58

        mark59 = float(entry_val59.get())
        exception_entry = exception_entry + 1
        if float(entry_val59.get()) > 100 or float(entry_val59.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[19][1] = mark59

        mark60 = float(entry_val60.get())
        exception_entry = exception_entry + 1
        if float(entry_val60.get()) > 100 or float(entry_val60.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[19][2] = mark60

        mark61 = float(entry_val61.get())
        exception_entry = exception_entry + 1
        if float(entry_val61.get()) > 100 or float(entry_val61.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[20][0] = mark61

        mark62 = float(entry_val62.get())
        exception_entry = exception_entry + 1
        if float(entry_val62.get()) > 100 or float(entry_val62.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[20][1] = mark62

        mark63 = float(entry_val63.get())
        exception_entry = exception_entry + 1
        if float(entry_val63.get()) > 100 or float(entry_val63.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[20][2] = mark63

        mark64 = float(entry_val64.get())
        exception_entry = exception_entry + 1
        if float(entry_val64.get()) > 100 or float(entry_val64.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[21][0] = mark64

        mark65 = float(entry_val65.get())
        exception_entry = exception_entry + 1
        if float(entry_val65.get()) > 100 or float(entry_val65.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[21][1] = mark65

        mark66 = float(entry_val66.get())
        exception_entry = exception_entry + 1
        if float(entry_val66.get()) > 100 or float(entry_val66.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[21][2] = mark66

        mark67 = float(entry_val67.get())
        exception_entry = exception_entry + 1
        if float(entry_val67.get()) > 100 or float(entry_val67.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[22][0] = mark67

        mark68 = float(entry_val68.get())
        exception_entry = exception_entry + 1
        if float(entry_val68.get()) > 100 or float(entry_val68.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[22][1] = mark68

        mark69 = float(entry_val69.get())
        exception_entry = exception_entry + 1
        if float(entry_val69.get()) > 100 or float(entry_val69.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[22][2] = mark69

        mark70 = float(entry_val70.get())
        exception_entry = exception_entry + 1
        if float(entry_val70.get()) > 100 or float(entry_val70.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[23][0] = mark70

        mark71 = float(entry_val71.get())
        exception_entry = exception_entry + 1
        if float(entry_val71.get()) > 100 or float(entry_val71.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[23][1] = mark71

        mark72 = float(entry_val72.get())
        exception_entry = exception_entry + 1
        if float(entry_val72.get()) > 100 or float(entry_val72.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[23][2] = mark72

        mark73 = float(entry_val73.get())
        exception_entry = exception_entry + 1
        if float(entry_val73.get()) > 100 or float(entry_val73.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[24][0] = mark73

        mark74 = float(entry_val74.get())
        exception_entry = exception_entry + 1
        if float(entry_val74.get()) > 100 or float(entry_val74.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[24][1] = mark74

        mark75 = float(entry_val75.get())
        exception_entry = exception_entry + 1
        if float(entry_val75.get()) > 100 or float(entry_val75.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[24][2] = mark75

        mark76 = float(entry_val76.get())
        exception_entry = exception_entry + 1
        if float(entry_val76.get()) > 100 or float(entry_val76.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[25][0] = mark76

        mark77 = float(entry_val77.get())
        exception_entry = exception_entry + 1
        if float(entry_val77.get()) > 100 or float(entry_val77.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[25][1] = mark77

        mark78 = float(entry_val78.get())
        exception_entry = exception_entry + 1
        if float(entry_val78.get()) > 100 or float(entry_val78.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[25][2] = mark78

        mark79 = float(entry_val79.get())
        exception_entry = exception_entry + 1
        if float(entry_val79.get()) > 100 or float(entry_val79.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[26][0] = mark79

        mark80 = float(entry_val80.get())
        exception_entry = exception_entry + 1
        if float(entry_val80.get()) > 100 or float(entry_val80.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[26][1] = mark80

        mark81 = float(entry_val81.get())
        exception_entry = exception_entry + 1
        if float(entry_val81.get()) > 100 or float(entry_val81.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[26][2] = mark81

        mark82 = float(entry_val82.get())
        exception_entry = exception_entry + 1
        if float(entry_val82.get()) > 100 or float(entry_val82.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[27][0] = mark82

        mark83 = float(entry_val83.get())
        exception_entry = exception_entry + 1
        if float(entry_val83.get()) > 100 or float(entry_val83.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[27][1] = mark83

        mark84 = float(entry_val84.get())
        exception_entry = exception_entry + 1
        if float(entry_val84.get()) > 100 or float(entry_val84.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[27][2] = mark84

        mark85 = float(entry_val85.get())
        exception_entry = exception_entry + 1
        if float(entry_val85.get()) > 100 or float(entry_val85.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[28][0] = mark85

        mark86 = float(entry_val86.get())
        exception_entry = exception_entry + 1
        if float(entry_val86.get()) > 100 or float(entry_val86.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[28][1] = mark86

        mark87 = float(entry_val87.get())
        exception_entry = exception_entry + 1
        if float(entry_val87.get()) > 100 or float(entry_val87.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[28][2] = mark87

        mark88 = float(entry_val88.get())
        exception_entry = exception_entry + 1
        if float(entry_val88.get()) > 100 or float(entry_val88.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[29][0] = mark88

        mark89 = float(entry_val89.get())
        exception_entry = exception_entry + 1
        if float(entry_val89.get()) > 100 or float(entry_val89.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[29][1] = mark89

        mark90 = float(entry_val90.get())
        exception_entry = exception_entry + 1
        if float(entry_val90.get()) > 100 or float(entry_val90.get()) < 0:
            raise Exception("ERROR : Please enter a number in between 0 amd 100 for CS001 first entry box")
        marks_table[29][2] = mark90

        if mark1 or mark2 or mark3:
            subject_no += 1
        if mark4 or mark5 or mark6:
            subject_no += 1
        if mark7 or mark8 or mark9:
            subject_no += 1
        if mark10 or mark11 or mark12:
            subject_no += 1
        if mark13 or mark14 or mark15:
            subject_no += 1
        if mark16 or mark17 or mark18:
            subject_no += 1
        if mark19 or mark20 or mark21:
            subject_no += 1
        if mark22 or mark23 or mark24:
            subject_no += 1
        if mark25 or mark26 or mark27:
            subject_no += 1
        if mark28 or mark29 or mark30:
            subject_no += 1
        if mark31 or mark32 or mark33:
            subject_no += 1
        if mark34 or mark35 or mark36:
            subject_no += 1
        if mark37 or mark38 or mark39:
            subject_no += 1
        if mark40 or mark41 or mark42:
            subject_no += 1
        if mark43 or mark44 or mark45:
            subject_no += 1
        if mark46 or mark47 or mark48:
            subject_no += 1
        if mark49 or mark50 or mark51:
            subject_no += 1
        if mark52 or mark53 or mark54:
            subject_no += 1
        if mark55 or mark56 or mark57:
            subject_no += 1
        if mark58 or mark59 or mark60:
            subject_no += 1
        if mark61 or mark62 or mark63:
            subject_no += 1
        if mark64 or mark65 or mark66:
            subject_no += 1
        if mark67 or mark68 or mark69:
            subject_no += 1
        if mark70 or mark71 or mark72:
            subject_no += 1
        if mark73 or mark74 or mark75:
            subject_no += 1
        if mark76 or mark77 or mark78:
            subject_no += 1
        if mark79 or mark80 or mark81:
            subject_no += 1
        if mark82 or mark83 or mark84:
            subject_no += 1
        if mark85 or mark86 or mark87:
            subject_no += 1
        if mark88 or mark89 or mark90:
            subject_no += 1
        
        if subject_no <= 12:
            raise Exception("you need to complete at least 12 modules. not qualified for the honours study")
            # win1 = Toplevel(myframe)
            # Label(win1, text = "you need to complete at least 12 modules. not qualified for the honours study", width=60, height=10, font=('Times', 15)).pack()

        mark_arr = json.dumps(marks_table).encode()
        client.send(mark_arr)

        server_msg = json.loads(client.recv(1024).decode())

        if server_msg[1] == "with 2 or more Fails! DOES NOT QUALIFY FOR HONORS STUDY!":
            win1 = Toplevel(myframe)
            Label(win1, text = "Your avearge is :"+str(server_msg[0]), width=60, height=10, font=('Times', 15)).pack()
            Label(win1, text = server_msg[1], width=60, height=10, font=('Times', 15)).pack()
        elif server_msg[1] == "QUALIFIED FOR HONOURS STUDY!":
            win1 = Toplevel(myframe)
            Label(win1, text = "Your avearge is :"+str(server_msg[0]), width=60, height=10, font=('Times', 15)).pack()
            Label(win1, text = server_msg[1], width=60, height=10, font=('Times', 15)).pack()
        elif server_msg[1] == "MAY HAVE GOOD CHANCE! Need further assessment!":
            win1 = Toplevel(myframe)
            Label(win1, text = "Your avearge is :"+str(server_msg[0]), width=60, height=10, font=('Times', 15)).pack()
            Label(win1, text = server_msg[1], width=60, height=10, font=('Times', 15)).pack()
        elif server_msg[1] == "MAY HAVE A CHANCE! Must be carefully reassessed and get the coordinator's permission!":
            win1 = Toplevel(myframe)
            Label(win1, text = "Your avearge is :"+str(server_msg[0]), width=60, height=10, font=('Times', 15)).pack()
            Label(win1, text = server_msg[1], width=60, height=10, font=('Times', 15)).pack()
        else:
            win1 = Toplevel(myframe)
            Label(win1, text = "Your avearge is :"+str(server_msg[0]), width=60, height=10, font=('Times', 15)).pack()
            Label(win1, text = server_msg[1], width=60, height=10, font=('Times', 15)).pack()

    except ValueError:
        win1 = Toplevel(myframe)
        Label(win1, text = "ERROR : Please enter a number for "+str(exception_entry+1)+" th entry box", width=60, height=10, font=('Times', 15)).pack()
    
    except Exception as e:
        win1 = Toplevel(myframe)
        Label(win1, text = e, width=80, height=10, font=('Times', 15)).pack()
    
    finally:
        entry_val1.delete(0, END) 
        entry_val2.delete(0, END) 
        entry_val3.delete(0, END) 
        entry_val4.delete(0, END) 
        entry_val5.delete(0, END) 
        entry_val6.delete(0, END) 
        entry_val7.delete(0, END) 
        entry_val8.delete(0, END) 
        entry_val9.delete(0, END) 
        entry_val10.delete(0, END) 
        entry_val11.delete(0, END) 
        entry_val12.delete(0, END) 
        entry_val13.delete(0, END) 
        entry_val14.delete(0, END) 
        entry_val15.delete(0, END) 
        entry_val16.delete(0, END) 
        entry_val17.delete(0, END) 
        entry_val18.delete(0, END) 
        entry_val19.delete(0, END) 
        entry_val20.delete(0, END) 
        entry_val21.delete(0, END) 
        entry_val22.delete(0, END) 
        entry_val23.delete(0, END) 
        entry_val24.delete(0, END) 
        entry_val25.delete(0, END) 
        entry_val26.delete(0, END) 
        entry_val27.delete(0, END) 
        entry_val28.delete(0, END) 
        entry_val29.delete(0, END) 
        entry_val30.delete(0, END) 
        entry_val31.delete(0, END) 
        entry_val32.delete(0, END) 
        entry_val33.delete(0, END) 
        entry_val34.delete(0, END)
        entry_val35.delete(0, END) 
        entry_val36.delete(0, END) 
        entry_val37.delete(0, END) 
        entry_val38.delete(0, END) 
        entry_val39.delete(0, END) 
        entry_val40.delete(0, END) 
        entry_val41.delete(0, END)
        entry_val42.delete(0, END) 
        entry_val43.delete(0, END) 
        entry_val44.delete(0, END) 
        entry_val45.delete(0, END) 
        entry_val46.delete(0, END) 
        entry_val47.delete(0, END) 
        entry_val48.delete(0, END) 
        entry_val49.delete(0, END) 
        entry_val50.delete(0, END) 
        entry_val51.delete(0, END) 
        entry_val52.delete(0, END) 
        entry_val53.delete(0, END) 
        entry_val54.delete(0, END) 
        entry_val55.delete(0, END) 
        entry_val56.delete(0, END) 
        entry_val57.delete(0, END) 
        entry_val58.delete(0, END) 
        entry_val59.delete(0, END) 
        entry_val60.delete(0, END) 
        entry_val61.delete(0, END) 
        entry_val62.delete(0, END) 
        entry_val63.delete(0, END) 
        entry_val64.delete(0, END) 
        entry_val65.delete(0, END) 
        entry_val66.delete(0, END) 
        entry_val67.delete(0, END)  
        entry_val68.delete(0, END)  
        entry_val69.delete(0, END)  
        entry_val70.delete(0, END)  
        entry_val71.delete(0, END)  
        entry_val72.delete(0, END)  
        entry_val73.delete(0, END)  
        entry_val74.delete(0, END)  
        entry_val75.delete(0, END)  
        entry_val76.delete(0, END)  
        entry_val77.delete(0, END)  
        entry_val78.delete(0, END)  
        entry_val79.delete(0, END)  
        entry_val79.delete(0, END)  
        entry_val80.delete(0, END)   
        entry_val81.delete(0, END)   
        entry_val82.delete(0, END)   
        entry_val83.delete(0, END)   
        entry_val84.delete(0, END)   
        entry_val85.delete(0, END)   
        entry_val86.delete(0, END)   
        entry_val87.delete(0, END)   
        entry_val88.delete(0, END)   
        entry_val89.delete(0, END)   
        entry_val90.delete(0, END)

        entry_val1 = 0 
        entry_val2 = 0 
        entry_val3 = 0  
        entry_val4 = 0 
        entry_val5 = 0 
        entry_val6 = 0 
        entry_val7 = 0 
        entry_val8 = 0 
        entry_val9 = 0 
        entry_val10 = 0 
        entry_val11 = 0 
        entry_val12 = 0 
        entry_val13 = 0
        entry_val14 = 0 
        entry_val15 = 0 
        entry_val16 = 0 
        entry_val17 = 0 
        entry_val18 = 0 
        entry_val19 = 0 
        entry_val20 = 0 
        entry_val21 = 0
        entry_val22 = 0 
        entry_val23 = 0 
        entry_val24 = 0 
        entry_val25 = 0 
        entry_val26 = 0 
        entry_val27 = 0 
        entry_val28 = 0 
        entry_val29 = 0 
        entry_val30 = 0 
        entry_val31 = 0 
        entry_val32 = 0 
        entry_val33 = 0 
        entry_val34 = 0 
        entry_val35 = 0 
        entry_val36 = 0 
        entry_val37 = 0 
        entry_val38 = 0 
        entry_val39 = 0 
        entry_val40 = 0 
        entry_val41 = 0 
        entry_val42 = 0 
        entry_val43 = 0 
        entry_val44 = 0 
        entry_val45 = 0 
        entry_val46 = 0
        entry_val47 = 0 
        entry_val48 = 0 
        entry_val49 = 0 
        entry_val50 = 0 
        entry_val51 = 0 
        entry_val52 = 0 
        entry_val53 = 0 
        entry_val54 = 0 
        entry_val55 = 0 
        entry_val56 = 0 
        entry_val57 = 0 
        entry_val58 = 0 
        entry_val59 = 0 
        entry_val60 = 0 
        entry_val61 = 0 
        entry_val62 = 0 
        entry_val63 = 0 
        entry_val64 = 0 
        entry_val65 = 0 
        entry_val66 = 0 
        entry_val67 = 0 
        entry_val68 = 0 
        entry_val69 = 0 
        entry_val70 = 0 
        entry_val71 = 0 
        entry_val72 = 0 
        entry_val73 = 0 
        entry_val74 = 0 
        entry_val75 = 0 
        entry_val76 = 0 
        entry_val77 = 0 
        entry_val78 = 0 
        entry_val79 = 0  
        entry_val80 = 0 
        entry_val81 = 0 
        entry_val82 = 0 
        entry_val83 = 0 
        entry_val84 = 0 
        entry_val85 = 0 
        entry_val86 = 0 
        entry_val87 = 0 
        entry_val88 = 0 
        entry_val89 = 0 
        entry_val90 = 0 


button = Button(wrapper2, text="Submit Results", command=submit, height= 5, width=20, font=('Times', 20)).pack()
#button.pack(side=LEFT, fill=BOTH, expand=1)


yscrollbar = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill=Y)

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")

wrapper1.pack(fill=BOTH, expand=1, padx=10, pady=10)
wrapper2.pack(fill=BOTH, expand=1, padx=10, pady=10)

label1 = Label(myframe, text="CS001").grid(row=1, column=0, pady=10, padx=10)
label1_entry1 = Entry(myframe, textvariable=entry_val1).grid(row=1, column=1, pady=10, padx=10)
label1_entry2 = Entry(myframe, textvariable=entry_val2).grid(row=1, column=2, pady=10, padx=10)
label1_entry3 = Entry(myframe, textvariable=entry_val3).grid(row=1, column=3, pady=10, padx=10)

label2 = Label(myframe, text="CS002").grid(row=2, column=0, pady=10, padx=10)
label2_entry1 = Entry(myframe, textvariable=entry_val4).grid(row=2, column=1, pady=10, padx=10)
label2_entry2 = Entry(myframe, textvariable=entry_val5).grid(row=2, column=2, pady=10, padx=10)
label2_entry3 = Entry(myframe, textvariable=entry_val6).grid(row=2, column=3, pady=10, padx=10)

label3 = Label(myframe, text="CS003").grid(row=3, column=0, pady=10, padx=10)
label3_entry1 = Entry(myframe, textvariable=entry_val7).grid(row=3, column=1, pady=10, padx=10)
label3_entry2 = Entry(myframe, textvariable=entry_val8).grid(row=3, column=2, pady=10, padx=10)
label3_entry3 = Entry(myframe, textvariable=entry_val9).grid(row=3, column=3, pady=10, padx=10)

label4 = Label(myframe, text="CS004").grid(row=4, column=0, pady=10, padx=10)
label4_entry1 = Entry(myframe, textvariable=entry_val10).grid(row=4, column=1, pady=10, padx=10)
label4_entry2 = Entry(myframe, textvariable=entry_val11).grid(row=4, column=2, pady=10, padx=10)
label4_entry3 = Entry(myframe, textvariable=entry_val12).grid(row=4, column=3, pady=10, padx=10)

label5 = Label(myframe, text="CS005").grid(row=5, column=0, pady=10, padx=10)
label5_entry1 = Entry(myframe, textvariable=entry_val13).grid(row=5, column=1, pady=10, padx=10)
label5_entry2 = Entry(myframe, textvariable=entry_val14).grid(row=5, column=2, pady=10, padx=10)
label5_entry3 = Entry(myframe, textvariable=entry_val15).grid(row=5, column=3, pady=10, padx=10)

label6 = Label(myframe, text="CS006").grid(row=6, column=0, pady=10, padx=10)
label6_entry1 = Entry(myframe, textvariable=entry_val16).grid(row=6, column=1, pady=10, padx=10)
label6_entry2 = Entry(myframe, textvariable=entry_val17).grid(row=6, column=2, pady=10, padx=10)
label6_entry3 = Entry(myframe, textvariable=entry_val18).grid(row=6, column=3, pady=10, padx=10)

label7 = Label(myframe, text="CS007").grid(row=7, column=0, pady=10, padx=10)
label7_entry1 = Entry(myframe, textvariable=entry_val19).grid(row=7, column=1, pady=10, padx=10)
label7_entry2 = Entry(myframe, textvariable=entry_val20).grid(row=7, column=2, pady=10, padx=10)
label7_entry3 = Entry(myframe, textvariable=entry_val21).grid(row=7, column=3, pady=10, padx=10)

label8 = Label(myframe, text="CS008").grid(row=8, column=0, pady=10, padx=10)
label8_entry1 = Entry(myframe, textvariable=entry_val22).grid(row=8, column=1, pady=10, padx=10)
label8_entry2 = Entry(myframe, textvariable=entry_val23).grid(row=8, column=2, pady=10, padx=10)
label8_entry3 = Entry(myframe, textvariable=entry_val24).grid(row=8, column=3, pady=10, padx=10)

label9 = Label(myframe, text="CS009").grid(row=9, column=0, pady=10, padx=10)
label9_entry1 = Entry(myframe, textvariable=entry_val25).grid(row=9, column=1, pady=10, padx=10)
label9_entry2 = Entry(myframe, textvariable=entry_val26).grid(row=9, column=2, pady=10, padx=10)
label9_entry3 = Entry(myframe, textvariable=entry_val27).grid(row=9, column=3, pady=10, padx=10)

label10 = Label(myframe, text="CS010").grid(row=10, column=0, pady=10, padx=10)
label10_entry1 = Entry(myframe, textvariable=entry_val28).grid(row=10, column=1, pady=10, padx=10)
label10_entry2 = Entry(myframe, textvariable=entry_val29).grid(row=10, column=2, pady=10, padx=10)
label10_entry3 = Entry(myframe, textvariable=entry_val30).grid(row=10, column=3, pady=10, padx=10)

label11 = Label(myframe, text="CS011").grid(row=11, column=0, pady=10, padx=10)
label11_entry1 = Entry(myframe, textvariable=entry_val31).grid(row=11, column=1, pady=10, padx=10)
label11_entry2 = Entry(myframe, textvariable=entry_val32).grid(row=11, column=2, pady=10, padx=10)
label11_entry3 = Entry(myframe, textvariable=entry_val33).grid(row=11, column=3, pady=10, padx=10)

label12 = Label(myframe, text="CS012").grid(row=12, column=0, pady=10, padx=10)
label12_entry1 = Entry(myframe, textvariable=entry_val34).grid(row=12, column=1, pady=10, padx=10)
label12_entry2 = Entry(myframe, textvariable=entry_val35).grid(row=12, column=2, pady=10, padx=10)
label12_entry3 = Entry(myframe, textvariable=entry_val36).grid(row=12, column=3, pady=10, padx=10)

label13 = Label(myframe, text="CS013").grid(row=13, column=0, pady=10, padx=10)
label13_entry1 = Entry(myframe, textvariable=entry_val37).grid(row=13, column=1, pady=10, padx=10)
label13_entry2 = Entry(myframe, textvariable=entry_val38).grid(row=13, column=2, pady=10, padx=10)
label13_entry3 = Entry(myframe, textvariable=entry_val19).grid(row=13, column=3, pady=10, padx=10)

label14 = Label(myframe, text="CS014").grid(row=14, column=0, pady=10, padx=10)
label14_entry1 = Entry(myframe, textvariable=entry_val40).grid(row=14, column=1, pady=10, padx=10)
label14_entry2 = Entry(myframe, textvariable=entry_val41).grid(row=14, column=2, pady=10, padx=10)
label14_entry3 = Entry(myframe, textvariable=entry_val42).grid(row=14, column=3, pady=10, padx=10)

label15 = Label(myframe, text="CS015").grid(row=15, column=0, pady=10, padx=10)
label15_entry1 = Entry(myframe, textvariable=entry_val43).grid(row=15, column=1, pady=10, padx=10)
label15_entry2 = Entry(myframe, textvariable=entry_val44).grid(row=15, column=2, pady=10, padx=10)
label15_entry3 = Entry(myframe, textvariable=entry_val45).grid(row=15, column=3, pady=10, padx=10)

label16 = Label(myframe, text="CS016").grid(row=16, column=0, pady=10, padx=10)
label16_entry1 = Entry(myframe, textvariable=entry_val46).grid(row=16, column=1, pady=10, padx=10)
label16_entry2 = Entry(myframe, textvariable=entry_val47).grid(row=16, column=2, pady=10, padx=10)
label16_entry3 = Entry(myframe, textvariable=entry_val48).grid(row=16, column=3, pady=10, padx=10)

label17 = Label(myframe, text="CS017").grid(row=17, column=0, pady=10, padx=10)
label17_entry1 = Entry(myframe, textvariable=entry_val49).grid(row=17, column=1, pady=10, padx=10)
label17_entry2 = Entry(myframe, textvariable=entry_val50).grid(row=17, column=2, pady=10, padx=10)
label17_entry3 = Entry(myframe, textvariable=entry_val51).grid(row=17, column=3, pady=10, padx=10)

label18 = Label(myframe, text="CS018").grid(row=18, column=0, pady=10, padx=10)
label18_entry1 = Entry(myframe, textvariable=entry_val52).grid(row=18, column=1, pady=10, padx=10)
label18_entry2 = Entry(myframe, textvariable=entry_val53).grid(row=18, column=2, pady=10, padx=10)
label18_entry3 = Entry(myframe, textvariable=entry_val54).grid(row=18, column=3, pady=10, padx=10)

label19 = Label(myframe, text="CS019").grid(row=19, column=0, pady=10, padx=10)
label19_entry1 = Entry(myframe, textvariable=entry_val55).grid(row=19, column=1, pady=10, padx=10)
label19_entry2 = Entry(myframe, textvariable=entry_val56).grid(row=19, column=2, pady=10, padx=10)
label19_entry3 = Entry(myframe, textvariable=entry_val57).grid(row=19, column=3, pady=10, padx=10)

label20 = Label(myframe, text="CS020").grid(row=20, column=0, pady=10, padx=10)
label20_entry1 = Entry(myframe, textvariable=entry_val58).grid(row=20, column=1, pady=10, padx=10)
label20_entry2 = Entry(myframe, textvariable=entry_val59).grid(row=20, column=2, pady=10, padx=10)
label20_entry3 = Entry(myframe, textvariable=entry_val60).grid(row=20, column=3, pady=10, padx=10)

label21 = Label(myframe, text="CS021").grid(row=21, column=0, pady=10, padx=10)
label21_entry1 = Entry(myframe, textvariable=entry_val61).grid(row=21, column=1, pady=10, padx=10)
label21_entry2 = Entry(myframe, textvariable=entry_val62).grid(row=21, column=2, pady=10, padx=10)
label21_entry3 = Entry(myframe, textvariable=entry_val63).grid(row=21, column=3, pady=10, padx=10)

label22 = Label(myframe, text="CS022").grid(row=22, column=0, pady=10, padx=10)
label22_entry1 = Entry(myframe, textvariable=entry_val64).grid(row=22, column=1, pady=10, padx=10)
label22_entry2 = Entry(myframe, textvariable=entry_val65).grid(row=22, column=2, pady=10, padx=10)
label22_entry3 = Entry(myframe, textvariable=entry_val66).grid(row=22, column=3, pady=10, padx=10)

label23 = Label(myframe, text="CS023").grid(row=23, column=0, pady=10, padx=10)
label23_entry1 = Entry(myframe, textvariable=entry_val67).grid(row=23, column=1, pady=10, padx=10)
label23_entry2 = Entry(myframe, textvariable=entry_val68).grid(row=23, column=2, pady=10, padx=10)
label23_entry3 = Entry(myframe, textvariable=entry_val69).grid(row=23, column=3, pady=10, padx=10)

label24 = Label(myframe, text="CS024").grid(row=24, column=0, pady=10, padx=10)
label24_entry1 = Entry(myframe, textvariable=entry_val70).grid(row=24, column=1, pady=10, padx=10)
label24_entry2 = Entry(myframe, textvariable=entry_val71).grid(row=24, column=2, pady=10, padx=10)
label24_entry3 = Entry(myframe, textvariable=entry_val72).grid(row=24, column=3, pady=10, padx=10)

label25 = Label(myframe, text="CS025").grid(row=25, column=0, pady=10, padx=10)
label25_entry1 = Entry(myframe, textvariable=entry_val73).grid(row=25, column=1, pady=10, padx=10)
label25_entry2 = Entry(myframe, textvariable=entry_val74).grid(row=25, column=2, pady=10, padx=10)
label25_entry3 = Entry(myframe, textvariable=entry_val75).grid(row=25, column=3, pady=10, padx=10)

label26 = Label(myframe, text="CS026").grid(row=26, column=0, pady=10, padx=10)
label26_entry1 = Entry(myframe, textvariable=entry_val76).grid(row=26, column=1, pady=10, padx=10)
label26_entry2 = Entry(myframe, textvariable=entry_val77).grid(row=26, column=2, pady=10, padx=10)
label26_entry3 = Entry(myframe, textvariable=entry_val78).grid(row=26, column=3, pady=10, padx=10)

label27 = Label(myframe, text="CS027").grid(row=27, column=0, pady=10, padx=10)
label27_entry1 = Entry(myframe, textvariable=entry_val79).grid(row=27, column=1, pady=10, padx=10)
label27_entry2 = Entry(myframe, textvariable=entry_val80).grid(row=27, column=2, pady=10, padx=10)
label27_entry3 = Entry(myframe, textvariable=entry_val81).grid(row=27, column=3, pady=10, padx=10)

label28 = Label(myframe, text="CS028").grid(row=28, column=0, pady=10, padx=10)
label28_entry1 = Entry(myframe, textvariable=entry_val82).grid(row=28, column=1, pady=10, padx=10)
label28_entry2 = Entry(myframe, textvariable=entry_val83).grid(row=28, column=2, pady=10, padx=10)
label28_entry3 = Entry(myframe, textvariable=entry_val84).grid(row=28, column=3, pady=10, padx=10)

label29 = Label(myframe, text="CS029").grid(row=29, column=0, pady=10, padx=10)
label29_entry1 = Entry(myframe, textvariable=entry_val85).grid(row=29, column=1, pady=10, padx=10)
label29_entry2 = Entry(myframe, textvariable=entry_val86).grid(row=29, column=2, pady=10, padx=10)
label29_entry3 = Entry(myframe, textvariable=entry_val87).grid(row=29, column=3, pady=10, padx=10)

label30 = Label(myframe, text="CS030").grid(row=30, column=0, pady=10, padx=10)
label30_entry1 = Entry(myframe, textvariable=entry_val88).grid(row=30, column=1, pady=10, padx=10)
label30_entry2 = Entry(myframe, textvariable=entry_val89).grid(row=30, column=2, pady=10, padx=10)
label30_entry3 = Entry(myframe, textvariable=entry_val90).grid(row=30, column=3, pady=10, padx=10)

# try:
#     client.connect(ADDR)
# except Exception as b:
#     win1 = Toplevel(myframe)
#     Label(win1, text = b, width=80, height=10, font=('Times', 15)).pack()

win.geometry("800x800")
win.title("Honors Enrolment Pre-assessment System (HEPaS)")
win.mainloop()