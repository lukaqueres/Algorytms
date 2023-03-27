import doctest


class Sort:
	"""
		>>> Sort.bubble([10, 20, 15, 123, 54, 32, 9, 54, 10, 23, 20])
		{0: True, 1: False, 2: True}
	"""

	@staticmethod
	def __swap(array: list, *indexes):
		temp = array[indexes[0]]
		array[indexes[0]] = array[indexes[1]]
		array[indexes[1]] = temp
		return array

	@staticmethod
	def bubble(array: list, method: str = "asc") -> list:
		for j in range(len(array)):
			sort = False
			for i in range(len(array)-1):
				n = i+1
				sort = False
				if method == "asc":
					if array[i] > array[n]:
						array = Sort.__swap(array, i, n)
						sort = True
				elif method == "desc":
					if array[i] < array[n]:
						array = Sort.__swap(array, i, n)
						sort = True
				else:
					raise AttributeError(f"Unsupported method {method}")
			if not sort:
				print(f"Sorting interrupted with {sort} on iteration {j}")
				break

		return array


doctest.run_docstring_examples(Sort, globals())
