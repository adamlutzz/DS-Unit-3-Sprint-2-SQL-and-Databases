import sqlite3

# open connection to new db file
CONN = sqlite3.connect('demo_data.sqlite3')

# create table
cursor = CONN.cursor()

create_table = 'CREATE TABLE demo (s varchar(30), x int, y int);'

cursor.execute(create_table)

cursor.close()
CONN.commit()

# add data to table
cursor2 = CONN.cursor()

insert_data = 'INSERT INTO demo (s, x, y) VALUES '

# data from table in markdown
data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

for datum in data:
    cursor2.execute(insert_data + str(datum))

cursor2.close()
CONN.commit()

# query data in table
cursor3 = CONN.cursor()

rows = cursor3.execute(
    'SELECT COUNT(*) FROM demo;'
    ).fetchall()

x_y = cursor3.execute(
    'SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;'
    ).fetchall()

y_values = cursor3.execute(
    'SELECT COUNT (DISTINCT y) FROM demo;'
    ).fetchall()

print('Number of Rows: ', rows[0])
print('Rows where X and Y are >= 5', x_y[0])
print('Unique values in column Y: ', y_values[0])

cursor3.close()
CONN.commit()