def comment_example():
    
    # comment example, recieves no arguments
    # it explains how to make a function header
    # and outputs or returns "Hello World!"
    print ("Hello World!")
    
def program2_1(): # apostrophe output
    
    print ('Kate Austen')
    print ('123 Full Cirlce Drive')
    print ('Asheville, NC 28899')
    
def program2_2(): # double quote output
    
    print ("Kate Austen")
    print ("123 Full Cirlce Drive")
    print ("Asheville, NC 28899")
    
def program2_3(): # display apostrophe
    
    print ("Don't fear!")
    print ("I'm here!")
    
def program2_4():
    
    print ('Your assignment is to read "Hamlet" by tomorrow.')
    
def program2_5(): # comment 1
    
    # This function displays a person's name and address
    print ('Kate Austen')
    print ('123 Full Cirlce Drive')
    print ('Asheville, NC 28899')
    
def program2_6():
    
    print ('Kate Austen') # Display the Name
    print ('123 Full Cirlce Drive') # Display the Address
    print ('Asheville, NC 28899') # Display the city, state, and ZIP
    
def program2_7(): # variable demo 1
    
    # This program demonstrates a variable
    room = 503
    
    print("I am staying in room number")
    print(room)
    
def program2_8(): # variable demo 2
    
    # Create two variables: top_speed and distance
    top_speed = 160
    distance = 300
    
    # Display the values referenced by the variables
    print("The top speed is")
    print(top_speed)   
    print("The distance traveled is")
    print(distance)
    
def program2_9():
    
    room = 503
    
    print("I am staying in room number", room)
    
def program2_10():
    
    value = 2.75
    
    print("I have", value, "in my account.")
    
    value = 99.95
    
    print("But now I have", value, "in my account!")
    
def program2_11():
    
    first_name = "Kathryn"
    last_name = "Marino"
    
    print(first_name, last_name)
    
def program2_12():
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    print("Hello", first_name, last_name)
    
def program2_13():
    
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    income = int(input("What is your income? "))
    
    print("Here is the data you entered: ")
    
    print("Name: ", name)
    print("Age: ", age)
    print("Income: ", income)
    
def program2_14():
    
    salary = 2500.00
    
    bonus = 1200.00
    
    pay = salary + bonus
    
    print("Your pay is ", pay)
    
def program2_15():
    
    original = float(input("What is the item's original price? "))
    
    discount = original * 0.2
    
    sale_price = original - discount
    
    print("Display Price: ", sale_price)
    
def program2_16():
    
    score_one = float(input("Enter the first test score: "))
    score_two = float(input("Enter the second test score: "))
    score_three = float(input("Enter the third test score: "))
    
    average = (score_one + score_two + score_three) / 3
    
    print("The average score is: ", average)
    
def program2_17():
    
    total_seconds = float(input("Enter the number of seconds: "))
    
    print("Here is the time in hours, minutes, and seconds: ")
    
    hours = total_seconds // 3600
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    
    print("Hours: ", hours)
    print("Minutes: ", minutes)
    print("Seconds: ", seconds)
    
def program2_18():
    
    desired_value = float(input("Enter the desired future value: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    years = float(input("Enter the number of years the money will grow: "))
    
    amount = desired_value / ((1 + interest_rate) ** years)
    
    print("You will need to deposit: $", format(amount, ',.2f'), sep='')
    
def program2_19():
    
    amount_due = 5000.00
    monthly_payment = amount_due / 12.0
    print("The monthly payment is ", monthly_payment)
    
def program2_20():
    
    amount_due = 5000.00
    monthly_payment = amount_due / 12.0
    print("The monthly payment is ", format(monthly_payment, '.2f'))
    
def program2_21():
    
    monthly_pay = 5000.00
    annual_pay = monthly_pay * 12
    print("Your annual pay is $", format(annual_pay, ',.2f'), sep='')
    
def program2_22():
    
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999
    
    print(format(num1, '7.2f'))
    print(format(num2, '7.2f'))
    print(format(num3, '7.2f'))
    print(format(num4, '7.2f'))
    print(format(num5, '7.2f'))
    print(format(num6, '7.2f'))