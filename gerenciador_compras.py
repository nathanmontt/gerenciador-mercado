import datetime
from time import sleep
from reportlab.pdfgen import canvas

# PDF CONFIG
pdf_file_name = "lista_compras.pdf"
doc_file_title_name = "LISTA DE COMPRAS"

complete_date = f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}"

doc_file_subtitle_name = f"Lista de compras do dia {complete_date}"

shopping_cart = []
print("BEM-VINDO(A) AO NOSSO MERCADO!")

while True:
    menu_options = input("Digite uma opção para seu carrinho de compras:\n1 - Adicionar\n2 - Remover um item\n3 - Limpar lista de compras\n4 - Ver Lista\n5 - Download (.pdf)\n6 - Sair\n: ").strip()
    match menu_options:
        case "1": # adicionar itens
            while True:
                item_add = input("Digite um produto ou 'sair' para voltar ao menu: ").strip()
        
                if item_add.lower() in ("sair", "cancelar"):
                    break
        
                item_add = item_add.capitalize()
        
                if (item_add in shopping_cart or len(item_add) <= 2 or any(caractere.isdigit() for caractere in item_add)):
                    print("Item inválido ou repetido.")
                    continue
        
                shopping_cart.append(item_add)
                print("Adicionando o produto", end="")
                for i in range(3):
                    sleep(.3)
                    print(".", end="")
                print(f"\n{item_add} foi adicionado.")

        case "2": # remover um item específico
            if (shopping_cart == []):
                print("Lista vazia.\nAdicione produtos para excluí-los")

            while True:
                remove_cart_item = input("Digite o item que deseja remover ou 'sair' para voltar ao menu: ").strip()
                if remove_cart_item.lower() in ("sair", "cancelar"):
                    break
                remove_cart_item = remove_cart_item.capitalize()
                
                if remove_cart_item in shopping_cart:
                    shopping_cart.remove(remove_cart_item)
                    print("Removendo item", end="")
                    for i in range(3):
                        sleep(.3)
                        print(".", end="")
                    print(f"\n{remove_cart_item} foi removido.")
                else:
                    print("Escolha um item que esteja na lista para excluir")
                    continue
                
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

        case "5": # download pdf
            pdf = canvas.Canvas(pdf_file_name)

            # title
            pdf.setTitle(doc_file_title_name)
            pdf.setFontSize(18)
            pdf.drawCentredString(300, 770, doc_file_title_name)

            # subtitle
            pdf.setFontSize(12)
            pdf.drawCentredString(300, 740, doc_file_subtitle_name)
            # altura = 770
            # for cont, product in enumerate(shopping_cart, start=1):
            #     pdf.drawString(100, altura, f"{cont} - {product}")
            #     altura -= 20
            pdf.save()
            print(f"PDF criado: {pdf_file_name}")

        case "6": # sair
            print("Obrigado por usar os serviços do NOSSO MERCADO! ATÉ LOGO!")
            break
        
        case _:
            print("Opção não encontrada.\n")