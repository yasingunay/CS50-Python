from fpdf import FPDF

# var LMARGIN: Left page margin (start of printable area)
# var NEXT: top of next line (bottom of current text)
class PDF(FPDF):
    def print_title(self):
        self.set_font("helvetica", "B",  50)
        self.cell(0, 60, 'CS50 Shirtificate', new_x ='LMARGIN', new_y= 'NEXT', align ="C")

    # var epw: Effective page width: the page width minus its horizontal margins.
    def render_image(self):
        self.image("./shirtificate.png", w=pdf.epw)

    def print_text(self, name):
        self.set_font_size(30)
        self.set_text_color(255,255,255)
        self.cell(0,-230,f'{name} took CS50', align ="C")

    def print_shirtificate(self ,name):
        self.add_page()
        self.print_title()
        self.render_image()
        self.print_text(name)

pdf = PDF()
name = input("Name: ")
pdf.print_shirtificate(name)
pdf.output("shirtificate.pdf")

