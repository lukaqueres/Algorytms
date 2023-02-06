import doctest


class Isprime:
    """
    >>> Isprime.check(1223)
    True
    >>> Isprime.check(82724)
    False
    >>> Isprime.check(15269)
    True

    >>> Isprime.check(102300)
    Traceback (most recent call last):
     ...
    ValueError: Number must be in between 0 and 100000
    >>> Isprime.check(-10)
    Traceback (most recent call last):
     ...
    ValueError: Number must be in between 0 and 100000

    >>> Isprime.fromfile("numbers.txt")
    {'87437': False, '23252': False, '35235': False, '613': True, '534': False}
    >>> Isprime.checkall([n for n in range(50)])

    """

    def __init__(self):
        pass

    @staticmethod
    def check(number):
        if number not in range(100000):
            raise ValueError("Number must be in between 0 and 100000")
        n = 2
        isprime = True
        while n * n <= number:
            if number % n == 0:
                isprime = False
                break
            n += 1
        return isprime

    @staticmethod
    def fromfile(file):
        results = {}
        with open(file) as file:
            while number := file.readline().rstrip():
                results.update({number: Isprime.check(int(number))})
        return results

    @staticmethod
    def checkall(numbers):
        primes = [1, 2, 3, 5]
        result = {}
        for p in primes:
            for number in numbers:
                if int(number) % p != 0:
                    numbers.remove(number)
        return numbers




doctest.run_docstring_examples(Isprime, globals())
