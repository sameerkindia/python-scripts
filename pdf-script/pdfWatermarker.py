import PyPDF2

def add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path):
    with open(input_pdf_path, "rb") as input_file, \
         open(watermark_pdf_path, "rb") as watermark_file:

        reader = PyPDF2.PdfReader(input_file)
        watermark = PyPDF2.PdfReader(watermark_file).pages[0]
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            page.merge_page(watermark) 
            writer.add_page(page)

        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)


add_watermark("input.pdf", "watermark.pdf", "watermarked_output.pdf")