# -*- coding: utf-8 -*-
"""atividadeeSemana6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_jAHOLkywdcuyuBdKVRh1Jz4k5vYNN2g
"""

pip install pycryptodome

import hashlib
from Crypto.Cipher import AES
from tabulate import tabulate

def hash_sha256(teste):
    return hashlib.sha256(teste.encode()).hexdigest()

def aes256_criptografar(chave, dados):
    cipher = AES.new(chave, AES.MODE_EAX)
    texto_cifrado, tag = cipher.encrypt_and_digest(dados)
    return texto_cifrado, cipher.nonce, tag

def aes256_descriptografar(chave, nonce, texto_cifrado, tag):
    cipher = AES.new(chave, AES.MODE_EAX, nonce=nonce)
    dados_descriptografados = cipher.decrypt_and_verify(texto_cifrado, tag)
    return dados_descriptografados

def executar_testes():
    palavras_chave = ["Nome", "Sobrenome", "Curso", "Cidade",
                "Estado", "Nacionalidade", "Interesse1",
                "Interesse2", "Interesse3", "Idade"]

    testes = ["Celine", "Souza", "Sistemas da Informação", "Manaus",
             "Amazonas", "Brasil", "Sustentabilidade", "Tecnologia",
             "Natureza", "Vinte"]

    resultados = []
    for i, teste in enumerate(testes):
        chave = hashlib.sha256(palavras_chave[i].encode()).digest()

        # SHA-256
        resultado_sha256 = hash_sha256(teste)

        # AES-256 Criptografar
        texto_cifrado, nonce, tag = aes256_criptografar(chave, teste.encode())
        texto_cifrado_hex = texto_cifrado.hex()

        # AES-256 Descriptografar
        dados_descriptografados = aes256_descriptografar(chave, nonce, texto_cifrado, tag)
        dados_descriptografados_str = dados_descriptografados.decode()

        resultados.append([i + 1, teste, resultado_sha256, texto_cifrado_hex, palavras_chave[i], dados_descriptografados_str])
    return resultados

if __name__ == "__main__":
    resultados_testes = executar_testes()
    cabecalhos = ["Número do teste", "Teste", "SHA-256", "AES-256 (Criptografado)", "Palavra-chave AES-256", "AES-256 (Descriptografado)"]
    print(tabulate(resultados_testes, headers=cabecalhos))
