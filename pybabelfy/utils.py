'''
Created on 02/12/2015

@author: david
'''


def get_fragment(semantic_annotation,input_text):
    """
    @param semantic_annotation: A L{pybabelfy.babelfy.SemanticAnnotation} instance.
    @para input_text: The text from where the semantic annotation was extracted
    """
    start = semantic_annotation.char_fragment_start()
    end = semantic_annotation.char_fragment_end()
    return input_text[start:end+1]
    
    