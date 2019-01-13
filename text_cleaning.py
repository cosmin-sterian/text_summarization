from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer


def stem(input_sentences: list):
    stemmer = PorterStemmer()
    result = [[stemmer.stem(word) for word in sentence] for sentence in input_sentences]
    return result


def get_all_words(input_sentences: list):
    result = []
    for sentence in input_sentences:
        result += sentence
    return result


def clean_text(input_text: str):
    # Clean input_text
    # Lower case the text before processing it
    input_text = input_text.lower()
    result = keep_words_only(input_text)
    result = remove_stop_words(result)
    return result


def remove_stop_words(input_text: str):
    # Remove stop words from input_text
    stop_words = set(stopwords.words('english'))
    # Split into sentences first because of Task 3
    sentences = sent_tokenize(input_text)
    output = []
    for sentence in sentences:
        word_tokens = word_tokenize(sentence)
        word_tokens = [word for word in word_tokens if word not in stop_words]
        output.append(word_tokens)

    return output


def keep_words_only(input_text: str, result_as_list=False):
    # Tokenizer to keep words only
    # can be used to remove punctuation marks
    tokenizer = RegexpTokenizer(r'\w+')
    output = tokenizer.tokenize(input_text)
    if result_as_list:
        return output
    return " ".join(output)
