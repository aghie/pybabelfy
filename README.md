# pybabelfy
A python interface for Babelfy http://babelfy.org/ 

Babelfy is a multilingual, graph-based approach to Entity Linking and Word Sense Disambiguation.

# Installation

You can install pybabelfy from Pypi.
```
sudo pip install pybabelfy
```
or download the project, use ```cd``` to move to the pybabelfy folder and run:
```
sudo python setup.py install
```
# Getting started
To use pybabelfy you must register at http://babelfy.org/ and obtain your RESTful key

```
text= "BabelNet is both a multilingual encyclopedic dictionary and a semantic network"
lang = "EN"
key = "KEY" #This only works for the demo example. Change for the key you get once registered

babelapi = Babelfy()

semantic_annotations = babelapi.disambiguate(text,lang,key)
```
