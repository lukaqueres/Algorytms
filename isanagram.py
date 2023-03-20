import doctest


class IsAnagram:
	"""
	>>> IsAnagram.from_file("anagrams.txt")
	{0: True, 1: False, 2: True}
	"""
	def __init__(self):
		pass

	@staticmethod
	def __occur(string: str) -> dict:
		occur = {}
		string = string.replace(" ", "").lower()
		for character in string:
			if character not in list(occur.keys()):
				occur.update({character: 1})
			else:
				occur[character] += 1
		return occur


	@staticmethod
	def check(word, check) -> bool:
		return IsAnagram.__occur(word) == IsAnagram.__occur(check)

	@staticmethod
	def from_file(file) -> dict:
		results = {}
		with open(file, encoding="utf-8") as file:
			i = 0
			while line := file.readline().rstrip():
				words = line.split(":")
				results.update({i: IsAnagram.check(words[0], words[1])})
				i += 1
		return results

doctest.run_docstring_examples(IsAnagram, globals())
