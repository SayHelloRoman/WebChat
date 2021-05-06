from tkinter import *
import websockets
from threading import Thread
import asyncio
import uuid

class Window(Tk):   
    def __init__(self):
        Tk.__init__(self)
        self.title('Chat')
        self.geometry("700x500")
        self.resizable(0, 0)

        self.id_ = str(uuid.uuid1())

        self.scrollbar = Scrollbar()
        self.text = Text(self, yscrollcommand=self.scrollbar.set, state='disabled')
        self.scrollbar.config(command=self.text.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text.pack()

        self.b_send = Button(text='send', command=self.send, width=20, height=2)
        self.b_send.place(x=500, y=430)

        self.ent = Entry(font=("Arial 30"))
        self.ent.place(x=10, y=430)

        Thread(target=asyncio.run, args=(self.get(),)).start()

        self.b_send.bind('<Button-1>', self.create_thread)
    
    async def get(self):
        async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
            while True:
                result = await websocket.recv()
                self.text.config(state='normal')
                self.text.insert(END, result + "\n")
                self.text.config(state='disabled')

    async def send(self):
        async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
            text = self.ent.get()
            await websocket.send(f"{self.id_}: {text}")
    
    def create_thread(self):
        Thread(target=asyncio.run, args=(self.send(),)).start()

Window().mainloop()