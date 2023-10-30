import pyodbc as pyodbc

SERVER = 'DESKTOP-M65EGB4'
DATABASE = 'crud'
USERNAME = 'sa'
PASSWORD = 'admin123'

cnxn = pyodbc.connect('DRIVER={SQL server};Server=DESKTOP-M65EGB4;DATABASE=crud;Port=1433;UID=sa'
                      ';PWD=admin123;')
cursor = cnxn.cursor()
