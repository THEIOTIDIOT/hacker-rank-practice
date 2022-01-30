
# symmetric difference will subtract any values that are in 
# both sets and leave non duplicates included in resulting set
s = set([1,2,3,4,5,6,7,8,9])
print(len(s.symmetric_difference(set([10,1,2,3,11,21,55,6,8]))))