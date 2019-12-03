import sqlite3

# open connection to new db file
CONN = sqlite3.connect('northwind_small.sqlite3')

cursor = CONN.cursor()

top_10_price = cursor.execute(
    'SELECT ProductName, UnitPrice FROM Product \
    Order BY UnitPrice desc LIMIT 10;'
    ).fetchall()

avg_emp_age = cursor.execute(
    "SELECT AVG((strftime('%Y', 'now') - strftime('%Y', BirthDate)) - \
    (strftime('%m-%d', 'now') < strftime('%m-%d', BirthDate) ))\
    FROM Employee;"
    ).fetchall()



print('Top 10 Most Expensive Products: ', top_10_price[0])
print('Average Employee Age: ', avg_emp_age[0])

cursor.close()
CONN.commit()


cursor1 = CONN.cursor()

top_10_supplier = cursor1.execute(
    'SELECT p.ProductName, p.UnitPrice, s.CompanyName FROM Product AS p,\
    Supplier AS s WHERE p.SupplierId = s.Id Order BY UnitPrice desc LIMIT 10;'
    ).fetchall()

largest_category = cursor1.execute(
    'SELECT CategoryName, MAX(Nunique) FROM(SELECT CategoryName, COUNT(CategoryName)\
    AS Nunique FROM(SELECT c.CategoryName FROM Category AS c, Product AS p \
    WHERE c.Id = p.CategoryId) GROUP BY CategoryName);'
    ).fetchall() # could not get this query to run correctly

print('Top 10 Products w/ Supplier: ', top_10_supplier[0])
print('Largest Category by unique Product: ', largest_category[0])

cursor1.close()
CONN.commit()