def mergeAlternately(self, word1: str, word2: str) -> str:
	ret = list(word1)
	for i in range(1, len(word2)+1):
		ret.insert(i*2-1, word2[i-1])
	return "".join(ret)