#Week 1 Test

# For file with only numbers, you should only return one thing(i.e.the first 10 characters)

# For file with story,you NEED to return two things(i.e. a modified string AND a list)
#  you can return multiple values by simply return them separated by commas like the following
# def editor(fname):
#
#     return 'modifystring', [a,b,c,d]

# HINT: to call your function for the story.txt file, use the following command
# editor("./data/story.txt")
# return statement should be in the format below
# return 'modifystring', [a,b,c,d]



import re
from collections import Counter

def editor(filepath):
    
    import re
    from collections import Counter
    with open(filepath, 'r') as file:
        content = file.read()

    if content.isdigit():
        modified_string = content[:10]
        top_5_words = []
        return modified_string
    else:
        modified_string = content.lower().strip()
        words = re.findall(r'\b\w+\b', modified_string)
        word_counts = Counter(words)
        top_5_words = [word for word, _ in word_counts.most_common(5)]
        return modified_string, top_5_words