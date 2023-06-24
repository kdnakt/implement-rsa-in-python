# prime1
p = 16319982204738582023
# prime2
q = 15332710240271036219

e = 65537
n = p * q
d = pow(e, -1, (p - 1) * (q - 1))

m = 0x112233445566778899aabbccddeeff00

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

cipher_text = rsa_encrypt(m, e, n)

print(f'c = {hex(cipher_text)}')
assert cipher_text != m

plain_text = rsa_decrypt(cipher_text, d, n)

print(f'm = {hex(plain_text)}')
assert plain_text == m

# Signature and Verification
signature = rsa_decrypt(m, d, n)

print(f's = {hex(signature)}')
assert signature == 0x16a5e20ab5c627718cef95451e358dab

verification = rsa_encrypt(signature, e, n)

print(f'v = {hex(verification)}')
assert verification == m
