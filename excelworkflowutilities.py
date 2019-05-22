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
    mantisse = number[0]
    index = getComma(mantisse)
    #print("comma: " + str(index))
    tempstrmant = str(mantisse)
    for i in range(1, len(tempstrmant)):
        #print(i)
        #print("test: " + str(tempstrmant[i + index]))
        if (tempstrmant[i + index] != '0'):
            break
    return(index + i)

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
    i = len(tempuncertain) - 1
    while (i >= 0 and tempuncertain[i] != '0'):
        #print("test: " + tempuncertain[i])
        x = tempuncertain[i] + x
        i = i-1
    return(str(value) + '(' + x + ')')



# value1 = float(9.656789 * 10**-10)
# value2 = float(0.0876 * 10**-12)
# #print(value1, value2)
#
# newvalue1 = numberToArray(value1)
# newvalue2 = numberToArray(value2)
# numbers = equalExponent(newvalue1, newvalue2)
# print(numbers)
# significantdigit = getSignDigit(numbers[1])
# #print(significantdigit)
# test1 = np.round(numbers[1][0], significantdigit)
# test2 = np.round(numbers[0][0], significantdigit)
# print(np.round(numbers[1][0], significantdigit))
# print(np.round(numbers[0][0], significantdigit))
# #print(type(np.round(numbers[0][0], significantdigit)))
# print(gaussNotation(test2, test1))
#
# endvalue1 = [ np.round(numbers[0][0], significantdigit), numbers[0][1] ]
# endvalue2 = [ np.round(numbers[1][0], significantdigit), numbers[1][1] ]
# #print(str(endvalue1[0]*np.power(10,endvalue1[1])), str(endvalue2[0]*np.power(10,endvalue2[1])))