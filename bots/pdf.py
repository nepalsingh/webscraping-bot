from fpdf import FPDF

def create_pdf(title, content,image):
    pdf = FPDF(orientation='portrait',unit='pt', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, title)
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 5, content)
    pdf.image(image, x=500, w=40 , h=30)
    pdf.output(f'files/{title}.pdf', 'F')

if __name__ == '__main__':
    create_pdf('Hello', 'This is a test', 'files/tiger.jpeg')