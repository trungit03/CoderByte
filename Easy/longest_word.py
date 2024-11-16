
import re
def LongestWord(sen):
    # current_word = ""
    # longest_word = ""
    # for char in sen:
    #     if re.match(r'^[a-zA-Z0-9]+$', char):
    #         current_word += char
    #     else:
    #         if(len(current_word) > len(longest_word)):
    #             longest_word = current_word
            
    #         current_word = ""
    # if len(current_word) > len(longest_word):
    #     longest_word = current_word

    # return longest_word

    words = re.findall(r'\b[a-zA-Z0-9]+\b', sen)
    if not words:
        return " "
    longest = sorted(words, key=len, reverse=True)

    if len(longest) > 1 and len(longest[0]) == len(longest[1]):
        return longest[0]
    return longest[0]
print(LongestWord('kdljs!! dsa'))
print(LongestWord('d dsad ekwlekqwlekqw dsadasdasaaaaafds'))