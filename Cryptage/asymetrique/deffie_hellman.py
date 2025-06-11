# p et g public
p= 17597
g= 2

# User A
# KprA = a -> {2, ..., p-2}
a= 13559
# KpubA = A
A= pow(g,a,p)

# User B
# KprB = b -> {2, ..., p-2}
b= 11753
# KpubB = B
B= pow(g,b,p)

# Secret keys
KsectB = pow(A,b,p)
KsectA = pow(B,a,p)

print(KsectA)
print(KsectB)




