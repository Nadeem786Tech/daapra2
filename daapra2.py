Aim: Write a python program to show stack operations using match-case.

Algorithm

1.   Start.
2.   Create an empty stack.
3.   Display the menu:
o Push
o Pop
o Peek
o Display
o Exit
4.   Accept the user's choice.
5.   Use the Match-Case statement:
o Case 1: Input an element and insert it into the stack using append().
o Case 2: If the stack is empty, display "Stack Underflow"; otherwise, remove the top
element using pop().
o Case 3: If the stack is empty, display "Stack is Empty"; otherwise, display the top
element.
o	Case 4: If the stack is empty, display "Stack is Empty"; otherwise, display all the elements of the stack.
o Case 5: Exit the program.
o Default Case: Display "Invalid Choice".
6.   Repeat the menu until the user selects Exit.
7.   Stop. Program stack = []
while True:
print("\n----- STACK MENU -----")
print("1. Push") print("2. Pop") print("3. Peek") print("4. Display") print("5. Exit")

choice = int(input("Enter your choice: "))

match choice:

case 1:
item = input("Enter element: ")
stack.append(item)
print("Element Inserted")

case 2:
if len(stack) == 0:
print("Stack Underflow")
else:
print("Deleted Element =", stack.pop())

case 3:
if len(stack) == 0: 
print("Stack is Empty")
else:
print("Top Element =", stack[-1])

case 4:
if len(stack) == 0:
print("Stack is Empty")
else:
print("Stack =", stack)

case 5:
print("Program Ended")
break

case _:
print("Invalid Choice")



Output

----- STACK MENU -----
1. Push
2. Pop
3. Peek
4. Display
5. Exit

Enter your choice: 1
Enter element: 10
Element Inserted

Enter your choice: 1
Enter element: 20
Element Inserted

Enter your choice: 4
Stack = ['10', '20']

Enter your choice: 3
Top Element = 20

Enter your choice: 2
Deleted Element = 20

Enter your choice: 4
Stack = ['10']

Enter your choice: 5
Program Ended
