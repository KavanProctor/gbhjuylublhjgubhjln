import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation #makes the variable global
    calculation += str(symbol) #turns anything into a string
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def do_calculations():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except: #this is just for any error case not very specific
        clear()
        text_result.insert(1.0, "error")
        pass

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk() #create the object
#anything below this is all the dimensions and dimensions

root.geometry("300x275")# shape of the box
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24, "bold"))#where the result will show at the top
text_result.grid(row=1, columnspan=5)

#creates the buttons
btn_1 = tk.Button(root, text=1, command=lambda:add_to_calculation(1), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_1.grid(row=2, column=1) #tells me where to place the button on the grid that we have
btn_2 = tk.Button(root, text=2, command=lambda:add_to_calculation(2), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_2.grid(row=2, column=2) #tells me where to place the button on the grid that we have
btn_3 = tk.Button(root, text=3, command=lambda:add_to_calculation(3), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_3.grid(row=2, column=3) #tells me where to place the button on the grid that we have
btn_4 = tk.Button(root, text=4, command=lambda:add_to_calculation(4), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_4.grid(row=3, column=1) #tells me where to place the button on the grid that we have
btn_5 = tk.Button(root, text=5, command=lambda:add_to_calculation(5), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_5.grid(row=3, column=2) #tells me where to place the button on the grid that we have
btn_6 = tk.Button(root, text=6, command=lambda:add_to_calculation(6), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_6.grid(row=3, column=3) #tells me where to place the button on the grid that we have
btn_7 = tk.Button(root, text=7, command=lambda:add_to_calculation(7), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_7.grid(row=4, column=1) #tells me where to place the button on the grid that we have
btn_8 = tk.Button(root, text=8, command=lambda:add_to_calculation(8), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_8.grid(row=4, column=2) #tells me where to place the button on the grid that we have
btn_9 = tk.Button(root, text=9, command=lambda:add_to_calculation(9), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_9.grid(row=4, column=3) #tells me where to place the button on the grid that we have
btn_0 = tk.Button(root, text=0, command=lambda:add_to_calculation(0), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_0.grid(row=5, column=2) #tells me where to place the button on the grid that we have

btn_plus = tk.Button(root, text="+", command=lambda:add_to_calculation("+"), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_plus.grid(row=2, column=4) #tells me where to place the button on the grid that we have
btn_minus = tk.Button(root, text="-", command=lambda:add_to_calculation("-"), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_minus.grid(row=3, column=4) #tells me where to place the button on the grid that we have
btn_mult = tk.Button(root, text="*", command=lambda:add_to_calculation("*"), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_mult.grid(row=4, column=4) #tells me where to place the button on the grid that we have
btn_div = tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_div.grid(row=5, column=4) #tells me where to place the button on the grid that we have

btn_openBrackets = tk.Button(root, text="(", command=lambda:add_to_calculation("("), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_openBrackets.grid(row=5, column=1) #tells me where to place the button on the grid that we have
btn_closeBrackets = tk.Button(root, text=")", command=lambda:add_to_calculation(")"), width=5, font=("Arial",14)) #lambda expression is needed otherwise it will call the function and not work
btn_closeBrackets.grid(row=5, column=3) #tells me where to place the button on the grid that we have

btn_clear = tk.Button(root, text="CE", command=clear, width=11, font=("Arial",14))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_equal = tk.Button(root, text="=", command=do_calculations, width=11, font=("Arial",14))
btn_equal.grid(row=6, column=3, columnspan=2)

root.mainloop()#run the loop