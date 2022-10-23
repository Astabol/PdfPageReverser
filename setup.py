#PyPDF2 is a tool for playing with pdf
#for installing PyPDF use "  pip install PyPDF2   "

from PyPDF2 import PdfFileReader, PdfFileWriter
class PdfOperations:
    def ReversePagesinPDFFile(self, inputPdfFileName, outputPdfFileName):
        print("Pdf Reversing Started!")
        pdfWriter = PdfFileWriter()
        pdfReader = PdfFileReader(inputPdfFileName)
        n = pdfReader.getNumPages()
        for i in range(n):
            page = pdfReader.getPage((n - i - 1))
            pdfWriter.addPage(page)
        with open(outputPdfFileName, 'wb') as outPdf:
            pdfWriter.write(outPdf)
        print("Pdf Reversing Done!")
    
if __name__ == "__main__":
    playWithPdf = PdfOperations()
    playWithPdf.ReversePagesinPDFFile("inputPdfName.pdf","outputPdfName.pdf") #change input output PDF name accordingly



