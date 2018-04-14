def encrypt_once(text):
    return text[1::2] + text[0::2]

def encrypt(text, n):
    if(text == None):
        return None
    
    l = len(text)
    if(n > 0 or l > 1):
        i = 0
        while(i < n):
            text = encrypt_once(text)
            i=i+1
    return text

def decrypt_once(text):
    l = len(text)
    hl = l // 2
    even = text[hl:l]
    odd = text[0:hl]
    dec_once = ""
    for i in range(hl):
        dec_once += even[i] + odd[i]
    if(l%2 != 0):
        dec_once += even[-1]
    return dec_once

def decrypt(encrypted_text, n):
    if(encrypted_text == None):
        return None

    l = len(encrypted_text)
    decrypted_text = encrypted_text
    if(n > 0 or l > 1):
        i = 0
        while(i < n):
            decrypted_text = decrypt_once(decrypted_text)
            i=i+1
    return decrypted_text

def decrypt_simpler(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text

def encrypt_simpler(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

text = [str(i) for i in input().split()]
print(text)