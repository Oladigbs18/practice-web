# a program to convert a sentence to a word list
def sentence_to_word_list(sentence):
    word_list = sentence.split()
    return word_list

sentence = " I love Python programming"
print(sentence_to_word_list(sentence))

# a program to reverse a word list
def reverse_word_list(word_list):
    word_list.reverse()
    return word_list

word_list = ["I", "love", "Python", "programming"]
print(reverse_word_list(word_list))
