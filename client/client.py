from tkinter import *
from websocket import create_connection
from threading import Thread
import asyncio
import uuid

class Window(Tk):   
    def __init__(self):
        super().__init__()
        
        self.ws = create_connection("ws://127.0.0.1:8000/ws")

        style_border = {"bd": 2, "relief":"groove"}

        self.title('Chat')
        self.geometry("700x500")
        self.resizable(0, 0)

        self.id_ = str(uuid.uuid1())

        self.scrollbar = Scrollbar()
        self.text = Text(self, yscrollcommand=self.scrollbar.set, state='disabled', **style_border)
        self.scrollbar.config(command=self.text.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text.pack()

        self.b_send = Button(text='send', command=self.send, width=20, height=2, **style_border)
        self.b_send.place(x=500, y=430)

        self.ent = Entry(font=("Arial 30"), **style_border)
        self.ent.place(x=10, y=430)

        Thread(target=self.get).start()

    def get(self):
        while True:
            result = self.ws.recv()
            self.text.config(state='normal')
            self.text.insert(END, result + "\n")
            self.text.config(state='disabled')

    def send(self):
        text = self.ent.get()
        self.ent.delete(0, 'end')
        self.ws.send(f"{self.id_}: {text}")

Window().mainloop()