import hashlib

data = "MIMIT"
hash_obj = hashlib.sha256(data.encode())
print("SHA-256: ", hash_obj.hexdigest())
print("SHA-512: ", hashlib.sha512(data.encode()).hexdigest())

hash_obj = hashlib.sha3_256(data.encode())
print("SHA3-256: ", hash_obj.hexdigest())
print("SHA3-512: ", hashlib.sha3_512(data.encode()).hexdigest())
