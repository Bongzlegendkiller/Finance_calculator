import math
# Start
# prompt user to print line
# prompt user to print statements
# prompt user to print line

print("--------------------------------------------------------------------------------------------------------------")
print("Investment - to calculate the amount of interest you will earn on your investment")

print("Bond - to calculate the amount you have to pay on a home loan")

print("Enter either - 'investment' or bond from the menu above to proceed: ")
print("---------------------------------------------------------------------------------------------------------------")
# prompt user to declare and store variable and choose investment type
investment_type = str(input("Enter investment type: "))
# prompt user If investment type is equal_type == Investment print investment variables
if investment_type == "Investment":
    print("Thank you. You have chosen investment.")
    # prompt user to declare and store all investment variables
    amount = float(input("How much do you want to deposit?: R "))
    rate = float(input("Please enter interest rate % : "))
    num_of_years = float(input("Please enter number of years: "))
    # prompt user to input interest type
    interest = str(input("Do you want Simple or Compound interest?: "))
    # prompt user if interest is == Simple interest calculate and print output
    if interest == "Simple":
        # prompt user to use "Simple interest" formular : A = P( 1 + r * t)
        result = amount * (1 + (rate / 100) * num_of_years)
        print("Total simple interest rate =  R", str(result))
        print("---------------------------------------------------------------")
        # prompt user if interest is == Compound interest calculate and print output
    elif interest == "Compound":
        # "Compound interest" formular : A = P(1+r)^t
        result = amount * math.pow((1 + rate / 100), num_of_years)
        round_result = round(result, 2)
        print("Total compound interest rate =  R", str(round_result))
        print("------------------------------------------------------------------")
        # prompt user if investment_type == Bond calculate and print output
elif investment_type == "Bond":
    print("Thank you.You have chosen bond.")
    present_value = float(input("Please enter value of house: R "))
    i = float(input("Please enter interest rate % : "))
    num_months = float(input("Please enter amount of months: "))
# prompt user to use "Bond repayment" formular : (i * P) / (1 - (1 + i) ** (-n))
    result = ((i / 100 / 12) * present_value) / (1 - (1 + (i / 100 / 12)) ** (- num_months))
    bond_result = round(result, 2)
    print("Total money to be repaid =  R", str(bond_result))
    print("----------------------------------------------------------------")
# prompt user to print "Please enter investment type." if user has not entered anything.
# End
else:
    print("Please enter investment type.")
