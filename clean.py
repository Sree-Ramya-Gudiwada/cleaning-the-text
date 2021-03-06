import nltk
import string
from .exceptions import CleanTextEmptyString

ps = nltk.PorterStemmer()


def clean(text: str, clean_all: bool = True, extra_spaces: bool = False, stemming: bool = False,stopwords: bool = False,
          lowercase: bool = False, numbers: bool = False, punct: bool = False, stp_lang: str = 'english') -> str:
    stop_words = nltk.corpus.stopwords.words(stp_lang)
    if not text:
        raise CleanTextEmptyString("No text is provided to clean")
    if clean_all:
        while '  ' in text.strip():
            text = text.replace("  ", " ")
        text = "".join([word.casefold() for word in text if word not in string.punctuation])
        text = "".join([_ for _ in text if not _.isdigit()])
        tokens = text.split()
        text = " ".join([ps.stem(word) for word in tokens if word not in stop_words])
        return text.strip()
    else:
        if extra_spaces:
            while '  ' in text.strip():
                text = text.replace("  ", " ")
        if lowercase:
            text = text.casefold()
        if numbers:
            text = "".join([_ for _ in text if not _.isdigit()])
        if punct:
            text = "".join([word for word in text if word not in string.punctuation])

        if stopwords:
            text = text.split()
            text = " ".join([word for word in text if word not in stop_words])
        if stemming:
            text = text.split()
            text = " ".join([ps.stem(word) for word in text])
        return text.strip()

def clean_words(text: str, clean_all: bool = True, extra_spaces: bool = False, stemming: bool = False,
                stopwords: bool = False,
                lowercase: bool = False, numbers: bool = False,
                punct: bool = False, stp_lang: str = 'english') -> list:
   
    text = clean(text, clean_all, extra_spaces, stemming, stopwords, lowercase, numbers, punct, stp_lang)

    return text.split()
