import smartsheet
access_tkn = "zwusuvdtqnmgib0vyvwexozj89"
smsh = smartsheet.Smartsheet(access_tkn)
sheet_id= 7679274808305540

# cell_values = []
total_row_values = []
colms = []
bool_list = []
work_sheet = smsh.Sheets.get_sheet(sheet_id)

# response = smsh.Cells.get_cell_history(7679274808305540,3542578240481156,3618974329005956)

# print(response.data)

for my_col in work_sheet.columns:
    colms.append(my_col.id)
print(colms)
bug_id = input("Enter the BugID:")

for my_row in work_sheet.rows:
    for my_cell in my_row.cells:
        if my_cell.column_id == colms[5]:
            if(my_cell.value != None and my_cell.value == bug_id):
                bool_list.append(True)
                print(my_cell.value)
                # print("yes")
            elif(my_cell.value != None):
                bool_list.append(False)
                # print('no')  

# print(bool_list)

for i,j in zip(work_sheet.rows,bool_list):
    if(j):
        # print("hello")
        for wo_cell in i.cells:
            print(wo_cell.value,end =" ")
        print("\n")
# for work_row in work_sheet.rows:
# #     flagval = 0CSCvn65599
#         cell_values = []
#         for work_cell in work_row.cells:
#                 if(work_cell.value == None):
#                         continue
#                 else:
#                         cell_values.append(work_cell.value)
# print(cell_values)
# total_row_values.append(cell_values)
#         # total_row_values.append(cell_values)
# print(total_row_values)
