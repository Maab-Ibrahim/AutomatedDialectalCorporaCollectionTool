from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(fill=X, side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

   def var_states():
       print(" return" % (var1.get(), var2.get()))
if __name__ == '__main__':
    window = Tk()
    window.title("Arabic Dialects Corpora")
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Corpus Collection')
    tab_control.add(tab2, text='Annotations')
    tab_control.add(tab3, text='Dataset')
    # dialects list
    cntr = ["Egypt", "Sudan", "Morocco", "Tunisia", "Libya", "Algeria", "Mauritania",
            "Yemen", "Iraq", "Oman", "Saudi Arabia", "UAE", "Qatar", "Kuwait", "Bahrain",
            "Syria", "Palesine", "Lebanon", "Jordan"]
    lng = Checkbar(tab1, cntr, side=LEFT)
    sb = Scrollbar(orient="vertical")
    text = Text(tab1, width=70, height=20, yscrollcommand=sb.set)
    sb.config(command=text.yview)
    sb.pack(side=RIGHT, fill=Y)
    text.pack(side="top", fill=X, expand=True)
    # countries list
    var = []
    i = 0
    for word in cntr:
        var.append(IntVar())
        cb = Checkbutton(window, text=word, height=1, width=20, variable=var[i], padx=0, pady=0, bd=0)
        i = i + 1
        text.window_create(END, window=cb)
        text.insert(END, "\n")

    # Streaming countries area
    listbox = Listbox(tab1, height=10, width=30)
    listbox.pack(fill=X, side=LEFT)

    # tweets in textarea
    displayText = Text(tab1, height=10, width=30)
    displayText.pack(fill=X, side=RIGHT)
    displayText.configure(state='disabled')
    scrolledtext.ScrolledText(tab1, width=20, height=40)


    # streaming function
    def start_streaming():

        n = 0
        for i in cntr:
            displayText.configure(state='normal')
            if var[n].get() == 1:
                listbox.insert(END, ['Streaming tweets from : %s ....\n ' % i])
                displayText.insert(INSERT, "tweets from %s ....\n" % i)
            n = n + 1
        displayText.configure(state='disabled')


    Button(tab1, text='Collect', command=start_streaming).pack(side=BOTTOM, fill=X)
    Button(tab1, text='Quit', command=window.quit).pack(side=BOTTOM, fill=X)



    lbl2 = Label(tab2, text='label2')

    lbl2.pack(side=LEFT)

    tab_control.pack(expand=1, fill='both')

    window.mainloop()
