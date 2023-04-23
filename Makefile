des: DES.c 
	gcc DES.c -o DES
aes_encrypt: AES_encrypt.c
	gcc AES_encrypt.c -o AES_encrypt
aes_decrypt: AES_decrypt.c
	gcc AES_decrypt.c -o AES_decrypt 
RSA: RSA.c
	gcc RSA.c -o RSA
SHA1: SHA1.c
	gcc SHA1.c -o SHA1
MD5: MD5.c 
	gcc MD5.c -lm -o MD5
clean:
	@rm -f DES AES_encrypt AES_decrypt RSA SHA1 MD5
