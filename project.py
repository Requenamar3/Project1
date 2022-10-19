# declare variables needed
flat_tax_rate = float (0.20)
standard_deduction = float (10000.0)

#to get the output
gross_income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

#to calculate the total dependents deduction

dependents_deduction = 3000 * dependents

#to calculate the income tax, I deducted standard and dependents amounts from gross income and multiply by tax rate
income_tax = (gross_income - standard_deduction -dependents_deduction) * flat_tax_rate

print("The income tax is" +" " "${:.1f}".format(income_tax))


