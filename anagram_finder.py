def import_word_list():
    # word_list = open('word_list.txt', 'r')
    # word_list = open('wordlist_tweaked.txt', 'r')
    word_list = open('/usr/share/dict/words', 'r')
    # for word in word_list:
    # # while word_list:
    #     try:
    #         print(word)
    #     except:
    #         pass

    return [word.strip() for word in word_list ]

def anagram_metric(string):
    #more efficient approach would be to do a census, but on short strings, difference is small.
    sorted_chars = sorted(string)
    return ''.join(sorted_chars)

def anagram_view(list):
    print(', '.join(list))
    return

words = import_word_list()
print(len(words))
anagram_survey = {}
for word in words:
    sorted_word = anagram_metric(word)
    if sorted_word not in anagram_survey:
        anagram_survey[sorted_word] = []
    anagram_survey[sorted_word].append(word)

most_anagrams = 0
most_anagrammable = []
for sorted_word in anagram_survey.keys():
    anagram_count = len(anagram_survey[sorted_word])
    if anagram_count > 1:
        anagram_view(anagram_survey[sorted_word])
    if anagram_count > most_anagrams:
        most_anagrams = anagram_count
        most_anagrammable = anagram_survey[sorted_word]
anagram_view(most_anagrammable)
