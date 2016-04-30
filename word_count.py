import re
from collections import Counter


# TODO Trim pre and post book information (Gutenberg project information for example) from text to be analyzed

# Target text to be read (Frankenstein)
INFILE = './pg84.txt'
# 230k+ words from the standard UNIX dict in a local text file ('/usr/share/dict/words')
ENGLISH_WORDS = './english_words.txt'


def main():

    with open(INFILE, 'rt') as fh, open(ENGLISH_WORDS, 'rt') as ed:
        # Read the target text into a string translating all letters to lowercase

        pre_post_text = re.compile("\n{10}")
        blank_line_regex = re.compile("^\n$")
        white_space_regex = re.compile("\s+")
        special_chars_regex = re.compile("[-\"\':;.?!,\(\)\d]+")

        fh = pre_post_text.split(fh.read())[1]

        english_dict = sorted(list(set([eng_word.lower().rstrip('\n') for eng_word in ed.readlines()])))
        word_count = Counter()

        for line in enumerate(line.strip() for line in fh.split('\n') if not blank_line_regex.match(line)):
            dcase_line = line[1].lower()
            dcase_line = special_chars_regex.sub('', dcase_line)

            word_count.update(Counter(white_space_regex.split(dcase_line)))

    # Create a list from counter object
    word_list = [word for word in word_count.items() if word[0] in english_dict]

    # Sort list by word count in descending order
    word_list.sort(key=lambda wc: wc[1], reverse=True)

    # Create a generator expression from list of verified words because I can
    word_gen = (word for word in word_list)

    # Use genexp to print a formatted string of a word and the number of occurrences of said word in the text
    for word in word_gen:
        wc_format = "'{0!s}' * {1!s}"
        print(wc_format.format(word[0], word[1]))

    print(word_list[:10])

if __name__ == '__main__':
    main()
