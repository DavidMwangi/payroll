def prompt():#prompts user for their details

    name = str(input("Full Name >> "))

    hoursWorked = float(input("Hours Worked >> "))

    payRate = float(input("Pay Rate ($/hr) >> "))

    details = (name, hoursWorked, payRate)

    return details


