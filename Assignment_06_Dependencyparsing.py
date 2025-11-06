###  Assignment No 6 ###

"""Assignment Title : : Implement and visualize Dependency Parsing of Textual Input
using Stan- ford CoreNLP and Spacy library"""


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Earth is the third planet from the Sun in our solar system and the only known celestial body to support life. 
With a diverse range of ecosystems, it is home to a vast array of plant and animal species, including humans. 
Earth's atmosphere, composed mainly of nitrogen and oxygen, sustains life by providing the necessary conditions for biological processes to thrive.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")


