from fpdf import FPDF


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, flatmate1, flatmate2):
        flatmate1_pay = flatmate1.pays(bill, flatmate2)
        flatmate2_pay = flatmate2.pays(bill, flatmate1)

        # 1. Creates FPDF object
        pdf_report = FPDF(orientation="P", unit="pt", format="A4")

        # 2. Adding page
        pdf_report.add_page()

        # 3. Adding image
        pdf_report.image(name="files/house.png", w=30, h=30)

        # 4. Setting font and creating the heading cell
        pdf_report.set_font(family="Times", size=24, style="B")
        pdf_report.cell(w=0, h=100, txt="Flatmate Bill", align="C", ln=1)

        # 5. Setting font and creating cells for period
        pdf_report.set_font(family="Times", size=18, style="B")
        pdf_report.cell(w=150, h=40, txt="Period: ")
        pdf_report.cell(w=150, h=40, txt=bill.period, ln=1)

        # 6. Creates cells for payment share information
        pdf_report.set_font(family="Times", size=14)
        pdf_report.cell(w=150, h=40, txt=flatmate1.name)
        pdf_report.cell(w=150, h=40, txt=flatmate2.name, ln=1)

        pdf_report.cell(w=150, h=40, txt=f"{flatmate1_pay:.2f}")
        pdf_report.cell(w=150, h=40, txt=f"{flatmate2_pay:.2f}")

        pdf_report.output(self.filename)
