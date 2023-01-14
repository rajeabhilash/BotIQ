from manipulate.text.pdfs import PDFExctractor
# from manipulate.visuals import simpleocr

if __name__ == "__main__":
    # a = simpleocr.get_text_from_image(r"D:\IBA\Projects\BotIQ\sampledata\BasicTable.png",True)
    # b = simpleocr.get_brackets_to_text(r'D:\IBA\Projects\BotIQ\sampledata\BasicTable.png')
    # print(a)

    arg = {

        'file_path': r"D:\Zoetis\UserData\ROW factors - January 2023.pdf",
        'data_table': 'MACHINE SHOP',
        'is_multi_table': False,
        'index_page_no' : 1,
    }

    obj = PDFExctractor.ExtractPDF(arg)

    # print('No of Pages : ', obj.total_pages())
    # print(obj.read_index(1))
    # print("Page No :", obj.get_page_no_by_content("Forge"))
    obj.extract_single_table_from_page(4)
