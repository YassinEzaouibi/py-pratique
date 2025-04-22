import random

# key generation
p=31824857602791436829133356369130484362073194100393695426222717513365410026323
g=2
# m=random.randint(1,p-1)
m= 10822443882941918350854756353817808703822700689763830800201289217574157439544

x=random.randint(2,p-2)
beta=pow(g,x,p)
# k_pub = (p,g,beta)
# k_prv = (x)

k=random.randint(2,p-2)
c_1 = pow(g,k,p)
c_2 = (m * pow(beta,k,p)) % p
# c = (c_1, c_2)
print(f'c1:' , c_1, 'c2: ',c_2)

msg = (c_2*pow(c_1,-x,p)) % p
print(f'message: ',msg)