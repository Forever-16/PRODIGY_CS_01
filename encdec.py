# CEASER CYPHER ALGORITHM FOR DATA ENCRYPTION
def encrypt_fn(txt,s):
    txt = txt.lower()
    et=""
    for i in range(len(txt)):
            char=txt[i]
            if(char==" "):
               et+=" "
            else:
               sv=ord(char)+s-97
               et+=chr((sv%26)+97)
    return et
def decrypt_fn(et,s):
    dt=""
    for i in range(len(et)):
            char=et[i]
            if(char==" "):
               dt+=" "
            else:
               sv=ord(char)-s-97
               dt+=chr((sv%26)+97)
    return dt
text=input("Enter a string: ")
shift_key=int(input("Enter the shift value : "))
encrypted_text = encrypt_fn(text,shift_key)
print("Original string: ",text)
print("After encryption : ",encrypted_text)
decrypted_text = decrypt_fn(encrypted_text,shift_key)
print('After decryption: ',decrypted_text)