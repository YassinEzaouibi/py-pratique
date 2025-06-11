
def discrete_log_bruteforce(g, b, p):
    for a in range(p):
        if pow(g, a, p) == b:
            return a
    return None  # not found

p=29
g=2
b=8
# a=random(p) = 2614443797

# trover a

a = discrete_log_bruteforce(g, b, p)
print(a)