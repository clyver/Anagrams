from anagramAlgorithm import Anagram
"""
Simple test file to ensure quality in our Anagram() class
"""

# Test 1
test1 = Anagram(['Act', 'cat', 'cat', 'dog', 'dog', 'aardvark'])
test1.get_anagrams()
assert test1.num_anagrams == 5, "Test1 failed! Expected 5, received {output}".\
	format(output=test1.num_anagrams)

# Test 2
test2 = Anagram(['ab', 'cat', 'CaT', 'Tac', 'b'])
test2.get_anagrams()
assert test2.num_anagrams == 3, "Test2 failed! Expected 3, received {output}".\
        format(output=test2.num_anagrams)

# Test 3
test3 = Anagram([])
test3.get_anagrams()
assert test3.num_anagrams == 0, "Test3 failed! Expected 0, received {output}".\
        format(output=test3.num_anagrams)

# Test 4
test4 = Anagram(['A'])
test4.get_anagrams()
assert test4.num_anagrams == 0,"Test4 failed! Expected 0, received {output}".\
        format(output=test4.num_anagrams)

# Test 5
test5 = Anagram(['CAT', 'tac'])
test5.get_anagrams()
assert test5.num_anagrams == 2,"Test5 failed! Expected 2, received {output}".\
        format(output=test5.num_anagrams)
 
