from tkinter import ttk
import tkinter

buttonsToGen = 9
def calculate(num1, num2, sign):
    if sign == "+":
        return int(num1) + int(num2)
    elif sign == "-":
        return int(num1) - int(num2)
    elif sign == "*":
        return int(num1) * int(num2)
    else:
        return int(num1) / int(num2)


def buttonPressed(buttonNum):
    displayBox.insert(index=len(displayBox.get()), string=buttonNum)

def clear():
    displayBox.delete(0, "end")

def equalButtonPressed():
    num1 = ""
    num2 = ""
    sign = ""

    for x in displayBox.get():
        if x.isdigit() and sign == "":
            num1 += x

        elif x.isdigit() and sign != "":
            num2 += x

        elif sign == "":
            sign = x

        else:
            None


    print(calculate(num1, num2, sign))


    displayBox.delete(0, "end")

    if str(calculate(num1, num2, sign) != "None"):
        displayBox.insert(index=len(displayBox.get()), string=(str(calculate(num1, num2, sign))))

    else:
        displayBox.delete(0, "end")
        displayBox.insert(index=len(displayBox.get()), string="Error")




root = tkinter.Tk()



root.title("Calculator")
root.geometry("450x570")
root.resizable(False, False)
root.iconbitmap("CalculatorIcon.ico")


displayBox = ttk.Entry(state="normal", width=10, justify="right", font=("Ariel", 50, 'bold'))
displayBox.place(x=50, y=0)



#Buttons
button0 = ttk.Button(root, text="0", command=lambda : buttonPressed(0), width=10, padding=20)
button0.place(x=50, y=100)

button1 = ttk.Button(root, text="1", command=lambda : buttonPressed(1), width=10, padding=20)
button1.place(x=170, y=100)

button2 = ttk.Button(root, text="2", command=lambda : buttonPressed(2), width=10, padding=20)
button2.place(x=290, y=100)

button3 = ttk.Button(root, text="3", command=lambda : buttonPressed(3), width=10, padding=20)
button3.place(x=50, y=170)

button4 = ttk.Button(root, text="4", command=lambda : buttonPressed(4), width=10, padding=20)
button4.place(x=170, y=170)

button5 = ttk.Button(root, text="5", command=lambda : buttonPressed(5), width=10, padding=20)
button5.place(x=290, y=170)

button6 = ttk.Button(root, text="6", command=lambda : buttonPressed(6), width=10, padding=20)
button6.place(x=50, y=240)

button7 = ttk.Button(root, text="7", command=lambda : buttonPressed(7), width=10, padding=20)
button7.place(x=170, y=240)

button8 = ttk.Button(root, text="8", command=lambda : buttonPressed(8), width=10, padding=20)
button8.place(x=290, y=240)

button9 = ttk.Button(root, text="9", command=lambda : buttonPressed(9), width=10, padding=20)
button9.place(x=50, y=310)



addButton = ttk.Button(root, text="+", command=lambda : buttonPressed("+"), width=10, padding=20)
addButton.place(x=50, y=380)

subtractButton = ttk.Button(root, text="-", command=lambda : buttonPressed("-"), width=10, padding=20)
subtractButton.place(x=170, y=380)

multiplyButton = ttk.Button(root, text="*", command=lambda : buttonPressed("*"), width=10, padding=20)
multiplyButton.place(x=290, y=380)

divideButton = ttk.Button(root, text="/", command=lambda : buttonPressed("/"), width=10, padding=20)
divideButton.place(x=290, y=310)

clear = ttk.Button(root, text="C", command=clear, width=10, padding=20)
clear.place(x=170, y=310)

equalButton = ttk.Button(root, text="=", command=equalButtonPressed, width=10, padding=20)
equalButton.place(x=50, y=450)



root.mainloop()

