import turtle

# personal info function
# input - none
# output - name, address, phone number, and projected major
def personal_info():
    
    print('Niklaus Schrader')
    print('306 South Firefly Street, Wichita, Kansas 67235')
    print('316-409-9022')
    print('Computer Science')

# total purchase function
# input - none
# output - subtotal, tax, and total
def total_purchase():
    
    # constants
    SALES_TAX = 0.07
    
    # variables
    subtotal = 0.0
    tax = 0
    total = 0
    
    # ask the user for the price of each of the five items
    subtotal += int(input('Please enter the price of your first item: '))
    subtotal += int(input('Please enter the price of your second item: '))
    subtotal += int(input('Please enter the price of your third item: '))
    subtotal += int(input('Please enter the price of your fourth item: '))
    subtotal += int(input('Please enter the price of your fifth item: '))
    
    # calculate tax and total
    tax = subtotal * SALES_TAX
    
    total = tax + subtotal
    
    # blank line
    print("")
    
    # print the subtotal, tax, and total
    print('Subtotal:    $   {:,.2f}'.format(subtotal))
    print('Tax:         $  ', tax)
    print('Total:       $  ', total)

# distance traveled function
# input - none
# output - the distance the car will travel in 6, 10, and 15 hours
def distance_traveled():
    
    HOUR_SIX = 6
    HOUR_TEN = 10
    HOUR_FIFTEEN = 15
    
    speed = float(input("How fast are you driving? "))
    
    # 6 hours
    miles = HOUR_SIX * speed
    print("At 60 miles per hour you will travel", miles, "miles in 6 hours")
    
    # 10 hours
    miles = HOUR_TEN * speed
    print("At 60 miles per hour you will travel", miles, "miles in 10 hours")
    
    # 15 hours
    miles = HOUR_FIFTEEN * speed
    print("At 60 miles per hour you will travel", miles, "miles in 15 hours")
    
# sales tax function
# input - none
# output - prints out the tax and total of a sale
def sales_tax():
    
    # constants
    STATE_TAX_AMOUNT = 0.05
    COUNTY_TAX_AMOUNT = 0.025
    
    # ask the user for the sale amount
    sale_amount = float(input('Enter the sale amount: '))
    
    # calculate 5% state tax, 2.5% county tax, total tax, and total sale
    state_tax = sale_amount * STATE_TAX_AMOUNT
    
    county_tax = sale_amount * COUNTY_TAX_AMOUNT
    
    total_tax = state_tax + county_tax
    
    total_sale = sale_amount + total_tax
    
    # print out the gathered information
    print('Your purchase price was:     $     ', total_sale, sep='')
    print('Your state tax amount is:    $     ', state_tax, sep='')
    print('Your county tax amount is:   $     ', county_tax, sep='')
    print('Your total tax is:           $     ', total_tax, sep='')
    print('Your total sale is:          $     ', total_sale, sep='')
    
# tip tax total function
# input - none
# output - prints out the tip, tax, and total amount of a sale
def tip_tax_total():
    
    # constants
    TIP_AMOUNT = 0.18
    TAX_AMOUNT = 0.07
    
    # ask the user to input the sale amount
    sale = float(input('Please enter the sale amount: '))
    
    # calculate the tip amount, sales tax amount, and total bill
    tip = sale * TIP_AMOUNT
    tax = sale * TAX_AMOUNT
    total = sale + tip + tax
    
    # print the sale amount, tip amount, sales tax amount, and total bill
    print('The sale was:                $   ', format(sale, '7.2f'), sep='')
    print('The tip amount is:           $   ', format(tip, '7.2f'), sep='')
    print('The sales tax amount is:     $   ', format(tax, '7.2f'), sep='')
    print('The total bill is:           $   ', format(total, '7.2f'), sep='')
    
# temperature converter
# input - none
# output - inputed temperature converted to fahrenheit
def temp_converter():
    
    # constants
    ADDITIVE_32 = 32
    FRACTION_ADDITIVE = (9/5)
    
    # ask the user to enter the Celcius amount
    original_temp = float(input('Please enter the degrees Celcius: '))
    
    # calculate the temp in Fahrenheit
    new_temp = (FRACTION_ADDITIVE * original_temp) + ADDITIVE_32
    
    # print out the temperature in Fahrenheit
    print(original_temp, 'degrees celsius is', new_temp, 'degrees Fahrenheit.')

