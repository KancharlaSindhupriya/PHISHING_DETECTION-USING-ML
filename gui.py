from tkinter import *
from PIL import Image, ImageTk
import run

scr = Tk()
scr.geometry('1920x1080+0+0')  # Increased dimensions (width x height) and position (x, y)
scr.resizable(width=True, height=True)

def retrieve_input():
    global us
    input1 = us.get()
    print(input1)
    out = run.main(input1)
    print(out)
    if out == "Warning The website is harmful for you":
        v1 = StringVar()
        v1.set(out)
        l2 = Label(f, text='Phishing / Not Phishing', textvariable=v1, font=('times', 20, 'bold'), bg='white', fg='red')
        l2.place(x=500, y=300)
    else:
        v1 = StringVar()
        v1.set(out)
        l2 = Label(f, text='Phishing / Not Phishing', textvariable=v1, font=('times', 20, 'bold'), bg='white', fg='red')
        l2.place(x=500, y=300)

l = Label(scr, text="Phishing Website Detection", font=('times', 20, 'bold'), bg='blue', fg='white')
l.pack(side=TOP, fill=X)
f = Frame(scr, bg='orange')
f.pack(fill=BOTH, expand=12)
v = StringVar()
l1 = Label(f, text='  Write The Website  ', font=('times', 20, 'bold'), bg='white', fg='black')
l1.place(x=300, y=100)
us = Entry(f, font=('times', 20, 'bold'), bg='white', fg='black', textvariable=v, width=50)
us.place(x=600, y=100)
b1 = Button(f, text='Predict', font=('times', 20, 'bold'), command=retrieve_input)
b1.place(x=700, y=200)

image_label = None  # A global variable to hold the image label
image_displayed = False  # Flag to keep track of image display status

def display_image():
    global image_label, image_displayed

    if not image_displayed:
        image_path = r"C:\Users\DELL\Downloads\Detecting-Phishing-Website-master (1)\Detecting-Phishing-Website-master\final/image.png"
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)

        # Create a label to display the image
        image_label = Label(f, image=img)
        image_label.image = img
        image_label.place(x=0.5, y=350)
        image_displayed = True
    else:
        # Remove the image label
        image_label.place_forget()
        image_displayed = False

image_button = Button(f, text="ACCURACY IMAGE", command=display_image, bg="yellow", font=("Arial", 12), fg="black")
image_button.place(x=50, y=100)

result_image_label = None  # A global variable to hold the result image label
result_image_displayed = False  # Flag to keep track of result image display status

def display_result_image():
    global result_image_label, result_image_displayed

    if not result_image_displayed:
        result_image_path = "C:/Users/DELL/Downloads/Detecting-Phishing-Website-master (1)/Detecting-Phishing-Website-master/final/image2.png"  # Replace with the actual path to your result image
        result_img = Image.open(result_image_path)
        result_img = ImageTk.PhotoImage(result_img)

        # Create a label to display the result image
        result_image_label = Label(f, image=result_img)
        result_image_label.image = result_img
        result_image_label.place(relx=0.5, rely=0.7, anchor=CENTER)
        result_image_displayed = True
    else:
        # Remove the result image label
        result_image_label.place_forget()
        result_image_displayed = False

result_button = Button(f, text="Result Image", command=display_result_image, bg="yellow", font=("Arial", 12), fg="black")
result_button.place(relx=0.5, rely=0.5, anchor=CENTER)

scr.mainloop()
