import PyPDF2

with open('dummy2.pdf', 'rb') as file:
    # print(file)
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    # print(reader.pages[0].extract_text())

    # page.rotateClockwise(90)
    # page.rotate_clockwise(90)
    page.rotate(90)

    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)