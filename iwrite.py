import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import pyttsx3
from gtts import gTTS
from playsound import playsound
import tempfile
align = "left"
def read_text(text_edit):
    engine = pyttsx3.init(driverName = "sapi5")
    engine.setProperty("rate",150)
    engine.setProperty("volume",1.0)
    content = text_edit.get("1.0","end").strip()
    if content:
        engine.say(content)
        engine.runAndWait()
#         tts = gTTS(text=content, lang = "ar")
#         with tempfile.NamedTemporaryFile(delete=False, suffix =".mp3") as fp:
#             tts.save(fp.name)
#             playsound(fp.name)
def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files","*.txt")])
    
    if not filepath:
        return
    text_edit.delete(1.0,tk.END)
    with open(filepath,"r") as k:
        content = k.read()
        text_edit.insert(tk.END,content)
    window.title(f"{filepath}")
def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files","*.txt")])
    
    if not filepath:
        return
    with open(filepath,"w") as k:
        content = text_edit.get(1.0,tk.END)
        k.write(content)
    window.title(f"{filepath}")
def alg(event):
    text = event.widget
    content = text.get("1.0",tk.END).strip()
    if not content:
        return
    first = content[0]
    
    text_edit.tag_remove("left","1.0",tk.END)
    text_edit.tag_remove("right","1.0",tk.END)
    if "\u0600" <= first <= "\u06FF":
        #align = "left"
        text_edit.tag_remove("left","1.0",tk.END)
        text_edit.tag_configure("right",justify = "right")
        text_edit.tag_add("right","1.0",tk.END)
    else:
        #align == "right"
        text_edit.tag_remove("right","1.0",tk.END)
        text_edit.tag_configure("left",justify = "left")
        text_edit.tag_add("left","1.0",tk.END)
def main():
    window = tk.Tk()
    window.title("IWrite")
    window.iconbitmap("favicon.ico")
    window.rowconfigure(0,minsize = 400)
    window.columnconfigure(1,minsize = 500)
    text_edit = tk.Text(window,font = "Arial 10")
    text_edit.grid(row = 0,column = 1)
    text_edit.bind("<Control-r>",alg)
    frame = tk.Frame(window, relief=tk.RAISED,bd=2)
    save_button = tk.Button(frame, text = "Save",command = lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text = "Open",command = lambda: open_file(window, text_edit))
    say_button = tk.Button(frame, text = "Read",command = lambda: read_text(text_edit))
    save_button.grid(row = 0,column = 0,padx = 7,pady = 7)
    open_button.grid(row = 1,column = 0,padx= 7,pady = 7)
    say_button.grid(row = 2,column = 0,padx= 7,pady = 7)
    frame.grid(row = 0 ,column = 0, sticky = "ns")
    window.bind("<Control-s>",lambda x: save_file(window, text_edit))
    window.bind("<Control-o>",lambda x: open_file(window, text_edit))
    window.mainloop()
main()