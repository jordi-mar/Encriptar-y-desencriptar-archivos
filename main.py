import customtkinter

print('hola')
app = customtkinter.CTk()
app.geometry("500x200")
customtkinter.set_appearance_mode('system')

def button_event():
    print('button pressed')

button = customtkinter.CTkButton(app, text='click aqui', width=140, height=28, command=button_event, anchor= 'center')
button.place(x=90, y=70)

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(app, width=140, height=28, from_=0, to=100, command=slider_event)

slider.place(x=10, y=10)

textbox = customtkinter.CTkTextbox(app, width=200, height=200)

textbox.place(x=10, y=10)

textbox.insert('0.0', 'new text to insert')  # insert at line 0 character 0
text = textbox.get('0.0', 'end')  # get text from line 0 character 0 till the end
textbox.delete('0.0', 'end')  # delete all text
textbox.configure(state='disabled')  # configure textbox to be read-only

app.mainloop()