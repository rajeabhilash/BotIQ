# from importer import imports
from manipulate.visuals import simpleocr

if __name__ == "__main__":
    # out = simpleocr.get_text_from_image('https://files.realpython.com/media/ocr.930a7baf9137.jpg',islocal=False)
    # out = simpleocr.get_text_from_image(r'D:\IBA\Projects\BotIQ\sampledata\DifferFonts.jpg',islocal=True)
    # out = simpleocr.get_brackets_to_text(r'D:\IBA\Projects\BotIQ\sampledata\AtoT.jpg')
    # out = simpleocr.get_brackets_to_text(r'D:\IBA\Projects\BotIQ\sampledata\invoices\Invoice_EastRepair.jpg')
    out = simpleocr.get_dict_from_image(r'D:\IBA\Projects\BotIQ\sampledata\invoices\Invoice_EastRepair.jpg')
    print(out)
    print('-'*20)
    print(out.keys())
