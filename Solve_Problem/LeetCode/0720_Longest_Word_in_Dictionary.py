from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set()
        result = ""
        words.sort() # to obtain result in the smallest lexical order
        for word in words:
          if len(word)==1 or word[:-1] in word_set: # This is a trie concept, which means that word[:-1] is in word_set.
            if len(result) < len(word):
              result = word
            word_set.add(word)
        return result

words = list(read().rstrip().split(','))
mod = Solution()
print(mod.longestWord(words))
