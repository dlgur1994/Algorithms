from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            if len(word) != len(pattern): # I don't have to check if the words and patterns don't match.
                continue
            mapping = {} # Dictionary to store letters and patterns
            ch = [] # List to store the characters I have verified so far
            flag = True
            for i in range(len(pattern)):
                if pattern[i] not in mapping:
                    if word[i] not in ch: # It's when a letter of the word first appears
                        mapping[pattern[i]] = word[i]
                        ch.append(word[i])
                    else: # It's when the letter of the word is mapped differently in the dictionary
                        flag = False
                        break
                else:
                    if mapping[pattern[i]] != word[i]: # This is when the letter of the word is different from that already stored in the dictionary
                        flag = False
                        break
            if flag == True:
                output.append(word)
        return output

# class Solution:
#     def getDif(self, word):
#         dif = []
#         for i in range(len(word)-1):
#             for j in range(i+1,len(word)):
#                 dif.append(ord(word[i])-ord(word[j]))
#         return dif
#
#     def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
#         output = []
#         pat_dif = self.getDif(pattern)
#         for word in words:
#             word_dif = self.getDif(word)
#             flag = True
#             shorter = min(len(pat_dif), len(word_dif))
#             for i in range(shorter):
#                 if (pat_dif[i]==0 and word_dif[i]!=0) or (pat_dif[i]!=0 and word_dif[i]==0):
#                     flag = False
#                     break
#             if flag == True:
#                 output.append(word)
#         return output

words = list(read().rstrip().split(','))
pattern = read().rstrip()
mod = Solution()
print(mod.findAndReplacePattern(words, pattern))
