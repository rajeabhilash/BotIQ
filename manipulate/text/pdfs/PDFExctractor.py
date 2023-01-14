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
        self.PDF_INDEX_PAGE_NO = args['index_page_no']

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

    def read_index(self, index_page_number):
        index = []
        page_data = self.page_data(self.get_page(index_page_number))
        table_of_contents = str(page_data.split('Page')[2])
        table_rows = table_of_contents.splitlines()
        for row in table_rows:
            if row.strip() != "":
                dt = row.split('.')
                content = dt[0]
                page_no = int(dt[len(dt)-1])
                index.append([content, page_no])
        return index

    def get_page_no_by_content(self, content):
        for contents in self.PDF_INDEX_DATA:
            if content in contents[0]:
                return contents[1]
        return -1

    def extract_single_table_from_page(self, page_no=4):
        page_data = self.page_data(self.get_page(page_no))
        table_head_starts_from = '1/80 = 100'
        table_head_ends_at = 'Date'
        table_head_start_index = page_data.index(table_head_starts_from)
        table_head_end_index = page_data.index(table_head_ends_at)
        print('Length of Page : ', len(page_data))
        print('Header Start Index', table_head_start_index)
        print('Header Ends at', table_head_end_index)
        table_header = page_data[table_head_start_index+len(table_head_starts_from):table_head_end_index]
        table_header = table_header.replace(' ','~')
        print('Table Header ', table_header)


        # lines = page_data.splitlines()
        # for line in lines:
        #     print(line)
