import pyodbc as pyodbc

SERVER = 'DESKTOP-M65EGB4'
DATABASE = 'crud'
USERNAME = 'sa'
PASSWORD = 'admin123'

cnxn = pyodbc.connect('DRIVER={ODBC DRIVER 17 FOR SQL SERVER};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+PASSWORD)
cursor = cnxn.cursor()
