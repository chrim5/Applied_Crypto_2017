from DESSBoxes import DESSBoxes

a1 = DESSBoxes().s2_p1_xor_s2_p2('000001', '000011')
b1 = DESSBoxes().s2_p1_xor_p2('000001', '000011')

a2 = DESSBoxes().s2_p1_xor_s2_p2('101011', '111110')
b2 = DESSBoxes().s2_p1_xor_p2('101011', '111110')

a3 = DESSBoxes().s2_p1_xor_s2_p2('001010', '000011')
b3 = DESSBoxes().s2_p1_xor_p2('001010', '010101')

print a1, b1
print a2, b2
print a3, b3