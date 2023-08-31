from pdf2docx import Converter
old_pdf = input('Enter the name of pdf: pdf_file.pdf ')
new_doc = input('Enter the name of doc file: new_docx.docx ')
obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()


from docx2pdf import convert
docx = input('Enter the name of doc file: docx_file.docx ')
pdf = input('Enter the name of pdf: new_pdf.pdf ')
convert(docx,pdf)