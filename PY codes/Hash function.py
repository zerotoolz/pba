import hashlib
with open("PATH to file","rb") as f:
    bytes = f.read()
    hash = hashlib.sha3_256(bytes).hexdigest(); 
    print(hash)