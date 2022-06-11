from PyPDF2 import PdfFileReader

reader = PdfFileReader("../files_to_play/The Quick Python Book.pdf")
number_of_pages = reader.numPages
page = reader.pages[2]
text = page.extractText()
# print(number_of_pages)
print(text)