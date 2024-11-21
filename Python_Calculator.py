import art
#Assigning different operation to functions
def add(n1, n2):
    return n1 + n2
def sub(n1 , n2):
    return n1 - n2
def mult(n1 , n2):
    return n1 * n2
def div(n1 , n2):
    return n1 / n2
#Assigning the functions to variables
addition = add
subtraction = sub
multiplication = mult
division = div
#Assigning the operations to the variables
Keys = {
    "+": addition ,
    "-": subtraction ,
    "*": multiplication ,
    "/": division ,
}
#Making the main function to the calculator
def calculator():
    print(art.logo) #Printing the logo from art.py
    n1 = float(input("Enter the first number: ")) #Taking from the user the first number
    while True:
        for symbol in Keys: 
            print(symbol) #Printing the symbols of the operations
        operation = input("Pick your operation: ") #Picking the operator that the user want to use
        n2 = float(input("Enter the second number: ")) #Entering the second number
        answer = Keys[operation](n1 , n2) #Assigning the inputs of the user in the variable answer
        print(f"{n1} {operation} {n2} = {answer}") #Printing the operation and the answer
        
        #Asking the user if he want to continue the calculation using the answer or he wants to start again
        choice = input("Do you want to continue your calculation using the same number?\n").lower()
         
        if choice == "yes": #If the user said yes he will continue the calculation using the answer
            n1 = answer
        else: #If he said no the user will do another calculation using different numbers
            print("\n" * 20)
            calculator()
            
calculator() #Calling the fucntion