# cookie monster function
# input - none
# output - how many ingredients are needed for how many cookies the user wants to make
def cookie_monster():
    
    # constants
    SUGAR_MULT = 12
    BUTTER_MULT = 8
    FLOUR_MULT = 22
    
    # ask the user how many cookies they want to make
    num_of_cookies = int(input('How many cookies do you want to make? '))
    
    # header statement
    print('For', num_of_cookies, 'cookies you will need:')
    
    # divide the number of cookies into how many batches of 24 there are
    batches = num_of_cookies / 24
    
    # multiply the batch amount by each amount of ingredient to find the amount needed of each ingredient
    sugar_amount = batches * SUGAR_MULT
    butter_amount = batches * BUTTER_MULT
    flour_amount = batches * FLOUR_MULT
    
    # print the amounts converted to cups and ounces
    print((sugar_amount // 8), 'cup(s)', format(sugar_amount % 8, '.0f'), 'ounces of sugar.')
    print((butter_amount // 8), 'cup(s)', format(butter_amount % 8, '.0f'), 'ounces of butter.')
    print((flour_amount // 8), 'cup(s)', format(flour_amount % 8, '.0f'), 'ounces of flour.')
    
# class demographics function
# input - none
# output - the classes demographics
def class_demographics():
    
    # constants
    PERCENT_MULT = 100
    
    # get the number of males and females in the class from the user
    num_fem = int(input('Enter the number of females: '))
    num_male = int(input('Enter the number of males: '))
    
    # calculate total number of students
    total = num_fem + num_male
    
    # find the decimal percentage
    fem_perc = num_fem / total
    male_perc = num_male / total
    
    # print out the percentages non decimal form
    print('The class consists of', int(PERCENT_MULT * fem_perc), '% females and', int(PERCENT_MULT * male_perc), '% males.')
    
def tortuga1():
    
    def reset():
        turtle.penup()
        turtle.goto(0, 0)
    
    turtle.setup(500, 500)
    turtle.hideturtle()
    
    reset() 
    
    turtle.pendown()
    turtle.pensize(3)
    turtle.goto(-100, 0)
    turtle.penup()
    turtle.goto(-140, -25)
    turtle.write('W', font=("Calibri", 30, "bold"))
    
    reset()
    
    turtle.pendown()
    turtle.goto(100, 0)
    turtle.penup()
    turtle.goto(110, -24)
    turtle.write('E', font=("Calibri", 30, "bold"))
    
    reset()
    
    turtle.pendown()
    turtle.goto(0, 100)
    turtle.penup()
    turtle.goto(-10, 100)
    turtle.write('N', font=("Calibri", 30, "bold"))
    
    reset()
    
    turtle.pendown()
    turtle.goto(0, -100)
    turtle.penup()
    turtle.goto(-8, -145)
    turtle.write('S', font=("Calibri", 30, "bold"))
    
    reset()
    
    turtle.pensize(2)
    
    turtle.pendown()
    turtle.goto(-50, 50)
    
    reset()
    
    turtle.pendown()
    turtle.goto(50, 50)
    
    reset()
    
    turtle.pendown()
    turtle.goto(50, -50)
    
    reset()
    
    turtle.pendown()
    turtle.goto(-50, -50)
    
#tortuga1()

def tortuga2():
    
    turtle.setup(500, 500)
    turtle.hideturtle()
    turtle.penup()
    
    turtle.begin_fill()
    turtle.fillcolor('blue')
    
    turtle.goto(-100,0)
    
    turtle.pendown()
    turtle.goto(-100,125)
    
    turtle.goto(0,125)
    
    turtle.goto(0,0)
    
    turtle.goto(-100,0)
    
    turtle.goto(-100,125)
    
    turtle.goto(-50, 175)
    
    turtle.goto(0,125)
    
    turtle.goto(115, 100)
    
    turtle.goto(115, 25)
    
    turtle.goto(0,0)
    
    turtle.penup()
    turtle.goto(-50, 175)
    turtle.pendown()
    
    turtle.goto(100, 125)
    
    turtle.goto(115, 100)
    
    turtle.end_fill()
    
    
tortuga2()
