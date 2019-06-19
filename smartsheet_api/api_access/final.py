import smartsheet
access_tkn = "zwusuvdtqnmgib0vyvwexozj89"
smsh = smartsheet.Smartsheet(access_tkn)
sheet_id = ['8244919853705092','8491038659635076']
# sheet_id= 7679274808305540
bug_id = input("Enter the BugID: ")
for sheets in sheet_id:
    total_row_values = []
    colms = []
    bool_list = []
    work_sheet = smsh.Sheets.get_sheet(sheets)

    for my_col in work_sheet.columns:
        colms.append(my_col.id)
    # print(colms)
    
    for my_row in work_sheet.rows:
        for my_cell in my_row.cells:
            if my_cell.column_id == colms[5]:
                if(my_cell.value != None and my_cell.value == bug_id):
                    bool_list.append(True)
                    # print(my_cell.value)
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


