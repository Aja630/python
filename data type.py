
# Numeric data type==>
# Integer Data type :--

# x=10
# print(x)
# print (type(x))

# Float data type:---

# x=10.5
# print(x)
# print (type(x))

# Complex data type:--

# x=10+2j
# print(x)
# print (type(x))


# x=10
# print(max(2))
# print(min(x))
# print(len(x))
# print(x)
# print(id(x))
# print(type(x))


# s='python'
# print(max(s))
# print(min(s))
# print(len(s))
# print(type(s))
# print(id(s))
# print(s)


# s="This is a python class"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())
# print(s.center(100))
# print(s.center(100,'!'))



# 'join' and 'split' interview me puchi jaati hai
# s1= 'Ajay'
# s2= 'ahirwar'
# print(' '.join(s1))
# print(' '.join((s1,s2)))
# print(' '.join((s1,s2)))


# s= 'This is python class'
# print(s.split())
# print(s.split('s'))
# print(s.split('s',0))
# print(s.split('s',2))


# method of list

# copy()
# clear()
# sort()
# reverse()
# count()

# //count
# l=[10,20,30,10,50,60]
# print(l.count(10))      # //calculate frequency

# //sort
# l=[10,30,5,20]
# l.sort()
# print(l)


# //reverse
# l=[3,4,4,]
# l.reverse


# //copy
# l=[1,3,5,6]
# l1=l.copy()
# print(l)
# print(l1)
# print(id(l),id(l1))



# l.clear()
# print(l)

# l.clear()
# x=l
# print(l)
# print(id(x))


# del(l)
# print(l)


# //Tuple==>collection of ordered progreous as well as hetrogeneous elements

# .represented through () with comma seperated objects
# .indexing supported
# .slicing supported
# .immutable in nature

# ex => 
# t= (2,3,6,3,1,5)
# print(t)
# print(id(t))


# t=(2,4,6,'python')
# print(len(t))
# print(sum(t))
# print(max(t))

# t=(10,20,30,'python',40)
# print( t.index('python'))


# //Dictionary=> collection of key value pairs
#   =>key must be unique
#   =>value may be duplicate
#   =>represented through {} with comma seperated pairs
#   =>indexing not supported 
# =>slicing not supported
# =>mutable in nature

# d={1:'ajay',2:21,3:'B.tech'}
# print(len(d))
# print(max(d))
# print(min(d))
# print(sum(d))

# d={2:'ajay', 2:21, '3':'b.tech'}
# print(d)
# d={2:100, 2:21, '3':'b.tech'}
# print(len(d))

d={'name': 'ajay','age':21,'quali':'b.tech'}
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.get('name'))
# print(d.get('age'))
# d.pop('age')
# print(d)
# d.popitem()
# print(d)

# l=[1,2,3,'z','p','q','r']
# d=dict.fromkeys(l,10)
# print(d)
# (d.setdefault('name','rahul'))
# print(d)
# d.copy()
# print(d)
d.clear()
print(d)