# from Crypto.Cipher import AES
# import binascii

# encrypted_hex = "8b0e85bdeb1f4c54d1ebcfd6b11f0248e7a73a334a9aca802fdc7a224f33a7bafc6c577eeae43b94402db4e1a3d322c9"

# key = b"supersecretkeyyy"  
# iv = b"IV_cbc" + b"\x00" * 10  

# encrypted_data = binascii.unhexlify(encrypted_hex)

# cipher = AES.new(key, AES.MODE_CBC, iv)

# decrypted_data = cipher.decrypt(encrypted_data)

# try:
#     decrypted_text = decrypted_data.decode("utf-8").rstrip("\x00")  
#     print("Decrypted text:", decrypted_text)
# except UnicodeDecodeError:
#     print("Decrypted binary data:", decrypted_data)






#--------json working or 

# jsonEx = {
#     "name" : "pratham" ,
#     "siucces" : True
# }

# print(jsonEx["name"])

# for key,value in jsonEx.items() :

#     print(f"{key} : {value}")





#----------lists

# list = [1 , 2 ,3 ,4]
# print(list.count(22)) # counting each element 
# print(len(list)) # getting the total number 


# for i in list :
#     print(i)


# print(list.clear()) #clearning the list 


# print(f"this is the list {list}") 





