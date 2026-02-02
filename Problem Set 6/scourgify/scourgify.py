# The goal is to split a string into two different columns
# We will take input the name of the file with the rows and columns and a new file to write into our results
# If the first name of the split can not be read/exist, then stop

import sys
import csv
import os

def main():
    if len(sys.argv) != 3:
         sys.exit("Error: Too few arguments | Usage: python lines.csv <filename>")
    before = sys.argv[1]
    after = sys.argv[2]

    if not before.endswith(".csv") or not after.endswith(".csv") :
          sys.exit("csv file not specfied.")

    # or if the specified file does not exist. Raise FileNotFound
    if not os.path.exists(before):
          raise FileNotFoundError("Error: File does not exist.")

    newfile(modify(before),after)

def modify(before):
	#create a dictonary to store the updates
    data = []
    #open it up
    with open(before) as b:
        reader = csv.DictReader(b)
        # loop for each row
        for row in reader:
            #split the name into first and last using space as the separator
            name = row["name"].split(", ")
            #if there is no first name, then stop
            if len(name) < 2:
                sys.exit("Error: Missing first name.")
            #store the first and last names into the dictonary
            last = name[0]
            first = name[1]
            house = row["house"]
            #append each row into the data dictonary
            data.append({"first": first, "last": last, "house": house})

    return data

def newfile(data, after):
    #write the data into a new .csv
    #open up the new csv file with "w"
    with open(after, "w") as a:
      #describe the each Row key or name using fieldnames
      fieldnames = ['first', 'last', 'house']
      #Using dictwriter(presence of keys and values) on the csv file and fieldnames as it fieldnames(key for each row)
      writer = csv.DictWriter(a, fieldnames= fieldnames)
      writer.writeheader()
      writer.writerows(data)


if __name__ == "__main__":
    main()
