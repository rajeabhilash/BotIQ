import PyPDF2
import re


class ExtractPDF(list):

    PDF_FILE_PATH = ''
    PDF_DATA_TABLE_NAME = ''
    PDF_OBJECT = None
    PDF_INDEX_PAGE_NO = 1
    PDF_INDEX_DATA = []
    PDF_IS_MULTI_TABLE = False

    def __init__(self, args):

        self.PDF_FILE_PATH = args['file_path']
        self.PDF_DATA_TABLE = args['data_table']
        self.PDF_IS_MULTI_TABLE = args['is_multi_table']
        # self.PDF_INDEX_PAGE_NO = args['index_page_no']

        self.init_pdf_reader()
        self.PDF_INDEX_DATA = self.read_index(self.PDF_INDEX_PAGE_NO)

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
        index = []
        page_data = self.page_data(self.get_page(index_page_number))
        table_of_contents = str(page_data.split('Page')[2])
        table_rows = table_of_contents.splitlines()
        for row in table_rows:
            if row.strip() != "":
                dt = row.split('.')
                content = dt[0]
                page_no = int(dt[len(dt)-1])
                index.append([content,page_no])
        return index

    def get_page_no_by_content(self, content):
        for contents in self.PDF_INDEX_DATA:
            if content in contents[0]:
                return contents[1]
        return -1

    def extract_data_as_dict(self):
        pass

