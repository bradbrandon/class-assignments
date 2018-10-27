# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:26:03 2018

@author: Brandon
"""os.getcwd()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'os' is not definimport os
>>> os.getcwd()
'C:\\Users\\Brandon\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.chdir()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Required argument 'path' (pos 1) not found
>>> os.chdir()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Required argument 'path' (pos 1) not found
>>>
>>> os.chdir("C:\\Users\\Brandon\Documents")
>>> os.getcwd()
'C:\\Users\\Brandon\\Documents'
>>> os.makedirs()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: makedirs() missing 1 required positional argument: 'name'
>>> os.makedirs("yu")
>>> os.chdir("\\yu")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 2] The system cannot find the file specified: '\\yu'
>>> os.chdir(".\\yu")
>>> os.getcwd()
'C:\\Users\\Brandon\\Documents\\yu'
>>> os.path.getsize(yu)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yu' is not defined
>>> os.path.getsize()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: getsize() missing 1 required positional argument: 'filename'
>>> os.path.getsize()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: getsize() missing 1 required positional argument: 'filename'
>>> os.path.exists()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exists() missing 1 required positional argument: 'path'
>>> os.path.exits("C:\\Users\\Brandon\\Documents\\yu")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'ntpath' has no attribute 'exits'
>>> os.path.exists("C:\\Users\\Brandon\\Documents\\yu")
True
>>>
