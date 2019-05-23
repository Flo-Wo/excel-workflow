#!/usr/bin/python
# coding: utf8

import numpy as np
import excelworkflowutilities as ewf
import xlwings as xw

#wb = xw.Book()
wb = xw.Book('Ergebnisse.xlsx')
sht = wb.sheets['Tabelle1']
#print(sht.range('K13:K16').value)
#print(type(sht.range('K13').value))

valuesArray = sht.range('M10:M38').value
uncertaintiesArray = sht.range('N10:N38').value
#resultsArray = sht.range('X10:X38').value

#Anweisungen, dass Unsicherheiten der zweite Array sein müssen


j = 10
sht.range('X9').value = "Test Überschrift"
if ((len(valuesArray) == len(uncertaintiesArray) and len(resultsArray) == len(valuesArray)):
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
            sht.range('X' + str(j)).value = str(ewf.gaussNotation(valueRounded, uncertaintyRounded)) + 'E' + str(int(numbers[1][1]))
        j += 1
elif (len(valuesArray) != len(uncertaintiesArray)):
    print("Fehler: Länge der Eingaben stimmt nicht überein.")
else :
    print("Fehler: Nicht genügend Platz für die Ergebnisse. Ein- und Ausgabegrößen müssen übereinestimmen.")




