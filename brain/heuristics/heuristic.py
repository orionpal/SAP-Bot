# Some information we can use along with their weights:

# turn number : w0
# -> probabilities for pet names
# board space 0 : w1
# -> stats : w1*w'0
# -> effects : w1*w'1
# -> food : w1*w'2
# board space 1 : w2
# -> stats : w2*w'0
# -> effects : w2*w'1
# -> food : w2*w'2
# board space 2 : w3
# -> stats : w3*w'0
# -> effects : w3*w'1
# -> food : w3*w'2
# board space 3 : w4
# -> stats : w4*w'0
# -> effects : w4*w'1
# -> food : w4*w'2
# board space 4 : w5
# -> stats : w5*w'0
# -> effects : w5*w'1
# -> food : w5*w'2

# I'm going to ignore weight combinations for now because a neural net will hopefully simulate that for us and we won't have to think about it