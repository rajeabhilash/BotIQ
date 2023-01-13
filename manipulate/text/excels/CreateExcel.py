import openpyxl


class CreateExcel(list):

    EXCEL_NAME = ''
    EXCEL_PATH = ''
    EXCEL_SHEET_NAME = ''
    EXCEL_DATA_TABLE = None

    def __init__(self, args):
        self.EXCEL_NAME = args['excel_name']
        self.EXCEL_SHEET_NAME = args['excel_sheet_name']
        self.EXCEL_DATA_TABLE = args['excel_data_table']
        wb = openpyxl.Workbook()
        sheet = wb.create_sheet(self.EXCEL_SHEET_NAME)
        sheet['A1'] = 'Header Data'
        sheet['A2'] = "Subheader Data"
        wb.save(str(self.EXCEL_PATH + self.EXCEL_NAME))
