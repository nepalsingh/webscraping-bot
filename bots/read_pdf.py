import tabula
# import pandas as pd


def read_pdf(path):
    df = tabula.read_pdf(path, pages='all')
    return df

data  = read_pdf('files/weather.pdf')
print(type(data))

data[0].to_csv('files/weather.csv', index=None)



# import fitz


# def read_pdf(path):
#     doc = fitz.open(path)
#     text = ''
#     for page in doc:
#         text += page.getText()
#     return text


# if __name__ == '__main__':
#     path = 'files/students.pdf'
#     print(read_pdf(path))