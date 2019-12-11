import hashlib

plain = ''                                                                          #Plain text input to be hashed
solution = ''        
filename = open("passW.txt", "r")

#For md5 hash
def hash_md5():
    result = hashlib.md5(plain.encode())
    print("The hexdecimal equivalent of the md5 hash is: ", end='')
    print(result.hexdigest())

#For sha1 hash
def hash_sha1():
    result = hashlib.sha1(plain.encode())
    print("The hexdecimal equivalent of the sha1 hash is: ", end='')
    print(result.hexdigest())
    
#For sha224
def hash_sha224():
    result = hashlib.sha224(plain.encode())
    print("The hexdecimal equivalent of the sha224 hash is: ", end='')
    print(result.hexdigest())

#For sha256
def hash_sha256():
    result = hashlib.sha256(plain.encode())
    print("The hexdecimal equivalent of the sha256 hash is: ", end='')
    print(result.hexdigest())

#For sha384
def hash_sha384():
    result = hashlib.sha384(plain.encode())
    print("The hexdecimal equivalent of the sha384 hash is: ", end='')
    print(result.hexdigest())

#For sha512
def hash_sha512():
    result = hashlib.sha512(plain.encode())
    print("The hexdecimal equivalent of the sha512 hash is: ", end='')
    print(result.hexdigest())

#For cracking through md5
def crack_md5():
    for line in filename:
        m = hashlib.md5()
        #cut off '\n' character
        m.update(line[:-1])
        guess = m.hexdigest()
        if guess == solution:
            print(line)
            break

#For cracking throught sha1
def crack_sha1():
    for line in filename:
        m = hashlib.sha1()
        #cut off the '\n' character
        m.update(line[:-1])
        guess = m.hexdigest()
        if guess == solution:
            print(line)
            break

#For cracking through sha224
def crack_sha224():
    for line in filename:
        m = hashlib.sha224()
        #cut off the '\n' character
        m.update(line[:-1])
        guess = m.hexdigest()
        if guess == solution:
            print(line)
            break

#For cracking through sha256
def crack_sha256():
    for line in filename:
        m = hashlib.sha256()
        m.update(line[:-1])
        guess = m.hexdigest()
        if guess == solution:
            print(line)
            break
    
#For cracking through sha384
def crack_sha384():
    for line in filename:
        m = hashlib.sha384()
        m.update(line[:-1])
        guess = m.hexdigest()
        if guess == solution:
            print(line)
            break

#For cracking through sha512
def crack_sha512():
    for line in filename:
        m = hashlib.sha512()
        m.update(line[:-1])
        guess = m.hexdigest()
        if guess == solution:
            print(line)
            break

#Logic to either hash or crack
choice = str(input("Enter whether you wanna hash or decrypt"))
if choice == 'hash':
    plain = input("Enter plain text input")    
    choice_hash = input("Enter which hashing algorithm you wanna use")
    if choice_hash == 'md5':
        hash_md5()
    elif choice_hash == 'sha1':
        hash_sha1()
    elif choice_hash == 'sha224':
        hash_sha224()
    elif choice_hash == 'sha256':
        hash_sha256()
    elif choice_hash == 'sha384':
        hash_sha384()
    elif choice_hash == 'sha512':
        hash_sha512()
elif choice == 'decrypt':
    filename = open("passW.txt", "r")
    solution = input("Enter the solution of the hash you are looking for")             #solution to be decrypted
    choice_decrypt = str(input("Enter the hashing algorithm used to obtain the solution"))
    if choice_decrypt == 'md5':
        crack_md5()
    elif choice_decrypt == 'sha1':
        crack_sha1()
    elif choice_decrypt == 'sha224':
        crack_sha224()
    elif choice_decrypt == 'sha256':
        crack_sha256()
    elif choice_decrypt == 'sha384':
        crack_sha384()
    elif choice_decrypt == '512':
        crack_sha512()






