#Downloading Google Forms Data

import ezsheets

#Use link as argument so it doesn't fail
ss = ezsheets.Spreadsheet(\
    'https://docs.google.com/spreadsheets/d/1VgXSh97M0kzrkZ6SexRk5KY2q2CAl4tPKGBDxNLsqYg/edit?resourcekey=&gid=986064492#gid=986064492')

#Get first sheet
sheet = ss[0]

#See how many rows and columns there are
print('Columns: ', sheet.columnCount)
print('Row: ', sheet.rowCount)

#Check for the column with email adress and then print them
for column in range(1, sheet.columnCount + 1):
    columnTitle = sheet[column, 1]
    if 'email' in columnTitle:
        for row in range(2, sheet.rowCount + 1):
            if(sheet[column,row] is not ''):
                print(sheet[column,row])
            else:
                break
        break
