## Dan and Cainan
import csv
import os
from pathlib import Path

#Main Path of the CSV Files
directory = 'States'

#Dictionary for storing the state names and a vector of each endangered species
StateSpecies = {}

#Iterates through every single file and inserts the metadata into the StateSpecies dictionary
for fileName in os.scandir(directory):
    if fileName.is_file():
        file = Path(fileName).stem
        with open('fileName', mode ='r')as file:
            csvFile = csv.reader(file)
            tempList = []
            for lines in csvFile:
                tempList = lines
            print(tempList)


'''
with open('States/Florida.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)
        '''