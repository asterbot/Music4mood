import nltk
nltk.download('wordnet', quiet=True)

import text2emotion as te
emotions_value=te.get_emotion("I'm bored of playing games")
print(emotions_value)