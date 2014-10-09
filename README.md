Anagrams
========

Given a list of strings, return how many anagrams are present

Time complexity:

In the order of  O(n (q log q)), where n is the size of the list
and q is the length of the longest string.  This is due to the fact
that my heaviest opperation sorts the letters in a string, while
itterating over all the strings.  I'm sure I can do better.  I'm
particularly opposed to having create a copy list to do my comparisons.
TODO: Decrease O() time complexity   


