import csv
import os

myPath = "/Users/johnoconnor/Documents/Programming/RealPython/sql/Output"
movies = [ ["Movie", "Rating"],            
            ["Batman", "9"],
            ["Spiderman", "7"],
            ["Unbreakable", "6"] ]

with open(os.path.join(myPath, "movies.csv"), "wb") as myFile:

    myFileWriter = csv.writer(myFile)
    myFileWriter.writerows(movies)
