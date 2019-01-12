from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer


def stem(input_words: list):
    result = []
    stemmer = PorterStemmer()
    for word in input_words:
        result.append(stemmer.stem(word))
    return result


def clean_text(input_text: str):
    # TODO: Clean input_text
    # TODO: Lower case the text before processing it
    input_text = input_text.lower()
    input_text = keep_words_only(input_text)
    input_text = remove_stop_words(input_text)
    return input_text


def remove_stop_words(input_text: str):
    # Remove stop words from input_text
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_text)

    output = [word for word in word_tokens if word not in stop_words]
    return " ".join(output)


def keep_words_only(input_text: str, result_as_list=False):
    # Tokenizer to keep words only
    # can be used to remove punctuation marks
    tokenizer = RegexpTokenizer(r'\w+')
    output = tokenizer.tokenize(input_text)
    if result_as_list:
        return output
    return " ".join(output)
