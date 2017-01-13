def is_palindrome(sentence):
	"""Returns True if sentence is a palindrome, else False."""
	sentence = [l for l in str(sentence).lower() if l.isalnum()]
	for i in range(int(len(sentence)/2)):
		if sentence[i] != sentence[-i-1]:
			return False
	return True

palindromes_test = [
"Don't nod",
"Dogma: I am God",
"Never odd or even",
"Too bad - I hid a boot",
"Rats live on no evil star",
"No trace; not one carton",
"Was it Eliot's toilet I saw?",
"Murder for a jar of red rum",
"May a moody baby doom a yam?",
"Go hang a salami; I'm a lasagna hog!",
"Satan, oscillate my metallic sonatas!",
"A Toyota! Race fast... safe car: a Toyota",
"Straw? No, too stupid a fad; I put soot on warts",
"Are we not drawn onward, we few, drawn onward to new era?",
"Doc Note: I dissent. A fast never prevents a fatness. I diet on cod",
"No, it never propagates if I set a gap or prevention",
"Anne, I vote more cars race Rome to Vienna",
"Sums are not set as a test on Erasmus",
"Kay, a red nude, peeped under a yak",
"Some men interpret nine memos",
"Campus Motto: Bottoms up, Mac",
"Go deliver a dare, vile dog!",
"Madam, in Eden I'm Adam",
"Oozy rat in a sanitary zoo",
"Ah, Satan sees Natasha",
"Lisa Bonet ate no basil",
"Do geese see God?",
"God saw I was dog",
"Dennis sinned"
]

palindromes_bool = map(is_palindrome, palindromes_test)

for p in zip(palindromes_test, palindromes_bool):
	print(p)
print("\nAll of the above are palindromes : " + str(all(palindromes_bool)))