from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport

# asking user bill information
enter_bill_amount = float(input("Please enter the bill amount: "))
enter_period = input("Please enter period (for example March 2022): ")

# 1. Creates bill object with amount and period as parameters
bill = Bill(enter_bill_amount, enter_period)

# asking user for flatmates days in house and names
enter_first_flatmate_name = input("Please enter a name for the first flatmate: ")
enter_first_flatmate_days_in_house = int(input("Please enter days in house for the first flatmate: "))
enter_second_flatmate_name = input("Please enter a name for the second flatmate: ")
enter_second_flatmate_days_in_house = int(input("Please enter days in house for the second flatmate: "))

# 2. Creates two flatmates objects with name and days in house as parameters
first_flatmate = Flatmate(enter_first_flatmate_name, enter_first_flatmate_days_in_house)
second_flatmate = Flatmate(enter_second_flatmate_name, enter_second_flatmate_days_in_house)

# 3. Creates pdf_report object
pdf_report = PdfReport(f"{bill.period}.pdf")

# 4. Generates pdf file by the generate method from the PdfReport class
pdf_report.generate(bill, first_flatmate, second_flatmate)

print("PDF report generated!")
