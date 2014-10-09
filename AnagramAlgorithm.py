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
		
		for elem in self.list:
			# Get the index of this element
			index = self.list.index(elem)
			
			# Sort this element
			elem = sorted(elem)
	
			# We say an elem has not been matched until it is
			matched = False		
	
			# Iterate over elements in search of anagram mathces	
			for compare_elem in self.list:
				# Two strings are anagrams if equal when sorted
				if elem == sorted(compare_elem):
					# If equal, add to count, pop from list
					matched = True
					self.num_anagrams += 1
					index2 = self.list.index(compare_elem)
					self.list.pop(index2)
			
			# If this elem was matched, let's not forget to give it credit
			if matched:
				self.num_anagrams += 1
			self.list.pop(index)
							
