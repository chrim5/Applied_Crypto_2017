from DESSBoxes import DESSBoxes

a1 = DESSBoxes().s2_p1_xor_s2_p2('000001', '000011')
b1 = DESSBoxes().s2_p1_xor_p2('000001', '000011')

a2 = DESSBoxes().s2_p1_xor_s2_p2('101011', '111110')
b2 = DESSBoxes().s2_p1_xor_p2('101011', '111110')

a3 = DESSBoxes().s2_p1_xor_s2_p2('001010', '000011')
b3 = DESSBoxes().s2_p1_xor_p2('001010', '010101')

print 'S2(p1) XOR S2(p2): %d' % a1, 'S2(p1 XOR p2): %s' % b1
print 'S2(p1) XOR S2(p2): %d' % a2, 'S2(p1 XOR p2): %s' % b2
print 'S2(p1) XOR S2(p2): %d' % a3, 'S2(p1 XOR p2): %s' % b3