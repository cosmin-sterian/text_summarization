from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean_text(input_text: str) -> list[str]:
    # TODO: Clean input_text
    # TODO: Lower case the text before processing it

def remove_stop_words(input_text: str) -> list[str]:
    # TODO: Remove stop words from input_text
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_text)

    output = [word for word in word_tokens if word not in stop_words]
    return output

def remove_punctuation_marks(input_text: str) -> list[str]:
    # TODO: Remove punctuation marks from input_text

def remove_additional_blanks(input_text: str) -> list[str]:
    # TODO: Remove additional blank spaces from input_text
