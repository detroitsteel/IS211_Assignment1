#! /usr/bin/env python
#! -*- coding: utf-8 -*-
"""Week 1 Assingment - Part 2"""

class Book(object):
    """First function required by assingment 1 which will return the numbers
    passed which are divisable by 2


    """
    author = ''
    title = ''
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
def display():
    """First function required by assingment 1 which will return the numbers
    passed which are divisable by 2
    """
    disbook1 = Book('John Steinbeck', 'Of Mice and Men')
    disbook2 = Book('Harper Lee', 'To Kill a Mockingbird')
   
    print disbook1.title, "written by", disbook1.author
    print disbook2.title, "written by", disbook2.author
