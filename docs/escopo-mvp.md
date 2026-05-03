# Escopo MVP - Gerador de Senhas Seguras

## Visão Geral

O Gerador de Senhas Seguras é uma aplicação Python que permite a geração de senhas aleatórias e criptograficamente seguras com base em critérios definidos pelo usuário. O MVP (Minimum Viable Product) fornece funcionalidades essenciais para geração, validação e avaliação de força de senhas através de uma interface de linha de comando interativa.

---

## Requisitos Funcionais

### RF01 - Gerar Senha Aleatória
- O sistema deve gerar senhas aleatórias com comprimento personalizável
- O tamanho mínimo permitido é de 4 caracteres
- O tamanho máximo recomendado é de 128 caracteres
- Cada geração deve produzir uma senha única e diferente

### RF02 - Configurar Composição de Caracteres
- O sistema deve permitir a inclusão/exclusão de caracteres especiais
- A senha deve incluir, obrigatoriamente, os seguintes tipos de caracteres:
  - Letras minúsculas (a-z)
  - Letras maiúsculas (A-Z)
  - Dígitos (0-9)
  - Caracteres especiais (opcional): !@#$%^&*()_+-=[]{}|;:,.<>?

### RF03 - Avaliar Força da Senha
- O sistema deve classificar a força da senha em 4 níveis:
  - **Fraca**: tamanho < 8 caracteres
  - **Média**: tamanho entre 8 e 11 caracteres
  - **Forte**: tamanho entre 12 e 15 caracteres
  - **Muito Forte**: tamanho ≥ 12 caracteres com caracteres especiais inclusos

---

## Requisitos Não-Funcionais

### RNF01 - Segurança Criptográfica
- O gerador deve utilizar o módulo `secrets` para garantir aleatoriedade criptograficamente segura
- Deve-se evitar o uso de funções aleatórias não criptográficas (ex.: `random.choice()`)
- As senhas devem ser embaralhadas para evitar padrões identificáveis

### RNF02 - Performance
- O tempo de geração de uma senha não deve exceder 100ms
- A interface deve responder imediatamente aos comandos do usuário
- O consumo de memória deve ser mínimo e constante

### RNF03 - Usabilidade
- A interface deve ser clara e intuitiva em linha de comando
- Mensagens de erro devem ser descriptivas e em linguagem técnica
- O programa deve ser interativo, permitindo múltiplas gerações consecutivas
- Deve permitir encerramento seguro via interrupção (Ctrl+C)

---

## Itens Fora de Escopo

- Armazenamento persistente de senhas geradas
- Integração com gerenciadores de senha (keepass, bitwarden, etc.)
- Interface gráfica (GUI)
- Suporte a múltiplos idiomas
- Validação de senhas contra dicionários de palavras comuns
- Sincronização em nuvem
- Autenticação de usuários
- Auditoria de senhas geradas
- Exportação em formatos específicos (CSV, JSON, etc.)
- Análise avançada de força baseada em entropia
