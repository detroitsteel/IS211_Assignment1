#! /usr/bin/env python
#! -*- coding: utf-8 -*-
"""Week 1 Assingment"""

def listDivide(numbers, divide = 2):
    """First function required by assingment 1 which will return the numbers
    passed which are divisable by 2


    """
    divbytwos = 0
    try:
        for num in numbers:
            if not num % divide:
                divbytwos += 1
    except ZeroDivisionError as ListDivideException:
        print 'You passed an invalid denominator. Please try again'
    else:
        return divbytwos

def testListDivide():
    """First function required by assingment 1 which will return the numbers
    passed which are divisable by 2


    """
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30, 54, 63,98, 100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
        listDivide([1,2,3,4,5], 0)
    except ListDivideException:
        print ListDivideException
        
