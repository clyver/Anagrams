from AnagramAlgorithm import Anagram

test1 = Anagram(['Act', 'cat', 'cat', 'dog', 'dog', 'aardvark'])
test1.algorithm()
assert test1.num_anagrams == 5, "Test1 failed! Expected 5, received {output}".\
	format(output=test1.num_anagrams) 
