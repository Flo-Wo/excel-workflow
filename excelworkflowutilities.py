#!/usr/bin/python
# coding: utf8

import numpy as np


def getExponent(number):
    """
    @param number
    @return power/exponent of the number
    """
    exponent = np.floor(np.log10(number))
    return(exponent)

def getMantisse(number):
    """
    @param number
    @return mantisse of the number without powers
    """
    mantisse = number / np.power(10, np.floor(np.log10(number)))
    return(mantisse)

def numberToArray(number):
    """
    function transfers an number to an array, split by mantisse and exponent
    @param number
    @return array with mantisse and exponent
    """
    mantisse = getMantisse(number)
    exponent = getExponent(number)
    number = [mantisse, exponent]
    return(number)


def equalExponent(value, uncertainty):
    """
    function equals the exponents after the mantisse
    of both of the input values represented by an array
    @param value as array
    @param uncertainty(value) as array
    @return array with both numbers with the same exponent
    """
    diff = value[1] - uncertainty[1]
    uncertaintytemp = [getMantisse(uncertainty[0]) * 10**(-diff), uncertainty[1] + diff]
    numbers = [value, uncertaintytemp]
    return(numbers)

def getComma(number):
    """
    function equals the exponents after the mantisse
    of both of the input values represented by an array
    @param number
    @return index of the comma, beginning by index 0
    """
    tempstring = str(number)
    i = 0
    try:
        while tempstring[i] != '.':
            i += 1
    except:
        print("Keine float Zahl, deshalb auf 0 gesetzt.")
        i = 0
    return(i)

def getSignDigit(number):
    """
    functions output is the index of the position to be rounded
    @param number array, with mantisse and exponent
    @return beginning index of the position which should be rounded,
    beginning with index 0 of the number
    """
    #Fallunterscheidung, ob vor oder nach dem Komma gerundet werden
    # Bsp 12,xxx bzw 1,xxx
    index = 0
    mantisse = number[0]
    #print('mantisse: ' + str(mantisse))
    indexComma = getComma(mantisse)
    #print("comma: " + str(indexComma))
    tempstrmant = str(mantisse)
    # führende Null
    #print('test: ' + tempstrmant[0])
    if tempstrmant[0] == '0':
        for i in range(1, len(tempstrmant)):
            #print(i)
            #print("test: " + str(tempstrmant[i + index]))
            if (tempstrmant[i + indexComma] != '0'):
                break
        index = indexComma + i
    # Zahl beginnt nicht mit 0
    else:
        # Setze Index auf Anzahl der Stellen vor dem Komma Unterscheide mit 1.xxx oder 21.xx
        # Siehe dazu Bild
        # dies entspricht gerade der Stelle mit dem Index 2 - indexComma
        index = 2 - indexComma
    return(index)

def gaussNotation(value, uncertainty):
    """
    function has the value and its uncertainty in Gauss-Notation as output
    e.g. 9.657(345)*E-12
    @param value
    @param uncertainty
    @return result
    """
    x = ''
    tempuncertain = str(uncertainty)
    # Beginn am Ende des Strings, da die Zahl 0.xx ist
    if uncertainty < 1:
        i = len(tempuncertain) - 1
        while (i >= 0 and tempuncertain[i] != '0' and tempuncertain[i] != '.'):
            #print("test: " + tempuncertain[i])
            x = tempuncertain[i] + x
            i -= 1
    # Fehler, bei 1,xx Zahlen
    elif uncertainty > 10:
        i = 0
        while (i < len(tempuncertain) and tempuncertain[i] != '.'): #and tempuncertain[i] != '0'
            x = x + tempuncertain[i]
            i += 1
        # Heraufschieben --> Abstand stimmt
        x = x + '0'
    # Zahlen im Bereich 1,xx bis 9,xx
    else:
        for j in range(0, len(tempuncertain)):
            if tempuncertain[j] != '.':
                x = x + tempuncertain[j]

    return(str(value) + '(' + x + ')')

def getStartIndex(indexRange):
    i = 1
    startIndex = ''
    while indexRange[i] != ':':
        startIndex = startIndex + str(indexRange[i])
        i += 1
    return(startIndex)

