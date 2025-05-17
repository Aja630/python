# frozenset:-
# .collection of unordered unique elements.
# .represent through frozenset() with comma seperated element.set
# indexing not supported
# slicing not supported
# immutable in nature

l1=[10,20,10,30,20,40]
l2=[2,4,6,8]
fs1=frozenset(l1)
fs2=frozenset(l2)
print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.issubset(fs2))
print(fs1.issuperset(fs2))


# print(fs)
# print(type(fs))
# print(sum(fs))

