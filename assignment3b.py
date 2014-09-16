import sqlite3

user_input = raw_input("AVG, MAX, MIN, SUM or EXIT?> ")

if user_input.lower() == "exit":
    print "Bye then..."
    exit()
else:
    command = user_input.upper()
    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()
        c.execute("SELECT {}(numbers) FROM numbers".format(command))
        answer = c.fetchone()
        print command, "is...", answer[0]

