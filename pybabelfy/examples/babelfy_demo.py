'''
Created on 02/12/2015

@author: david
'''


from pybabelfy.babelfy import *


def frag(semantic_annotation, input_text):
    start = semantic_annotation.char_fragment_start()
    end = semantic_annotation.char_fragment_end()
    return input_text[start:end+1]

text= "BabelNet is both a multilingual encyclopedic dictionary and a semantic network"
lang = "EN"
key = "KEY" #This only works for the demo example. Change for the key you get once registered

babelapi = Babelfy()

semantic_annotations = babelapi.disambiguate(text,lang,key, anntype= AnnTypeValues.ALL)
for semantic_annotation in semantic_annotations:
    print frag(semantic_annotation,text)
    semantic_annotation.pprint()
