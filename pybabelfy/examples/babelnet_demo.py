'''
Created on 02/12/2015

@author: david
'''


from pybabelfy.babelfy import Babelfy



text= "BabelNet is both a multilingual encyclopedic dictionary and a semantic network"
lang = "EN"
key = "KEY" #This only works for the demo example. Change for the key you get once registered

babelapi = Babelfy()

output = babelapi.disambiguate(text,lang,key)

print output
