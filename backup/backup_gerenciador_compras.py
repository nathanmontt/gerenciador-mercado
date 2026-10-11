from time import sleep

'''
1. Gerenciador de Lista de Compras (Foco em Listas)
Um programa de terminal onde o usuário pode adicionar, remover e visualizar itens que precisa comprar.
Como funciona:
- Crie um menu simples em um loop while (Ex: 1-Adicionar, 2-Remover, 3-Ver Lista, 4-Sair).

O que você vai praticar:
- Manipulação de listas (.append(), .remove(), .pop()), loops for para imprimir os itens enumerados e condicionais (if/else) para menus.

Toque para o GitHub:
- Adicione uma funcionalidade de "limpar a lista inteira" e trate o erro caso o usuário tente remover um item que não existe na lista.
'''
print("BEM-VINDO(A) AO NOSSO MERCADO!")

"""
para verificar os repetidos = lower em tudo, ate na lista. depois, para mostragem, captilize
para verificações:
- um caractere ou um numero = repetir
"""

shopping_cart = []

while True:
    menu_options = input("Digite uma opção para seu carrinho de compras:\n1 - Adicionar\n2 - Remover um item\n3 - Limpar lista de compras\n4 - Ver Lista\n5 - Sair\n: ").strip()
    match menu_options:
        case "1": # adicionar itens
            item_add = input("Escreva o item que deseja adicionar no carrinho: ").capitalize().strip()
            shopping_cart.append(item_add)
            # quer adicionar mais um?
            # se sim:
            # verificar se é repetido. se não adiciona
            # se não:
            # cancela
            continue_or_not = input("Deseja adicionar mais um produto? (S/N)\n: ").capitalize().strip()
            while continue_or_not != 'N':
                if (
                    item_add in shopping_cart
                    or len(item_add) <= 2
                    or any(caractere.isdigit() for caractere in item_add)
                    or item_add.isspace()
                ):
                    item_add = input("Item inválido ou repetido. Escreva outro item: ").capitalize().strip()
                else:
                    continue_or_not = input("Deseja adicionar outro produto? (S/N)\n: ").capitalize().strip()
                    shopping_cart.append(item_add)
                # while (
                #     item_add in shopping_cart
                #     or len(item_add) <= 2
                #     or any(caractere.isdigit() for caractere in item_add)
                #     or item_add.isspace()
                # ):
                #     item_add = input("Item inválido ou repetido. Escreva outro item: ").capitalize().strip()
                # shopping_cart.append(item_add)

        case "2": # remover um item específico
            print("LISTA DE COMPRAS")
            if (shopping_cart == []):
                print("Lista vazia.\nAdicione produtos para excluí-los")
            else:
                remove_cart_item = input("Digite o nome do item que deseja remover: ").capitalize().strip()
                if remove_cart_item in shopping_cart:
                    shopping_cart.remove(remove_cart_item)
                else:
                    print("Escolha um item que esteja na lista para excluir")

        case "3": # limpar a lista
            if (shopping_cart == []):
                print("Carrinho vazio.\nAdicione produtos caso queira eliminá-los!\n")
            else:
                shopping_cart.clear()
                print("Limpando a lista de compras", end="")
                for i in range(5):
                    sleep(.5)
                    print(".", end="")
                print("\nLista de compras limpa!\nAdicione novos itens!")
 
        case "4": # ver a lista
            cont = 1
            print("LISTA DE COMPRAS")
            if (shopping_cart == []):
                print("Lista vazia.\nAdicione produtos para mostrá-los")
            else:
                for products in shopping_cart:
                    print(f"{cont} = {products}", end="\n")
                    cont+=1
                print("\n")

        case "5": # sair
            print("Obrigado por usar os serviços do NOSSO MERCADO!ATÉ LOGO!")
            break
        
        case _:
            print("Opção não encontrada.\nDigite novamente\n")