# https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
# prints the sorted symmetric_difference of two sets

a = set(list(map(int, "2 4 5 9".split())))
b = set(list(map(int, "2 4 11 12".split())))

print(*sorted(a.symmetric_difference(b)), sep='\n')
