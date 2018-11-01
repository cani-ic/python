from tkinter import Label
widget=Label(None,text='Hello world!!')
# widget=pack()  #Error!!!
widget.pack()   #pack() is a method ,use "." to call it
# widget=main.loop() #Error
widget.mainloop() #mainloop() is a method
