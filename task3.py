#(1)
d1={"a":100}
d2={"x":200}
d=d1.copy()
d.update(d2)
print(d)

#(2)
d1={"a":100,"b":200,"c":300}
del d1['a']
print(d1)

#(3)
keys=['red','yellow','blue']
value=['23','34','78']
color=dict(zip(keys,value))
print(color)

#(4)
set=(2,3,4,5,6,7,8,9,0)
print(len(set))

#(5)
sn1={1,2,3,4,5,6}
sn2={3,6,9,12,15}
sn1.difference_update(sn2)
print(sn1)
#otherway
print(sn1-sn2)