#!/usr/bin/python
# coding: utf8

import numpy as np
import excelworkflowutilities as eu
import xlwings as xw

#wb = xw.Book()
wb = xw.Book('Ergebnisse.xlsx')
sht = wb.sheets['Sheet1']
print(sht.range('K13').value)



