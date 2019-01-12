import text_cleaning
import parser
from math import log
import json
from threading import Thread


def thread_compute_idf(vocabulary, ctext_words, index, num_threads):
    n = int(len(vocabulary)/num_threads)
    i = 0
    local_vocabulary = {}
    for word in list(vocabulary.keys())[n*index:n*(index+1)]:
        if i % 50 == 0:
            print('[Thread', index, '] word', n*index + i, 'out of ', len(vocabulary), 'thread range:', (n*index, n*(index+1)-1))
        tf, _ = vocabulary[word]
        occurrences = 0
        for words in ctext_words:
            if word in words:
                # Found a document that contains word, so we increase the idf count
                occurrences += 1
        local_vocabulary[word] = (tf, log(len(ctext_words) / occurrences))
        i += 1
    print('Thread', index, 'is done, updating master dict')
    vocabulary.update(local_vocabulary)
    print('Thread', index, 'is done updating')


def compute_tf_idf(dataset):
    # dataset = [headlines, text, ctext]
    vocabulary = {}  # {word: (tf, idf)}
    ctext_words = []  # list of words in each document, sort of a [document_words]
    i = 0
    for _, _, ctext in dataset:
        print(i)
        words = text_cleaning.keep_words_only(ctext, True)
        words = text_cleaning.stem(words)
        ctext_words.append(set(words))
        for word in words:
            if word not in vocabulary:
                vocabulary[word] = (1, 0)
            else:
                tf, idf = vocabulary[word]
                vocabulary[word] = (tf + 1, idf)
        i += 1
    print("Done computing TF")
    i = 0
    # Compute IDF as log(N/docs_with_word)
    # threads = []
    # for i in range(4):
    #     new_thread = Thread(target=thread_compute_idf, args=(vocabulary, ctext_words, i, 4))
    #     new_thread.start()
    #     threads.append(new_thread)
    # for thread in threads:
    #     thread.join()
    for word in vocabulary:
        if i % 1000 == 0:
            print('word', i+1, 'out of', len(vocabulary))
        tf, _ = vocabulary[word]
        occurrences = 0
        for words in ctext_words:
            if word in words:
                # Found a document that contains word, so we increase the idf count
                occurrences += 1
        vocabulary[word] = (tf, log(len(ctext_words) / occurrences))
        i += 1
    print('Done with IDF')
    # TODO: dunno, maybe return vocabulary
    return vocabulary


def main():
    sentence = "At eight o'clock on Thursday morning morning Arthur didn't feel very good. French-Fries"
    print("".join(text_cleaning.clean_text(sentence)))
    # TODO: Actual stuff
    # 1. and 2.: Clean text and compute TF-IDF
    dataset = parser.read_input()  # [headlines, text, ctext]
    vocabulary = compute_tf_idf(dataset)  # {word: (TF, IDF)}


def debug_dump_vocabulary(vocabulary, path='vocabulary.txt'):
    out_file = open(path, 'w')
    out_file.write(json.dumps(vocabulary))
    out_file.close()


if __name__ == "__main__":
    main()