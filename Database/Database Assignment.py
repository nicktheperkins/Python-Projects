
import sqlite3

# create and connect to the database file in my directory
conn = sqlite3.connect('test_db.db')

# create the tbl_files in the database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT)")
    conn.commit()
conn.close()

# reconnect to the database after closing it
conn = sqlite3.connect('test_db.db')

# tuple of file names
fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# loop through each object in the tuple to find the names that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # The value for each row will be one name out of the tuple therefore (x,)
            # will denote a one element tuple for each name ending in .txt.
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (x,))
conn.close()