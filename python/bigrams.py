# Write a function called find_bigrams that takes a sentence or paragraph of strings and returns a list of all its bigrams in order.

# Note: A bigram is a pair of consecutive words.

def find_bigrams(sentence):
    senetence_list = sentence.lower().strip().split(" ")
    result = []
    temp = senetence_list[0]
    for word in senetence_list[1:]:
        if word != '':
            result.append(tuple([temp, word]))
            temp = word
    return result
