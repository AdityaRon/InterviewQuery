# Given a list of stop words, write a function stopwords_stripped that takes a string and returns a string stripped of the stop words with all lower case characters.

# Example:

# Input:

# stopwords = [
#     'I', 
#     'as', 
#     'to', 
#     'you', 
#     'your', 
#     'but', 
#     'be', 
#     'a',
# ]

# paragraph = 'I want to figure out how I can be a better data scientist'


def stopwords_stripped(paragraph:str, stopwords:list[str])-> str:
    updated_paragraph = []
    paragraph_list = paragraph.strip().split(' ')
    for word in paragraph_list:
        if word not in stopwords:
            updated_paragraph.append(word.lower())
    return ' '.join(updated_paragraph)    
