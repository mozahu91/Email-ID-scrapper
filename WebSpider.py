from pandas import DataFrame
import re
import csv
mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
exampleFile = open("google.csv", encoding = "utf16")
exampleReader = csv.reader(exampleFile)
l1 = []
for row in exampleReader:
    l1.append(mailsrch.findall(str(row)))
df = DataFrame({"Email IDs":l1})
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
