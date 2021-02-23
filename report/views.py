from fpdf import FPDF
from django.http import FileResponse

"""
Redéfinition du header et du footer 
"""


class PDF(FPDF):
    def header(self):
        # Logo
        self.image("/portail_web_chu/report/static/report/logo.jpg", 10, 5, 33)
        # helvetica bold 15
        self.set_font('helvetica', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(60, 10, 'Recherche Clinique', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # helvetica italic 8
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def create_report(request, recherche_id):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1, 41):
        pdf.cell(50, 10, 'TEST' + str(i), 0, 1, "C")
    pdf.output('test1.pdf')

    return FileResponse(open("/portail_web_chu/test1.pdf"), "rb")
