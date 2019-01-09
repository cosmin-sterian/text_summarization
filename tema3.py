import nltk
import text_cleaning


def main():
    sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good. French-Fries"
    print("".join(text_cleaning.clean_text(sentence)))
    # TODO: Actual stuff


if __name__ == "__main__":
    main()