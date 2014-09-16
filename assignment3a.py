import random
import sqlite3

#create empty list
rands = []

#generate numbers and add to list
for i in range(100):
    numb = random.randint(0,100)
    rands.append(numb)

rands.sort()
print rands


with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    for item in rands:
        c.execute("INSERT INTO numbers VALUES(?)", item)

    

