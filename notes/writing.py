# AC 2nd Write To Notes

"""with open("notes\\sample.txt", 'a') as file:
    file.write("\nJoe\n")
    file.write("Israel\n")
    file.write("Zee\n")

print("Run Finished")"""

"""content = []"""
# r+ is read and write
"""with open("notes\\sample.txt", 'r+') as file:
    for line in file:
        content.append(line.strip())
    
    index = content.index('Tia')
    content[index] = "Torii"

    file.truncate(0)

    for name in content:
        file.write(name + "\n")

print("Code Ends")"""

import csv

"""with open("notes/test.csv", 'w', newline='') as csvfile:
    fieldnames = ['username', 'favorite color']
    writer = csv.writer(csvfile)

    # writer.writerow(fieldnames)
    writer.writerow(["user1", "red"])
    writer.writerow(["user2", "orange"])"""

users = [{"username": "cosmic_voyager", "favorite color": "indigo"}, {"username": "cosmic_voyager", "favorite color": "indigo"}, {"username": "cosmic_voyager", " favorite color": "indigo"}, {"username": "cosmic_voyager", "favorite color": "indigo"}]

with open("notes/test.csv", 'a', newline='') as csvfile:
    fieldnames = ['username', 'favorite color']
    writer = csv.DictReader(csvfile, fieldnames=fieldnames)

    # writer.writerow(fieldnames)
    writer.writerows(users)