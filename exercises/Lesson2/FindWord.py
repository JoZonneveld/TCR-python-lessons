def find_word(sentence, word):
    word_found = 0

    for sentence_part in sentence.split(' '):
        if sentence_part == word:
            word_found += 1
    return word_found


print(find_word('this is the sentence, it will search for the word this', 'this'))