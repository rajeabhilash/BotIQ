from manipulate.text.pdfs import PDFExctractor

if __name__ == "__main__":
    arg = {

        'file_path': r"D:\Zoetis\UserData\ROW factors - January 2023.pdf",
        'data_table': 'MACHINE SHOP',
        'is_multi_table': False
    }

    obj = PDFExctractor.ExtractPDF(arg)
    print('No of Pages : ', obj.total_pages())
    # print(obj.read_index(1))
    print("Page No :", obj.get_page_no_from_index("Abhilash"))
    obj.extract_data_as_dict()
