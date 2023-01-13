import PyPDF2
import re


class ExtractPDF(list):
    PDF_FILE_PATH = ''
    PDF_DATA_TABLE = ''
    PDF_IS_MULTI_TABLE = False
    PDF_OBJECT = None

    def __init__(self, args):
        self.PDF_FILE_PATH = args['file_path']
        self.PDF_DATA_TABLE = args['data_table']
        self.PDF_IS_MULTI_TABLE = args['is_multi_table']
        self.init_pdf_reader()

    def init_pdf_reader(self):
        self.PDF_OBJECT = PyPDF2.PdfReader(self.PDF_FILE_PATH)

    def total_pages(self):
        return len(self.PDF_OBJECT.pages)

    def get_page(self, page_no):
        if page_no > self.total_pages():
            return None
        return self.PDF_OBJECT.pages[page_no-1]

    def page_data(self, page):
        return page.extract_text()

    def read_index(self,index_page_number):
        page_data = self.page_data(self.get_page(index_page_number))
        page_data = page_data.replace('.', '')
        splitted_data = page_data.split('n')
        for data in splitted_data:
            print(data)

    def extract_data_as_dict(self):
        pass

