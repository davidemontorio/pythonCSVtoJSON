import csv
import json
from collections import OrderedDict

def main():

  # Final dictionary
  dictionary = {}

  # Open the csv file
  with open('dict.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:

        # Define items
        items = ""

        # Get items value (from both languages, cols 1 and 2)
        if row[1] != "" and row[1] != "?":
            items = row[1] + ";"
        if row[2] != "" and row[1] != "?":
            items = items + row[2]

        # Add items
        if items != "":
            # Create an array with all choices
            items = items.lower().split(';')

            dictionary[row[0].lower()] = items
            lineCount += 1
    
    print('Added ' + str(lineCount) + ' lines.')

    # Save dictionary to json file
    with open('dict.json', 'w') as outfile:
        # Create an ordered collection
        orderedDictionary = OrderedDict(sorted(dictionary.iteritems()))
        # Save json to file
        json.dump(orderedDictionary, outfile, ensure_ascii=False)

if __name__== "__main__":
  main()
