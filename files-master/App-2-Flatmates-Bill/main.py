from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport

# 1. Creates bill object with amount and period as parameters
bill = Bill(120, "March 2022")

# 2. Creates two flatmates objects with name and days in house as parameters
first_flatmate = Flatmate("Marian", 25)
second_flatmate = Flatmate("Monika", 20)

# 3. Creates pdf_report object
pdf_report = PdfReport("bill.pdf")

# 4. Generates pdf file by the generate method from the PdfReport class
pdf_report.generate(bill, first_flatmate, second_flatmate)
