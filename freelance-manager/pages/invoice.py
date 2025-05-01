# import streamlit as st 
# from fpdf import FPDF

# st.title("INVOICES")

# # Invoice class definition
# class Invoice:
#     def __init__(self, invoice_id, client, project, amount, status, due_date):
#         self.invoice_id = invoice_id
#         self.client = client
#         self.project = project
#         self.amount = amount
#         self.status = status
#         self.due_date = due_date

#     def generate_invoice_pdf(self):
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=13)
#         # Correct way to pass the text to the PDF
#         pdf.cell(200, 10, txt=f"Invoice No. : {self.invoice_id}", ln=True)
#         pdf.cell(200, 10, txt=f"Client: {self.client}", ln=True)
#         pdf.cell(200, 10, txt=f"Project: {self.project}", ln=True)
#         pdf.cell(200, 10, txt=f"Amount: {self.amount}", ln=True)
#         pdf.cell(200, 10, txt=f"Status: {self.status}", ln=True)
#         pdf.cell(200, 10, txt=f"Due Date: {self.due_date}", ln=True)
#         pdf.output("invoice.pdf")
