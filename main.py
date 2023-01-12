from manipulate.text.pdfs import PDFExctractor

if __name__ == "__main__":
    arg = {

        'file_path': r"D:\Zoetis\UserData\ROW factors - January 2023.pdf",
        'data_table': 'MACHINE SHOP',
        'is_multi_table': False
    }

    obj = PDFExctractor.ExtractPDF(arg)
    obj.extract_data()
