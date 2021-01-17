import shelve
import os
os.getcwd()
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon']
shelfFile.close()

shelFile = shelve.open('mydata')
shelFile['cats']
