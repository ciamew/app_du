import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import PyPDF2

win = tk.Tk()

canvas = tk.Canvas(win, width=600,height=300)
canvas.grid(columnspan=3, rowspan=3) #rozdelilo mi to canvas na 3 neviditelne stlpce

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo) #z pillow image na tkinter image
logo_label = tk.Label(image=logo)
logo_label.image = logo

logo_label.grid(column=1,row=0)

inst = tk.Label(win, text="Select a PDF file on your PC to extract all its text")
inst.grid(columnspan=3,column=0,row=1)

def openfile():
    browse_text.set("loading...")
    file = askopenfile(parent=win, mode="rb", title="Choose a file",filetype=[("PDF file","*.pdf")])
    if file:
        # print("The file was succesfully loaded")
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_text = page.extractText()

        text_box = tk.Text(win, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_text)
        text_box.tag_configure("center", justify="center")  #upravuje text na stred
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1,row=3)

        browse_text.set("BROWSE")

browse_text = tk.StringVar()
browse_button = tk.Button(win, textvariable=browse_text,command=openfile,background="black",fg="white",font='sans 16 bold',height=1,width=8) #command=lambda:openfile()
browse_text.set("BROWSE")
browse_button.grid(column=1,row=2)

canvas = tk.Canvas(win, width=600,height=250)
canvas.grid(columnspan=3)

win.mainloop()