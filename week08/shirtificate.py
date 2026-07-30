from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Heading
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    page_width = pdf.w
    image_width = 100
    image_x = (page_width - image_width) / 2
    image_y = 40

    pdf.image("shirtificate.png", x=image_x, y=image_y, w=image_width)

    # User's name, in white, on top of the shirt
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(image_x, image_y + 55)
    pdf.cell(image_width, 10, name, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
