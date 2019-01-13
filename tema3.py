import text_cleaning
import parser
from math import log
import json
from nltk import pos_tag


def compute_sentences_scores(vocabulary, dataset, headline_similarity_influence):
    sentences_scores = {}
    for headline, _, ctext in dataset:
        article_sentences = text_cleaning.clean_text(ctext)  # [[words]]
        article_sentences = text_cleaning.stem(article_sentences)
        headline_sentences = text_cleaning.clean_text(headline)
        headline_sentences = text_cleaning.stem(headline_sentences)
        headline_words = set(text_cleaning.get_all_words(headline_sentences))
        count_article_words_in_headline = 0
        for i, sentence in enumerate(article_sentences, start=1):
            sentence_score = 0
            nouns_count = 0
            # 3.1: Compute score using Nouns only
            tagged_sentence = pos_tag(set(sentence))
            for word, pos in tagged_sentence:
                if word in vocabulary and pos[:2] == 'NN':  # word is Noun
                    nouns_count += 1
                    tf, idf = vocabulary[word]
                    sentence_score += tf * idf  # TODO: Check if correct
                    if word in headline_words:  # 3.2: Compute additional score if words from headline
                        count_article_words_in_headline += 1
            sentence_score /= nouns_count # Normalize it
            sentences_scores[' '.join(sentence)] = \
                (sentence_score +
                 (count_article_words_in_headline / len(headline_words))*headline_similarity_influence)\
                * (i / len(article_sentences))  # 3.3 sentence's location in text weight

    return sorted(sentences_scores.items(), key=(lambda d: d[1]), reverse=True)[:3]


def compute_tf_idf(dataset):
    # dataset = [headlines, text, ctext]
    vocabulary = {}  # {word: (tf, idf)}
    ctext_words = []  # list of words in each document, sort of a [document_words]
    dataset_sentences = []
    for _, _, ctext in dataset:
        sentences = text_cleaning.clean_text(ctext)  # [[words]]
        sentences = text_cleaning.stem(sentences)
        dataset_sentences.append(sentences)
        words = text_cleaning.get_all_words(sentences)
        ctext_words.append(set(words))

        for word in words:
            if word not in vocabulary:
                vocabulary[word] = (1, 0)
            else:
                tf, idf = vocabulary[word]
                vocabulary[word] = (tf + 1, idf)

    print("Done computing TF")

    for word in vocabulary:
        tf, _ = vocabulary[word]
        occurrences = 0
        for words in ctext_words:
            if word in words:
                # Found a document that contains word, so we increase the idf count
                occurrences += 1
        vocabulary[word] = (tf, log(len(ctext_words) / occurrences))

    print('Done with IDF')
    return vocabulary, dataset_sentences


def main():
    # Tasks 1. and 2.: Clean text and compute TF-IDF
    dataset = parser.read_input()  # [headlines, text, ctext]
    print("Computing TF-IDF for words")
    vocabulary, dataset_sentences = compute_tf_idf(dataset)  # {word: (TF, IDF)}

    # Task 3: Compute sentence score
    print("Computing sentences scores")
    sentences = compute_sentences_scores(vocabulary, dataset, 0.1)
    write_top3_sentences(sentences)


def write_top3_sentences(sentences, path='sentences_top3.txt'):
    out_file = open(path, 'w')
    for sentence, score in sentences:
        out_file.write(sentence + '\nScore: ' + str(score) + '\n\n')
    out_file.close()
    print('Sentences saved to file', path)


def write_to_file(vocabulary, path='vocabulary.txt'):
    out_file = open(path, 'w')
    out_file.write(json.dumps(vocabulary))
    out_file.close()


if __name__ == "__main__":
    main()