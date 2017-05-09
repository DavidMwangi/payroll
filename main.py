def prompt():#prompts user for their details

    name = str(input("Full Name >> "))

    def hours():

        hoursWorked = float(input("Hours Worked >> "))

        if hoursWorked > 80:

            print("Invalid Entry!")

            hours()

        else:

            return hoursWorked

    hoursWorked = hours()

    def rate():

        payRate = float(input("Pay Rate ($/hr) >> "))

        if payRate > 10 and payRate < 75:

            return payRate

        else:

            rate()

    payRate = rate()

    details = (name, hoursWorked, payRate)

    return details

print(prompt())


