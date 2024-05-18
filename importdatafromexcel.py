import pandas as pd
import sqlite3

def import_excel_to_sqlite(excel_file, db_file):
    # Read Excel file into a pandas DataFrame
    xls = pd.ExcelFile(excel_file)
    df_dict = pd.read_excel(xls, sheet_name=None)

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Iterate over each DataFrame (sheet) in the Excel file
    for sheet_name, df in df_dict.items():
        # Clean sheet name for table creation
        table_name = sheet_name.replace(' ', '_').lower()

        # Create table in SQLite database
        df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Replace 'input_excel.xlsx' with the path to your Excel file
excel_file = 'sql-assesment-data-set.xlsx'
# Replace 'output_db.db' with the desired SQLite database file name
db_file = 'test.db'

# Call the function to import data from Excel to SQLite
import_excel_to_sqlite(excel_file, db_file)