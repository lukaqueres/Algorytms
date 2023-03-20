import doctest


class IsPalindrome:
	"""
	>>> IsPalindrome.fromfile("palindromes.txt")
	{'Kajak': True, 'kamil ślimak': True, 'lubiece eceibul': True, 'a ja nie palindrom': False}
	"""

	def __init__(self):
		pass

	@staticmethod
	def line(text: str) -> bool:
		text = text.replace(" ", "").lower()
		if len(text) % 2 == 0:
			for i in range(int(len(text)/2)):
				if text[i] != text[(i+1)*-1]:
					return False
			return True
		else:
			for i in range(int(len(text)/2)+1):
				if text[i] != text[(i+1)*-1]:
					return False
			return True

	@staticmethod
	def fromfile(file: str) -> dict:
		results = {}
		with open(file, encoding="utf-8") as file:
			while line := file.readline().rstrip():
				results.update({line: IsPalindrome.line(line)})
		return results


doctest.run_docstring_examples(IsPalindrome, globals())
