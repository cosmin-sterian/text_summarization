import text_cleaning
import parser


def main():
    sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good. French-Fries"
    print("".join(text_cleaning.clean_text(sentence)))
    # TODO: Actual stuff
    dataset = parser.read_input()


if __name__ == "__main__":
    main()