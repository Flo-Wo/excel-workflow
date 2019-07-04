#!/usr/bin/python
# coding: utf8

import numpy as np
import excelworkflowutilities as ewf
import xlwings as xw

#wb = xw.Book()
path = str(input("Pfad zur Datei eingeben (mit .xlsx): "))
sheet = str(input("Tabelle eingeben (z.B. 'Tabelle1'): "))
valuesInput = str(input("Eingabespalten eingeben (z.B. 'M10:M38'): "))
uncertaintiesInput = str(input("Eingabespalten eingeben (z.B. 'N10:N38'): "))
resultsInput = str(input("Ziel eingeben für Gauss-Notation (z.B 'X10:X38'): "))


wb = xw.Book(path)
sht = wb.sheets[sheet]


valuesArray = sht.range(valuesInput).value
uncertaintiesArray = sht.range(uncertaintiesInput).value
resultsArray = sht.range(resultsInput).value

#Anweisungen, dass Unsicherheiten der zweite Array sein müssen


j = int(ewf.getStartIndex(resultsInput))
print(j)
#j = 10
sht.range('X9').value = "shesh"
if ( (len(valuesArray) == len(uncertaintiesArray) and len(resultsArray) == len(valuesArray))):
    for x in range(0, len(valuesArray)):
        # Check if there is an entry
        if valuesArray[x] != None:
            newvalue = ewf.numberToArray(valuesArray[x])
            newuncertainty = ewf.numberToArray(uncertaintiesArray[x])
            numbers = ewf.equalExponent(newvalue, newuncertainty)
            significantdigit = ewf.getSignDigit(numbers[1])
            uncertaintyRounded = np.round(numbers[1][0], significantdigit)
            valueRounded = np.round(numbers[0][0], significantdigit)
            #print(str(ewf.gaussNotation(valueRounded, uncertaintyRounded)) + 'E' + str(int(numbers[1][1])) )
            sht.range(str(resultsInput[0]) + str(j)).value = str(ewf.gaussNotation(valueRounded, uncertaintyRounded)) + 'E' + str(int(numbers[1][1]))
        j += 1
elif (len(valuesArray) != len(uncertaintiesArray)):
    print("Fehler: Länge der Eingaben stimmt nicht überein.")
else:
    print("Fehler: Nicht genügend Platz für die Ergebnisse. Ein- und Ausgabegrößen müssen übereinestimmen.")




