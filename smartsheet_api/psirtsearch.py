import os
import openpyxl

while True:
        os.chdir("C:\\Users\\vikm\\Desktop\\psirt_filter")
        wb = openpyxl.Workbook()
        sheet = wb.active
        file_name = input("Enter file name:")
        f = open(file_name+".html","r")
        for x in f:
            if(x.startswith("		var bugId =")==True):
                ids = x[15:-3]
                # print(ids)
                sheet.append([ids])
        wb.save(file_name+"_psirt.xlsx")
        print("Success..")