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
        return self.PDF_OBJECT.pages[page_no - 1]

    def _page_data(self, page):
        return page.extract_text()

    def read_index(self, index_page_number):
        index = []
        page_data = self._page_data(self.get_page(index_page_number))
        table_of_contents = str(page_data.split('Page')[2])
        table_rows = table_of_contents.splitlines()
        for row in table_rows:
            if row.strip() != "":
                dt = row.split('.')
                content = dt[0]
                page_no = int(dt[len(dt) - 1])
                index.append([content, page_no])
        return index

    def get_page_no_by_content(self, content):
        for contents in self.PDF_INDEX_DATA:
            if content in contents[0]:
                return contents[1]
        return -1

    def _process_header_string(self, header_string, column_count):
        header = []
        # header_string = re.sub(r'\n', '*', header_string)
        # header_string = re.sub(r'\n', '1', header_string)
        # header_string = header_string.replace(' ', '~')
        header_string = header_string.splitlines()
        # temp = header_string.split('~~')
        print(header_string)
        # print(temp)
        # temp = ' '.join(temp).split()
        # for words in temp:
        #     if len(words)<2 :
        #         continue
        #     else:
        #         if words.__contains__('1'):
        #             new_word = words.replace('1', ' ')
        #             # new_word = words.replace('~', ' ')
        #             header[len(header)-1] = header[len(header)-1] + ""+ new_word
        #         else:
        #             header.append(words.replace('~',' '))

        # for i in range(len(header_string)):
        #     if header_string[i].isalpha():
        #         print(header_string[i])
        # print(header_string)
        print(header)

        return header

    def extract_single_table_from_page(self, page_no=4):
        page_data = self._page_data(self.get_page(page_no))
        _header_starts_from = '1/80 = 100'
        _header_ends_at = 'Date'
        _sub_header_ends_at = 'Mult.'
        _header_start_index = page_data.index(_header_starts_from)
        _header_end_index = page_data.index(_header_ends_at)
        _header_string = page_data[_header_start_index + len(_header_starts_from):_header_end_index]
        # _header_string = _header_string.replace(' ', '~')
        _sub_head_string = page_data[_header_end_index: page_data.rindex(_sub_header_ends_at) + len(_sub_header_ends_at)]
        _sub_headers = _sub_head_string.split('  ')
        _sub_head_len = len(_sub_headers)
        headers = self._process_header_string(_header_string, _sub_head_len)
        # print(headers)
