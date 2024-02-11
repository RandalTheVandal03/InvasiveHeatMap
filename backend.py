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
        fileStem = Path(fileName).stem
        with open(Path(fileName), mode ='r') as file:
            csvFile = csv.reader(file)
            AnimalList = []
            for lines in csvFile:
                AnimalList.append(lines)
            
            StateSpecies[fileStem.lower()] = AnimalList

def getStateData(Name):
    return StateSpecies[Name]

# #Mainly For Debugging Purposes, gets all the information from any state
# for x in range(1):    
#     for list in StateSpecies['alaska']:
#         for list2 in list:
#             print(list2 , end=" ")
#         print()
