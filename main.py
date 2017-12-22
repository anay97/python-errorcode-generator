import xlrd
book = xlrd.open_workbook("error code.xlsx")

print (book.sheet_names())
ec=[]
routes=[]
first_sheet = book.sheet_by_index(0)
for i in range(1,first_sheet.nrows):
    cell = first_sheet.cell(i,0)
    ec.append((int(cell.value)))
    routes.append(first_sheet.cell(i, 1).value)
y=""
for i in range(0, len(routes)):
    a=routes[i]
    if '/' not in a:
        a = a + '/'
    b=a[:a.find('/')]
    y=y+'else if(endPoint.contains("'+b+'")){errorCode="'+str(ec[i])+'";}\n'

x="""
package com.vaisansar.das.filters;
public class ErrorCode {
public static String fetchErrorCode(String endPoint) {
String errorCode="";
"""


z="""
return errorCode;
}
}
"""


w = x + "\n" + y + "\n" + z

text_file = open("Output.txt", "w")
text_file.write(w)
text_file.close()