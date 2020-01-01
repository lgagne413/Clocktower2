import tkinter as tk
import clocktower

LARGE_FONT= ("Verdana", 12)


class clocktowerapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title = 'Clocktower'
        self.frames = {}
        self.clock = clocktower.clock()
        self.data = {'enintext' : tk.StringVar() ,'enouttext' : tk.StringVar(),
                    "deintext": tk.StringVar() , "deouttext" : tk.StringVar()}
        for F in PAGES:

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, container):

        frame = self.frames[container]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Would you like to encode or decode a clocktower cipher?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Encode",
                            command=lambda: controller.show_frame(EncodePage))
        button.pack()

        button2 = tk.Button(self, text="Decode",
                            command=lambda: controller.show_frame(DecodePage))
        button2.pack()


class EncodePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Please type or copy and paste the text you would like to have encoded.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        text = tk.Text(self, width=40, height=20)
        text.pack(pady=10,padx=10)

        button = tk.Button(self, text="Encode",
                                command=lambda: self.process(text.get('1.0','end')))
        button.pack()

    def process(self,text):
        self.controller.data["enintext"].set(text)
        self.controller.data['enouttext'].set(self.controller.clock.encode(text))
        self.controller.show_frame(EncodedPage)
        return

class DecodePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Please type or copy and paste the text you would like to have decoded.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        text = tk.Text(self, width=40, height=20)
        text.pack(pady=10,padx=10)

        button = tk.Button(self, text="Decode",
                            command=lambda: self.process(text.get('1.0','end')))
        button.pack()
    def process(self,text):
        self.controller.data["deintext"].set(text)
        self.controller.data['deouttext'].set(self.controller.clock.decode(text))
        self.controller.show_frame(DecodedPage)
        return

class EncodedPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Following is your encoded message.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Reveal",
                            command=lambda: self.reveal(text))
        button1.pack()
        text = tk.Text(self, width=40, height=20)
        text.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()

    def reveal(self,text):
        text.insert('1.0',self.controller.data['enouttext'].get())
        return

class DecodedPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Following is your decoded message.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Reveal",
                            command=lambda: self.reveal(text))
        button1.pack()
        text = tk.Text(self, width=40, height=20)
        text.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()

    def reveal(self,text):
        text.insert('1.0',self.controller.data['deouttext'].get())
        return

PAGES = (StartPage, EncodePage,DecodePage,EncodedPage,DecodedPage)
app = clocktowerapp()
app.mainloop()
