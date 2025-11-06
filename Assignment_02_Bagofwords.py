##Assignment No.02##

#Title:Assignment to implement Bag of Words and TFIDF using Gensim library.
import gensim
from gensim import corpora
from gensim.utils import simple_preprocess

text2 = ["""I love programming
         Python is my favorite programming language.
         Programming allows me to solve real-world problems."""]

tokens2 = [[item for item in line.split()] for line in text2]
g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " + str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)

g_bow2 = [g_dict2.doc2bow(token, allow_update=True) for token in tokens2]
print("Bag of Words : ", g_bow2)

text3 = ["""I love programming
         Python is my favorite programming language.
         Programming allows me to solve real-world problems."""]

g_dict3 = corpora.Dictionary([simple_preprocess(line) for line in text3])
g_bow3 = [g_dict3.doc2bow(simple_preprocess(line)) for line in text3]

print("\nDictionary : ")
for item in g_bow3:
    print([[g_dict3[id], freq] for id, freq in item])


    
##OUTPUT##
'''
The dictionary has: 12 tokens

{'I': 0, 'Python': 1, 'allows': 2, 'favorite': 3, 'is': 4, 'language.': 5, 'love': 6, 'me': 7, 'my': 8, 'programming': 9, 'real-world': 10, 'solve': 11}
Bag of Words :  [[(0, 1), (6, 1), (9, 1)], [(1, 1), (3, 1), (4, 1), (5, 1), (8, 1), (9, 1)], [(2, 1), (7, 1), (10, 1), (11, 1), (9, 1)]]

Dictionary : 
[['I', 1], ['love', 1], ['programming', 1]]
[['Python', 1], ['favorite', 1], ['is', 1], ['language', 1], ['my', 1], ['programming', 1]]
[['allows', 1], ['me', 1], ['real-world', 1], ['solve', 1], ['programming', 1]]

'''