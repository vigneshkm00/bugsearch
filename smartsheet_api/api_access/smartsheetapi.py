import smartsheet
access_tkn = "zwusuvdtqnmgib0vyvwexozj89"

smsh = smartsheet.Smartsheet(access_tkn)
sheet_id= 7679274808305540
col_id = 3618974329005956

work_sheet = smsh.Sheets.get_sheet(sheet_id)

for my_row in work_sheet.rows:
    for my_cell in my_row.cells:
        if my_cell.column_id == col_id:
            if(my_cell.value == "CSCvn26674"):
                print(my_cell.value)
                # print(",")
    # print(",")
