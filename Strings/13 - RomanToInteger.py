def romanToInt(self, s: str) -> int:
	hash_table = {'I': 1, 'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
	total = 0
	prev = 0
	for letter in reversed(s):
		if hash_table[letter] < prev:
			total -= hash_table[letter]
		else:
			total += hash_table[letter]
		if hash_table[letter] > prev:
			prev = hash_table[letter]
	return total