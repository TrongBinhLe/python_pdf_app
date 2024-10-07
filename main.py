from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation= "P", unit= "mm", format = "A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
      # Set the header
      pdf.add_page()
      pdf.set_font(family= "Times", style= "B", size = 24)
      pdf.set_text_color(100,100,100)
      pdf.cell(w=0, h=12, txt= row["Topic"], align = 'L', ln=1)
      pdf.line(10, 22, 200, 22)

      # Set the footer
      pdf.ln(238)
      pdf.set_font(family= "Times", style= "I", size = 8)
      pdf.set_text_color(80, 80, 80)
      pdf.cell(w=0, h=10, txt= row["Topic"], align = 'R')

      
      for i in range(row["Pages"]-1):
            pdf.add_page()

            # Set the footer
            pdf.ln(250)
            pdf.set_font(family= "Times", style= "I", size = 8)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=0, h=10, txt= row["Topic"], align = 'R')

pdf.output("output.pdf")

