__author__="ChristopherLyver"

class Anagram():
	"""
	Class contains the utilities and resources to run the 'Anagram Problem'
	"""

	def __init__(self, input_list):
		self.list = input_list
		self.len = len(self.list)
		self.num_anagrams = 0
	def algorithm(self):
		"""
		The meat of the class.
		Go through the list's elements,
		 and determine if anagrams are present
		"""
		# Create a copy so we don't corrupt our class field.
		# This may come in handy as this project grows.	
		our_list = self.list
		
		for elem in our_list:
			# Get the index of this element
			index = our_list.index(elem)
			
			# Sort this element
			elem = sorted(elem)
	
			# Remove this element from the list
			our_list.pop(index)
	
			# We say an elem has not been matched until it is
			matched = False		
	
			# Iterate over elements in search of anagram mathces	
			for compare_elem in our_list:
				# Two strings are anagrams if equal when sorted
				if elem == sorted(compare_elem):
					# If equal, add to count, pop from list
					matched = True
					self.num_anagrams += 1
					index2 = our_list.index(compare_elem)
					our_list.pop(index2)
			
			# If this elem was matched, let's not forget to give it credit
			if matched:
				self.num_anagrams += 1
	
							
