# Atividade_Semana6

Nessa atividade eu devia fazer a comparação entre os algoritmos de hash SHA-256 e de criptografia simétrica AES-256 em Python.

## Métodos utilizados
**SHA-256 (Secure Hash Algorithm 256):** Este algoritmo é uma função de hash criptográfica que produz um hash a partir de uma entrada de dados. O SHA-256 é muito utilizado para garantir a integridade dos dados, pois mesmo uma pequena mudança na mensagem resultará em uma sequência completamente diferente.

**AES-256 (Advanced Encryption Standard 256):** Este é um algoritmo de criptografia simétrica que usa uma chave secreta para criptografar e descriptografar dados. O AES-256 é considerado altamente seguro e é amplamente utilizado em sistemas de segurança devido à sua robustez e eficácia. O processo de criptografia simétrica é geralmente mais rápido do que o da criptografia assimétrica, tornando-a ideal para criptografar grandes volumes de dados em sistemas que precisam de alta velocidade de processamento.

## Resultados Obtidos
Os testes foram realizados utilizando uma lista de palvras de testes com palavras-chave no AES-256 e uma lista de palavras para serem hashadas pelo SHA-256. Os resultados obtidos foram registrados em uma tabela, que inclui o número do teste, a palavra de teste, o hash SHA-256, o texto criptografado usando AES-256, a palavra-chave AES-256 utilizada e o texto descriptografado.

Acredito que a principal diferença entre os dois é que o SHA-256 não dá para descriptografar e o AES-256 dá, pois utiliza uma chave para isso.

## Tabela de Resultados:
Essa tabela apresenta os resultados dos testes realizados, incluindo o número do teste, a palavra de teste, o hash SHA-256, o texto criptografado usando AES-256, a palavra-chave AES-256 utilizada e o texto descriptografado.

| Número do teste | Teste                   | SHA-256                                                          | AES-256 (Criptografado)                           | Palavra-chave AES-256 | AES-256 (Descriptografado) |
|-----------------|-------------------------|------------------------------------------------------------------|--------------------------------------------------|------------------------|----------------------------|
| 1               | Celine                  | c959af3162393c9d72e5de0a3d3681f742246f8625df4cda9bea482503331f22 | 7db430509777                                      | Nome                   | Celine                     |
| 2               | Souza                   | c988444841ebbdb16ffc457bb9cd0de514d15d677a7a7fda419ccc85e0fffce5 | 8dfd7186c1                                        | Sobrenome              | Souza                      |
| 3               | Sistemas da Informação  | 7d719e9db29ad79e1157ad448423e300a40dbfd6b75dc5dea6c582cc8e822d36 | 31a5e2fe1e148afc2006439d50b12e96b7b58e4f6da7a139 | Curso                  | Sistemas da Informação    |
| 4               | Manaus                  | d6c2e8f87879ae81e45938f26dfebad6c20e8ebe8f38cf725f271446ae945906 | 251439eff0e0                                      | Cidade                 | Manaus                     |
| 5               | Amazonas                | 21a02fb6a7e1c4524a5ee293687a78d524a5ddebef2a6073684c227eaf4918da | 7312c08c3f17a78e                                  | Estado                 | Amazonas                   |
| 6               | Brasil                  | 6641c5a7ff9f56ef2baceefb41d9906583b9816a7b3e9c4c23773646be584caf | cb5c0b61bfe1                                      | Nacionalidade          | Brasil                     |
| 7               | Sustentabilidade        | 9f032a34d9e40bf2e6ecdfa574693726e9e2742540cef3fa0ac0b6b2ec194c12 | 6245ef62fb457bdece9f64f64962a5da                  | Interesse1             | Sustentabilidade           |
| 8               | Tecnologia              | 735197da557e725c54b7784f7fb14918f9fa563c1b82b7dff726e064839ff3e2 | 691d2e418425767f1e88                              | Interesse2             | Tecnologia                 |
| 9               | Natureza                | f58c2019b3037ba487f04d9adbffe8cfb855aaa993aa6b449baea92046ece21f | 85080cd810200d93                                  | Interesse3             | Natureza                   |
| 10              | Vinte                   | ee718f155de32aee742b0c4b48fbff00de1beee9f595ded81e2f68d1ba0af139 | 40438c2fbd                                        | Idade                  | Vinte                      |

