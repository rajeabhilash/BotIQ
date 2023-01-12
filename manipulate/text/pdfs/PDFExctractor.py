class ExtractPDF(list):

    PDF_FILE_PATH = ''
    PDF_DATA_TABLE = ''
    PDF_IS_MULTI_TABLE = False

    def __init__(self, args):
        self.PDF_FILE_PATH = args['file_path']
        self.PDF_DATA_TABLE = args['data_table']
        self.PDF_IS_MULTI_TABLE = args['is_multi_table']

    def extract_data(self):
        print(self.PDF_FILE_PATH)
        print(self.PDF_DATA_TABLE)
        print(self.PDF_IS_MULTI_TABLE)
        pass
