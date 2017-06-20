import csv
import time
from japTrans import transCat


def read_eng_cat():
 cat_eng = open('catalog-sup-2017-06-17-09-35-00.csv', "r")
 d_reader = csv.DictReader(cat_eng, delimiter='|')
 return d_reader
 cat_eng.close()

def trans_file_header():
   header = read_eng_cat().fieldnames
   test_array = []

# Translate headers to Japanese

   for line in header:
       trans_txt = transCat.run_quickstart(line)
       test_array.append(trans_txt)

   return test_array

def trans_field_value():
    rows = list(read_eng_cat())

    for row in rows:
        transCat.run_quickstart(row['Product_Name'])

def write_to_file():
    '''
    timeStamp = time.strftime("%d%m%y%H%M%S")

    csv_file = open('test02.csv', 'w', encoding='utf-8')
    wtr = csv.writer(csv_file, delimiter='|')

    for x in trans_file_header():
        wtr.writerow([x])

    print('File created successfully')
  '''
    print(trans_file_header())
#trans_file_header()
#trans_field_value()
write_to_file()



