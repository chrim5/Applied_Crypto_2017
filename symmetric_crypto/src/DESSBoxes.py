class DESSBoxes:
	"""Verify that S-boxes in DES are nonlinear by computing the output for several pairs of inputs.
	S2-box example
			x0000x 	x0001x 	x0010x 	x0011x 	x0100x 	x0101x 	x0110x 	x0111x 	x1000x 	x1001x 	x1010x 	x1011x 	x1100x 	x1101x 	x1110x 	x1111x
	0yyyy0 	15  	1   	8 	    14  	6   	11   	3 	    4 	    9 	    7 	    2 	    13 	    12 	    0   	5   	10
	0yyyy1 	3 	    13  	4   	7 	    15  	2 	    8 	    14   	12   	0 	    1   	10  	6 	    9   	11   	5
	1yyyy0 	0   	14  	7   	11 	    10 	    4   	13  	1   	5   	8   	12 	    6   	9   	3   	2   	15
	1yyyy1 	13  	8   	10  	1    	3   	15  	4   	2 	    11  	6   	7    	12 	    0   	5   	14  	9

	Show that S2(p1) XOR S2(p2) != S2(p1 XOR p2) where XOR is performed bitwise

	XOR table:
	0 0 0
	0 1	1
	1 0 1
	1 1 0

	Args:
		1. p1 = 000001, p2 = 000011
		2. p1 = 101011, p2 = 111110
		3. p1 = 001010, p2 = 010101

	Returns:
	"""
	S2_BOX = [{'0000': '00', 'val': 15}, {'0001': '00', 'val': 1}, {'0010': '00', 'val': 8}, {'0011': '00', 'val': 14},
			  {'0100': '00', 'val': 6}, {'0101': '00', 'val': 11}, {'0110': '00', 'val': 3}, {'0111': '00', 'val': 4},
			  {'1000': '00', 'val': 9}, {'1001': '00', 'val': 7}, {'1010': '00', 'val': 2}, {'1011': '00', 'val': 13},
			  {'1100': '00', 'val': 12}, {'1101': '00', 'val': 0}, {'1110': '00', 'val': 5}, {'1111': '00', 'val': 10},
			  {'0000': '01', 'val': 3}, {'0001': '01', 'val': 13}, {'0010': '01', 'val': 4}, {'0011': '01', 'val': 7},
			  {'0100': '01', 'val': 15}, {'0101': '01', 'val': 2}, {'0110': '01', 'val': 8}, {'0111': '01', 'val': 14},
			  {'1000': '01', 'val': 12}, {'1001': '01', 'val': 0}, {'1010': '01', 'val': 1}, {'1011': '01', 'val': 10},
			  {'1100': '01', 'val': 6}, {'1101': '01', 'val': 9}, {'1110': '01', 'val': 11}, {'1111': '01', 'val': 5},
			  {'0000': '10', 'val': 0}, {'0001': '10', 'val': 14}, {'0010': '10', 'val': 7}, {'0011': '10', 'val': 11},
			  {'0100': '10', 'val': 10}, {'0101': '10', 'val': 4}, {'0110': '10', 'val': 13}, {'0111': '10', 'val': 1},
			  {'1000': '10', 'val': 5}, {'1001': '10', 'val': 8}, {'1010': '10', 'val': 12}, {'1011': '10', 'val': 6},
			  {'1100': '10', 'val': 9}, {'1101': '10', 'val': 3}, {'1110': '10', 'val': 2}, {'1111': '10', 'val': 15},
			  {'0000': '11', 'val': 13}, {'0001': '11', 'val': 8}, {'0010': '11', 'val': 10}, {'0011': '11', 'val': 1},
			  {'0100': '11', 'val': 3}, {'0101': '11', 'val': 15}, {'0110': '11', 'val': 4}, {'0111': '11', 'val': 2},
			  {'1000': '11', 'val': 11}, {'1001': '11', 'val': 6}, {'1010': '11', 'val': 7}, {'1011': '11', 'val': 12},
			  {'1100': '11', 'val': 0}, {'1101': '11', 'val': 5}, {'1110': '11', 'val': 14}, {'1111': '11', 'val': 9}]

	""" Helper function decimal to binary
	Args: Integer value from S2 box
	Returns: String formatted binary value
	"""
	def dec_to_bin(self, x):
		#return int(bin(x)[2:])
		return '{0:b}'.format(x)

	""" Helper function to perform binary xor bitwise
	Args: 2 binary strings
	Returns: String formatted binary value
	"""
	def binary_xor_bitwise(self, x, y):
		result = int(x, 2) ^ int(y, 2)
		return bin(result)[2:].zfill(len(x))

	""" Lookup a decimal value in S2 box and return it as binary
	Args: Binary string
	Returns: String formatted binary value
	"""
	def lookup_table_s2(self, p):
		p = str(p)
		s2_box = self.S2_BOX

		if len(p) == 6:
			outer_bits = p[0] + p[5]
			inner_bits = p[1:5]
		else:
			filled_6_bits = '000000'[:-len(p)] + p
			outer_bits = filled_6_bits[0] + filled_6_bits[5]
			inner_bits = filled_6_bits[1:5]

		for i in s2_box:
			if inner_bits in i and outer_bits in i.values():
				return self.dec_to_bin(i.get('val'))
				break

	""" Calculate S2(p1) XOR S2(p2)
	Args: 2 binary strings
	Returns: String formatted binary value
	"""
	def s2_p1_xor_s2_p2(self, p1, p2):
		#print self.lookup_table_s2(p1), self.lookup_table_s2(p2)
		result =  int(self.binary_xor_bitwise(self.lookup_table_s2(p1), self.lookup_table_s2(p2)))
		return result

	""" Calculate S2(p1 XOR p2)
	Args: 2 binary strings
	Returns: String formatted binary value
	"""
	def s2_p1_xor_p2(self, p1, p2):
		return self.lookup_table_s2(self.binary_xor_bitwise(p1, p2))

	""" Constructor
	Args: self
	Returns:
	"""
	def __init__(self):
		pass