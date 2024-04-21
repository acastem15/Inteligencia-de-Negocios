from nltk.tokenize import WordPunctTokenizer 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

spanish_stopwords = stopwords.words('spanish')


def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        if word is not None:
          new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
          new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_words.append(word.lower())
    return new_words
    

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        if word is not None:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
    return new_words



def remove_numbers(textos):
    textos = textos.replace(r'\d+,\d+', '', regex=True)
    textos = textos.replace(r'\d+', '', regex=True)
    textos = textos.replace(r'\d+.\d+', '', regex=True)
    return textos

def remove_stopwords(words):
    own = ['ser','haber','tener','ir','poder','hacer','hotel','pedir','llegar','mas','habitacion','habitación',
           'decir','lugar','dia','alguno','dar','querer','comida','ver','vista','despue',
           'un','dos','tres','cuatro','cuc','adema','buen']
    new_words = []
    for word in words:
        if word not in spanish_stopwords and word not in own:
            new_words.append(word)
    return new_words

def preprocessing(words):
    words = words.apply(to_lowercase)
 #   words = replace_numbers(words)
    words = words.apply(remove_punctuation)
#    words = remove_non_ascii(words)
    words = words.apply(remove_stopwords)
    #Pasar a str de una
    words = words.apply(getString)
    return words

def getString(list): 
    string = ""
    for w in list: 
        string += w + " "
    return string

def getTokens(textos): 
    textos=textos.str.split()
    return textos


def softPreprocessing(textos):
    textos =remove_numbers(textos)
    tokens = getTokens(textos)
    words = tokens.apply(to_lowercase)
    words = words.apply(remove_non_ascii)
    words = words.apply(getString)
    return words

def tokenizar(textos):
    textos = textos.apply(WordPunctTokenizer().tokenize)
    return textos

from tqdm.notebook import tqdm
tqdm.pandas()
def lemmatizer(review):
    
    doc  =  nlp(review)
    #print (review)
    lemma = [[word.lemma for word in sent.words]  for sent in doc.sentences]
    finalLemma =[]
    for sent in lemma:
        for word in sent:  
            finalLemma.append(word)
    
    finalLemma = getString(finalLemma)

    return finalLemma

def applyLemmatizer(textos):

    return textos.progress_apply(lemmatizer) 


"""
textos['tokens']= textos.apply(lemmatizer,axis=1) #Aplica la lematización

#Codigo para guardar los lemas en csv
textos.to_csv('lemaSoftProcessing.csv')"""
"""
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import FunctionTransformer
softPreprocessingTransformer = FunctionTransformer(softPreprocessing)
tokenizarTransformer = FunctionTransformer(tokenizar)
preprocessingTransformer = FunctionTransformer(preprocessing)
applyLemmatizerTransformer = FunctionTransformer(applyLemmatizer)"""

"""from joblib import load
#pipeline_loaded = load("modelLemmatizer.joblib")
pipeline_loaded2 = load("model.joblib")"""