import hashlib
import os
import random
import string

def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    dic = {}
    source = string.ascii_letters + string.digits
    start = ""
    m = hashlib.sha256()
    while True:
        char = random.choice(source)
        start += char
        m.update(char.encode('utf-8'))
        new_hex = m.hexdigest()
        last_k = get_last_k_bit(k, new_hex)
        if last_k in dic:
            x = start
            y = dic.get(last_k)
            break
        dic[last_k] = start
    x = bytes(x, 'utf-8')
    y = bytes(y, 'utf-8')
    print(x,y)
    return (x, y)


def get_last_k_bit(k, a):
    bit = int(a, 16)
    mask = 1 << k
    last_k = bit & (mask - 1)
    return last_k
