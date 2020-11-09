import tkinter as tk
from tkinter import ttk 
import tkinter.font as tkFont
import math
import random
import time

from csv_handeling import append_indvidual_test
from csv_handeling import append_all_data
from csv_handeling import setup_heaedr_individual_test
from csv_handeling import setup_header_all_data

from plotting import plot_ID_vs_MT
from plotting import plot_D_vs_MT
from plotting import plot_W_vs_MT

#UI functions
def make_label(master,text,x, y, w, h, background, textColor, fontStyle):
    label_frame = tk.Frame(master, width=w, height=h, bg=background)
    label_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
    label = tk.Label(label_frame, bg=background, fg=textColor,text=text, font=fontStyle)
    label.pack()
    label_frame.place(x=x,y=y)
    return label_frame

def make_button():
    global buttons_clicked
    global max_clicks
    if buttons_clicked == max_clicks: 
        global test_id, index_D, movement_t, test_width, test_distance
        append_all_data(index_D, movement_t, test_width, test_distance)
        append_indvidual_test(test_id, index_D, movement_t, test_width, test_distance)
        main_loop()
        return
    width = random_width()
    dist = random_dist()
    shift = dist
    if not origin_right: shift = -1 * (dist + width)

    button = tk.Frame(app, width=width, height=Button_height, bg="#2353ba")
    button.pack_propagate(0) # Stops child widgets of label_frame from resizing it
    button.place(x=origin_x+shift, y=height_center(Button_height))
    button.bind("<Button-1>", lambda event, button=button, shift=shift, width=width: make_button_helper(button, shift, width))
    global starting_time
    starting_time = time.time()
    return button

def make_button_helper(button, shift, width):
    global ending_time
    ending_time = time.time()
    global starting_time
    movement_time = ending_time - starting_time

    button.destroy()
    global origin_right
    global buttons_clicked
    buttons_clicked += 1
    origin_right = not origin_right

    global home_x
    global test_dist
    global test_id
    current_x = origin_x + shift + (width/2)
    if buttons_clicked > 1: test_dist = abs(home_x - current_x)
    home_x = current_x

    #data packing
    if buttons_clicked > 1:
        global index_D
        x = (2*test_dist) / width
        iD = math.log(x, 2)
        index_D.append(iD)
        global movement_t
        movement_t.append(movement_time)
        global test_width
        test_width.append(width)
        global test_distance
        test_distance.append(test_dist)

    make_button()

def start_test(event):
    start_btn.destroy()
    instructions2.destroy()
    true_or_false = [True, False]
    global origin_right
    origin_right = true_or_false[random.randint(0,1)]
    global buttons_clicked
    buttons_clicked = 0
    global test_id
    test_id += 1

    file = open("sys_settings/test_id.txt", "w")
    file.write(str(test_id))
    file.close()
    
    global index_D
    index_D = []
    global movement_t
    movement_t = []
    global test_width
    test_width = []
    global test_distance
    test_distance = []
    make_button()

def main_loop():
    global instructions2
    global start_btn
    global start_btn_text
    instructions2 = make_label(app,
                              "click start to begin",
                              500, 70,
                              400, 30,
                              "white", "black", fontStyleBody)
        
    start_btn = tk.Frame(app, width=150, height=30, bg="#2353ba")
    start_btn.pack_propagate(0) # Stops child widgets of label_frame from resizing it
    start_btn_text= tk.Label(start_btn, bg="#2353ba", fg="white",text="start", font=fontStyleTitle)
    start_btn_text.pack()
    start_btn.place(x=625, y=100)
    start_btn.bind("<Button-1>", start_test)
    start_btn_text.bind("<Button-1>", start_test)

def height_center(element_height):
    return (820 - element_height)/2

def random_width():
    random_index = random.randint(0, len(widths)-1)
    width =  widths[random_index]
    # widths.pop(random_index)
    return width

def random_dist():
    random_index = random.randint(0, len(distance_from_origin)-1)
    distance = distance_from_origin[random_index]
    return distance

#System variables
Button_height = 40
origin_x =700
origin_y =410
widths = [5, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
distance_from_origin = [0, 100, 200, 300, 400, 500]
origin_right = True
buttons_clicked = 3
instructions2 = None
start_btn = None
start_btn_text = None
starting_time = None
ending_time = None
test_id = 0
home_x = 0
test_dist = 0
max_clicks = 10
max_clicks += 1
index_D = []
movement_t = []
test_width = []
test_distance = []

if __name__ == "__main__":
    app = tk.Tk()
    app.resizable(0, 0)
    app.title("Fitt's Law experiment")
    app.geometry("1400x820")

    fontStyleTitle = tkFont.Font(family="Lucida Grande", size=20)
    fontStyleBody = tkFont.Font(family="Lucida Grande", size=15)


    title = make_label(app, "Fitt's Law Experiment",
                    350, 20,
                    700, 30,
                    "white", "#2353ba", fontStyleTitle)

    instructions1 = make_label(app,
                              "click the buttons that will appear randomly on screen",
                              500, 50,
                              400, 30,
                              "white", "black", fontStyleBody)

    plot_btn = tk.Frame(app, width=200, height=30, bg="#2353ba")
    plot_btn.pack_propagate(0) # Stops child widgets of label_frame from resizing it
    plot_btn_text= tk.Label(plot_btn, bg="#2353ba", fg="white",text="plot ID vs MT", font=fontStyleTitle)
    plot_btn_text.pack()
    plot_btn.place(x=1100, y=20)
    plot_btn.bind("<Button-1>", plot_ID_vs_MT)
    plot_btn_text.bind("<Button-1>", plot_ID_vs_MT)

    plot2_btn = tk.Frame(app, width=200, height=30, bg="#2353ba")
    plot2_btn.pack_propagate(0) # Stops child widgets of label_frame from resizing it
    plot2_btn_text= tk.Label(plot2_btn, bg="#2353ba", fg="white",text="plot D vs MT", font=fontStyleTitle)
    plot2_btn_text.pack()
    plot2_btn.place(x=1100, y=60)
    plot2_btn.bind("<Button-1>", plot_D_vs_MT)
    plot2_btn_text.bind("<Button-1>", plot_D_vs_MT)

    plot3_btn = tk.Frame(app, width=200, height=30, bg="#2353ba")
    plot3_btn.pack_propagate(0) # Stops child widgets of label_frame from resizing it
    plot3_btn_text= tk.Label(plot3_btn, bg="#2353ba", fg="white",text="plot W vs MT", font=fontStyleTitle)
    plot3_btn_text.pack()
    plot3_btn.place(x=1100, y=100)
    plot3_btn.bind("<Button-1>", plot_W_vs_MT)
    plot3_btn_text.bind("<Button-1>", plot_W_vs_MT)

    file = open("sys_settings/test_id.txt", "r")
    test_id = int(file.readline())
    file.close()

    if test_id < 1: 
        setup_heaedr_individual_test(max_clicks)
        setup_header_all_data()

    main_loop()
    app.mainloop()



