import nltk
from nltk.tokenize import WordPunctTokenizer 
from nltk.corpus import stopwords
import re, string, unicodedata
from tqdm.notebook import tqdm
import stanza
from joblib import load

from sklearn.preprocessing import FunctionTransformer
stanza.download('es')
nltk.download('stopwords')
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')
spanish_stopwords = stopwords.words('spanish')
#print(spanish_stopwords)


from .funciones import softPreprocessing,preprocessing,tokenizar,applyLemmatizer
import __main__


__main__.softPreprocessing = softPreprocessing
__main__.preprocessing =preprocessing
__main__.tokenizar =tokenizar
__main__.applyLemmatizer = applyLemmatizer
