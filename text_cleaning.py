from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer


def clean_text(input_text: str):
    # TODO: Clean input_text
    # TODO: Lower case the text before processing it
    input_text = input_text.lower()
    input_text = remove_punctuation_marks(input_text)
    input_text = remove_stop_words(input_text)
    return input_text


def remove_stop_words(input_text: str):
    # Remove stop words from input_text
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_text)

    output = [word for word in word_tokens if word not in stop_words]
    return " ".join(output)


def remove_punctuation_marks(input_text: str):
    # Remove punctuation marks from input_text
    tokenizer = RegexpTokenizer(r'\w+')
    output = tokenizer.tokenize(input_text)
    return " ".join(output)
