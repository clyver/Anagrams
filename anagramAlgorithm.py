__author__="ChristopherLyver"
import pdb
class Anagram():
	"""
	Class contains the utilities and resources to run the 'Anagram Problem'
	"""

	def __init__(self, input_list):
		self.list = input_list
		self.len = len(self.list)
		self.num_anagrams = 0

	def get_anagrams(self):
		"""
		Return the number of anagrams present in the list of strings.
		We are case insensitive. 
		"""
		molded_list = []

		# Go through each element.  Sort its letters and lower case it
		for elem in self.list:
			elem = elem.lower()
			elem = ''.join(sorted(elem))
			# add the elem to the list we will work with
			molded_list.append(elem)

		# While we still have elements to match:
		while molded_list:
			# The element we will check for anagrams:
			our_head = molded_list[0]
			# The number of times the head occurs in our copy list:
			occurrences = molded_list.count(our_head)
			
			if occurrences > 1:
				# If > 1, we have anagrams. Count em'!
				self.num_anagrams += occurrences
			# Remove the instanes of the head and continue comparing
			molded_list = [elem for elem in molded_list\
					 if elem != our_head]

