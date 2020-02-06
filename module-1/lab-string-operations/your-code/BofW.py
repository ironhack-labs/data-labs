#bag of words
import re
corpus = ['Ironhack is cool.', 'I love Ironhack.', 'I am a student at Ironhack.']
# print [re.sub('[a-zA-Z]'+[ ], '', _) for _ in corpus]
print(''.join(c for c in corpus if c not in '._-'))

