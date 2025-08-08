
# x = int(input("x:"))
# y = int(input("y:"))
# op = input("operator:")

# if(op =="+"):
#     print(x + y)

# elif(op =="-"):
#     print(x - y)

# elif(op =="*"):
#     print(x * y)

# elif(op =="/"):
#     print(x / y)

# else:
#     print("Invalide result")




# num1 = int(input("num1:"))
# num2 = int(input("num2:"))
# op = input("operator:")

# if(op =="+"):
#     print(num1+num2)

# elif(op =="-"):
#     print(num1-num2)

# elif(op =="*"):
#     print(num1*num2)

# elif(op =="/"):
#     print(num1/num2)

# else:
#     print("Invalid reselt")



# num1 = int(input("Enter A Number:"))
# num2 = int(input("Enter A number:"))
# op = input("operator:")


# if(op =="+"):
#     print(num1+num2)

# elif(op =="-"):
#     print(num1-num2)

# elif(op =="*"):
#     print(num1*num2)

# elif(op =="/"):
#     print(num1/num2)

# else:
#     print("Invalide reselt")            



# a = int(input("a:"))
# b = int(input("b:"))
# op = input("operator:")

# if op =='+':
#     print(a + b)

# elif op =='-':
#     print(a - b)

# elif op =='*':
#     print(a * b)

# elif op =='/':
#     print(a / b)

# else:
#     print("Invalid reselt")






# def addition(num1,num2):
#     print("Addition =", num1+num2)

# def subtraction(num1,num2):
#     print("Subtraction =", num1-num2)

# def multiplication(num1,num2):
#     print("Multiplication =", num1*num2)

# def division(num1,num2):
#         print("division =", num1/num2)

# while True:
     
#      print("1. Addition")
#      print("2. Subrtaction")
#      print("3. Multiplication")
#      print("4. Division")
#      print("5. Exit")
# choice = int(input("Enter My choice(1-5):"))

# if choice == 1:
#      num1 = int(input("Enter 1st Number"))
#      num2 = int(input("Enter 2nd Number:"))
#      addition(num1,num2)


# elif choice ==2:
#      num1 = int(input("Enter 1st Number:"))
#      num2 = int(input("Enter 2nd Number:"))
# subtraction(num1,num2)

# elif choice ==3:
# num1 = int(input("Enter 1st Number:"))
# num2 = int(input("Enter 2nd Number:"))
# multiplication(num1,num2)

# elif choice ==4:
# num1 = int(input("Enter 1st Number:"))
# num2 = int(input("Enter 2nd Number:"))

# if num2 ==0:
#      print("Infinity")

# else:
#      division(num1,num2)

# elif choice ==5:

# break

# else:

# print("Wrong choice")




# while True:
#     a = int(input("Enter A Number:"))
#     b = int(input("Enter A Number:"))
#     c = input("operator:")
    
#     if c=="+":
#         print(a+b)

#     elif c=="-":
#         print(a-b)

#     elif c=="*":
#         print(a*b)
        
#     elif c=="/":
#         print(a/b)

#     else:
#         print("Invalide result")




# def add(x,y):
#     return(x+y)

# def sub(x,y):
#     return(x-y)

# def multiply(x,y):
#     return(x*y)

# def divide(x,y):
#     return(x/y)

# while True:

#     print("operation.")
#     print("1.+")
#     print("2.-")
#     print("3.*")
#     print("4./")

# choice = input("Enter choice(1/2/3/4):")
# num1 = int(input("Enter 1st Number:"))
# num2 = int(input("Enter 2nd Number:"))

# if choice =="1":
#     print(num1+num2)

# elif choice =="2":
#     print(num1-num2)

# elif choice =="3":
#     print(num1*num2)

# elif choice =="4":
#     print(num1/num2)

# else:
#     print("Invalid result")


# import tkinter as tk

# def button_press(key):
#     global expression
#     expression += str(key)
#     equation.set(expression)

# def equals_press():
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression = ""
#     except:
#         equation.set("error")
#         expression = ""

# def clear_press():
#     global expression
#     expression = ""
#     equation.set("")

# # Main window setup
# root = tk.Tk()
# root.title("Simple Calculator")

# expression = ""
# equation = tk.StringVar()

# # Entry field for display
# entry_field = tk.Entry(root, textvariable=equation, justify='right')
# entry_field.grid(row=0, column=0, columnspan=4, ipadx=70, ipady=10)

# # Buttons
# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]

# row_val = 1
# col_val = 0
# for button_text in buttons:
#     if button_text == '=':
#         tk.Button(root, text=button_text, command=equals_press, height=2, width=8).grid(row=row_val, column=col_val)
#     else:
#         tk.Button(root, text=button_text, command=lambda key=button_text: button_press(key), height=2, width=8).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# tk.Button(root, text="Clear", command=clear_press, height=2, width=16).grid(row=row_val, column=0, columnspan=2)

# root.mainloop()




# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero!"
#     return x / y

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# while True:
#     choice = input("Enter choice(1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter numbers only.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#         elif choice == '4':
#             result = divide(num1, num2)
#             print(num1, "/", num2, "=", result)
#         break
#     else:
#         print("Invalid input. Please enter 1, 2, 3, or 4.")



# import tkinter as tk
# def button_press(key):
#     global expression
#     expression += str(key)
#     equation.set(expression)

# def equals_press():
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression = ""
#     except:
#         equation.set("error")
#         expression = ""

# def clear_press():
#     global expression
#     expression = ""
#     equation.set("")

# # Main window setup
# root = tk.Tk()
# root.title("Simple Calculator")

# expression = ""
# equation = tk.StringVar()

# # Entry field for display
# entry_field = tk.Entry(root, textvariable=equation, justify='right')
# entry_field.grid(row=0, column=0, columnspan=4, ipadx=70, ipady=10)

# # Buttons
# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]

# row_val = 1
# col_val = 0
# for button_text in buttons:
#     if button_text == '=':
#         tk.Button(root, text=button_text, command=equals_press, height=2, width=8).grid(row=row_val, column=col_val)
#     else:
#         tk.Button(root, text=button_text, command=lambda key=button_text: button_press(key), height=2, width=8).grid(row=row_val, column=col_val)
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# tk.Button(root, text="Clear", command=clear_press, height=2, width=16).grid(row=row_val, column=0, columnspan=2)

# root.mainloop





# import tkinter as tk
# def button_press(key):
#     global express
#     expression += str(key)
#     equation.set(expression)

# def equals_press():
 
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression =""

#     except:
#         equation.set("error")
#         expression = ""

# def clear_press():
#     global expression
#     expression = ""
#     equation.set("")


# # main window setup

# root = tk.Tk()
# root.title("simple calculator")
# expression =""
# equation = tk.StringVar()

# # Enter field for display.

# entry_field = tk.Entry(root, textvariable=equation,justify='right')
# entry_field.grid(row=0, column=0, columnspan=4, ipadx=70, ipady=10)

# #Buttons.

# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '_',
#     '0', '.', '=', '+' 
# ]

# row_val=1
# col_val=0
# for button_text in buttons:
#     if button_text=='=':
#         tk.button(root,text=button_text,command=equals_press,weight=2,width=8).grid(row=row_val,column=col_val)


#     else:
#         tk.Button(root,text=button_text,command=lambda key=button_text:button_press(key),height=2,width=8).grid(row_val,column=col_val)
#         col_val+=1
#         if col_val>3:
#             col_val=0
#             row_val+=1

#             tk.Button(root,text="clear", command=clear_press,height=2,width=16).grid(row=row_val,column=0,columnspan=2)

#             root.mainloop()
        




















































