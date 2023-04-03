import doctest

from typing import Any


class Lider:
	"""
	>>> Lider.get([1, 2, 3, 4, 5, 1, 1, 1, 1, 1])
	1
	>>> Lider.get([1, 2, 3, 4, 1, 1])

	>>> Lider.get([10, 2, 13, 2, 102, 2, 234, 2, 10, 2, 12, 2, 2])
	2
	"""
	@staticmethod
	def __occurrence(array: list) -> dict:
		occurrences = {}
		for element in array:
			try:
				occurrences[element] += 1
			except KeyError:
				occurrences[element] = 1
			except Exception as e:
				raise e
		return occurrences

	@staticmethod
	def get(array: list) -> Any:
		occurrences = Lider.__occurrence(array)
		lider = {"variable": None, "occurrences": 0}
		for variable, occurrences in occurrences.items():
			if lider["occurrences"] < occurrences:
				lider = {"variable": variable, "occurrences": occurrences}
		if lider["occurrences"] <= len(array)/2:
			return None
		return lider["variable"]


doctest.run_docstring_examples(Lider, globals())
