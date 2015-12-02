'''
Created on 02/12/2015

@author: David
'''

import urllib
import json


class BabelfyJSONKeys(object):
    
    
    TOKEN_FRAGMENT = "tokenFragment"
    CHAR_FRAGMENT = "charFragment"
    CHAR_FRAGMENT_START = "start"
    CHAR_FRAGMENT_END = "end"
    BABEL_SYNSET_ID = "babelSynsetID"
    DBPEDIA_URL = "DBpediaURL"
    BABELNET_URL = "BabelNetURL"
    SCORE = "score"
    COHERENCE_SCORE = "coherenceScore" 
    GLOBAL_SCORE ="globalScore"
    SOURCE =  "source"
           
    
#     def expression(self):
#         start = self.char_fragment()[self.CHAR_FRAGMENT_START]
#         end = self.char_fragment()[self.CHAR_FRAGMENT_END]
#         return self.text[start:end+1]

class Babelfy(object):

    TEXT = "text"
    LANG = "lang"
    KEY = "key"
    ANNTYPE= "annType"
    ANNRES = "annRes"
    TH = "th"
    MATCH = "match"
    MCS = "MCS"
    DENS = "dens"
    CANDS = "cands"
    POSTAG = "postag"
    EXTAIDA = "extAIDA"
        
    PARAMETERS = [TEXT,LANG,KEY,ANNTYPE,ANNRES,TH,MATCH,MCS,DENS,CANDS,POSTAG,EXTAIDA]
    
    API = "https://babelfy.io/v1/"
    DISAMBIGUATE = "disambiguate?"
    
        
    def disambiguate(self, text,lang,key, anntype=None, annres=None, th=None,
                     match=None,mcs=None,dens=None,cands=None,postag=None,
                     extaida=None):
        """
        Params: Take a look to: http://babelfy.org/guide
        @return: A list of dictionaries with the expressions that were disambiguated. List is sorted
        according to the expressions position inside the text
        """
        dict_word_babelfy_json = {}
        values = [text,lang,key,anntype,annres,th,match,mcs,dens,
                            cands,postag,extaida]
        
        query = "&".join([param+"="+value for param,value in zip(self.PARAMETERS, values)
                         if value is not None])

        
        json_string = urllib.urlopen(self.API+self.DISAMBIGUATE+query).read()
        babelfy_jsons = json.loads(json_string)
        return babelfy_jsons