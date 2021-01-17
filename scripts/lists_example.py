>>> range(4)
range(0, 4)
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> supplies = ['pens', 'cars', 'bin']
>>> for i in range(len(supplies)):
	print('Index: ' + str(i) + ' in supp: ' + supplies[i])

	
Index: 0 in supp: pens
Index: 1 in supp: cars
Index: 2 in supp: bin
>>> cat = ['fat', 'orange', 'loud']

>>> size, color, dispo = cat
>>> size
'fat'
>>> dispo
'loud'
>>>
>>> size, color = 'skynni', 'black'
>>> size
'skynni'
>>> color
'black'
>>> spam = 42
>>> spam = spam + 1
>>> spam += 1
>>> spam
44
>>>
spam.append('moose')

>>> spam = ['hello', 'hi', 'howdy']
>>> spam.index('hello')
0
>>> spam.index()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    spam.index()
TypeError: index expected at least 1 argument, got 0
>>> 
>>> spam.index('sahdajkhd')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    spam.index('sahdajkhd')
ValueError: 'sahdajkhd' is not in list
>>> spam = ['cat', 'dog']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'moose']
>>> spam.insert(1,'mouse')
>>> spam
['cat', 'mouse', 'dog', 'moose']
>>> spam.append('moose')
>>> spam.append('moose')
>>> spam.append('moose')
>>> spam
['cat', 'mouse', 'dog', 'moose', 'moose', 'moose', 'moose']
>>> 
>>> spam.remove('dog')
>>> spam
['cat', 'mouse', 'moose', 'moose', 'moose', 'moose']
>>> spam.sort()
>>> spam
['cat', 'moose', 'moose', 'moose', 'moose', 'mouse']
>>> spam.append('dog')
>>> spam.sort()
>>> spam
['cat', 'dog', 'moose', 'moose', 'moose', 'moose', 'mouse']



>>> import copy
>>> spam = ['a','b','c']
>>> cheese = copy.deepcopy(spam)
>>> cheese
['a', 'b', 'c']
>>> cheese[1] = 32
>>> cheese
['a', 32, 'c']
>>> spam
['a', 'b', 'c']
