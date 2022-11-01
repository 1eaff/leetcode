class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for s in sentences:
            words = s.split(' ')
            if len(words) > m: m = len(words)
        return m