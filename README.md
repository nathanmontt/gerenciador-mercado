# Gerenciador de Lista de Compras (CLI)

Um programa de terminal desenvolvido em Python para organizar compras do dia a dia.

O projeto prático foi criado para fixar conceitos fundamentais de Python, com foco em manipulação de listas, loops, estruturas de decisão e tratamento de strings.

## Funcionalidades

- **Adicionar itens:** inserção novos produtos, com validações que impedem entrada de números, itens com menos de 3 caracteres ou produtos repetidos.
- **Remover itens:** exclusão de itens específico da lista, informando caso o usuário tente deletar algo que não exista ou se a lista estiver vazia.
- **Limpar lista:** esvazio do carrinho por completo com uma única ação.
- **Visualizar:** amostragem de todos os itens da lista enumerados e organizados.
- **UI de Terminal:** efeitos de carregamento utilizando a biblioteca `time`.

## _Feats_ Futuras

- [ ] Exportação da lista de compras em formato **PDF**.

## O que foi aprendido e praticado neste projeto
- Estruturas de decisão com _match_ e _case_.
- Manipulação de dados com métodos de lista: _.append()_, _.remove()_ e _.clear()_.
- Validação e formatação de Strings utilizando _.strip()_, _.capitalize()_, _.lower()_ e _list comprehensions_ com _.isdigit()_.
- Importação e uso de bibliotecas nativas _(from time import sleep)_.

## Pré-requisitos

Para rodar o projeto, é necessário ter instalado **Python 3.10 ou uma versão superior** no seu computador.

## 💻 Como clonar e executar para uso próprio

Se você quiser testar ou modificar este projeto na sua máquina, siga os passos abaixo:

1. Abra o seu terminal (ou Git Bash).
2. Clone este repositório executando o comando:
   ```bash
   git clone https://github.com/nathanmontt/gerenciador-mercado.git
3. Entre na pasta do projeto que acabou de ser baixado
    ```bash
    python gerenciador_compra.py
