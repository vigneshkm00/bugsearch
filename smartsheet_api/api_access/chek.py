import smartsheet
access_tkn = "zwusuvdtqnmgib0vyvwexozj89"
smsh = smartsheet.Smartsheet(access_tkn)
sheet_id = ['8244919853705092','8491038659635076']
# sheet_id= 7679274808305540
bug_id = input("Enter the Bug ID: ")
proj_id = input("Enter the Project ID: ")
for sheets in sheet_id:
    total_row_values = []
    colms = []
    bool_list = []
    work_sheet = smsh.Sheets.get_sheet(sheets)

    # for my_col in work_sheet.columns:
    #     colms.append(my_col.id)
    # print(colms)
    # my_col = []
    # my_col = work_sheet.columns
    # col_id = my_col[5].id
    
    for my_row in work_sheet.rows:
        my_cells = []
        my_cells = my_row.cells
        if(my_cells[4].value == proj_id and my_cells[5].value ==bug_id):
            print(my_cells[1].value,my_cells[2].value,my_cells[3].value,my_cells[4].value,my_cells[5].value,my_cells[8].value,my_cells[9].value,my_cells[10].value,my_cells[11].value,my_cells[12].value,my_cells[13].value,my_cells[14].value,my_cells[15].value,my_cells[16].value,my_cells[17].value)

        # for my_cell in my_row.cells:
        #     if my_cell.column_id == col_id:
        #         if(my_cell.value != None and my_cell.value == bug_id):
        #             bool_list.append(True)
        #             # print(my_cell.value)
        #             # print("yes")
        #         elif(my_cell.value != None):
        #             bool_list.append(False)
                    # print('no')  
    
    # print(bool_list)
     
    # for i,j in zip(work_sheet.rows,bool_list):
    #     if(j):
    #         # print("hello")
    #         for wo_cell in i.cells:
    #             print(wo_cell.value,end =" ")
    #         print("\n")


