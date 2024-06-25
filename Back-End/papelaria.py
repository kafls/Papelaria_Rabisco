"""AULA 13 - Sistema Papelaria"""
import os
import mysql.connector #drive BD MySQL

#CONEXÃO COM O BANCO DE DADOS
conexaoDB = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="senai",
    database="Papelaria"
)

def imprimir_header():
    os.system('cls')
    print("- " * 20)
    print("*** SISTEMA PAPELARIA ***")
    print("- " * 20)

# cadastrar produtos
def cadastrar():
    imprimir_header() #Cabeçalho
    print("*** CADASTRO DE PRODUTOS ***")
    nome = input("Informe o nome do produto: ")
    descricao = input("Digite a descrição: ")


    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Erro! Preço e quantidade devem ser valores numéricos.")
        return #retorna para o MENU


    #VALIDAÇÃO
    if (not nome) or (not descricao) or (not preco) or (not quantidade):
        print("Erro! Todos os campos devem ser preechidos!")
        return #retorna para o MENU

    if (preco < 0) or (quantidade < 0):
        print("Erro! Preço e quantidade não podem ser menores que ZERO!")
        return #retorna para o MENU

    if len(nome) > 50:
        print("Erro! O nome do produto é maior que 50 caracteres!")
        return #retorna para o MENU
   
    comandoSQL = f'INSERT INTO Produto VALUES (null,"{nome}","{descricao}",{preco},{quantidade})'

    try:
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f"Erro! Falha ao cadastrar: {erro}")
        return

    print("*** OK! Cadastro realizado com sucesso! ")
    cursorDB.close()

# mostrar produtos
def listar():
    imprimir_header()
    print("*** LISTA DE PRODUTOS ***")


    try:
        cursorDB = conexaoDB.cursor()
        cursorDB.execute('SELECT * FROM Produto')
        resultados = cursorDB.fetchall()


        if not resultados:
            print("Não há produtos cadastrados!")
        else:
            for produto in resultados:
                print(f"ID: {produto[0]} - NOME: {produto[1]} - DESCRIÇÃO: {produto[2]} - PREÇO: {produto[3]} - QUANT: {produto[4]}")
                print("- " * 50)
    except mysql.connector.Error as erro:
        print(f"Erro! Falha ao listar: {erro}")


    cursorDB.close()

# buscar produtos
def get_produto(id_produto):
    cursorDB = conexaoDB.cursor()
    comandoSQL = f'SELECT * FROM Produto WHERE idProduto = {id_produto}'
    cursorDB.execute(comandoSQL)
    resultado = cursorDB.fetchone()
    cursorDB.close()
    return resultado

# alterar quantidades
def alterar_quant():
    imprimir_header()
    print("*** ALTERAR QUANTIDADE ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("Erro! ID deve ser numérico.")
        return
   
    produto = get_produto(id_produto)
    if not produto:
        print(f"Produto com o ID {id_produto} não encontrado!")
        return

    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]} - QUANTIDADE ATUAL: {produto[4]}")

    try:
        nova_quantidade = int(input("Informe a nova quantidade: "))
    except ValueError:
        print("Erro! Valor da quantidade deve ser número inteiro!")
        return
    
    if nova_quantidade == produto[4]:
        print("A quantidade informada é igual ao valor atual.")
        return
    if nova_quantidade < 0 or nova_quantidade > 1000:
        print("Erro! Esse valor é inválido.")
        return
    
    try:
        comandoSQL = f'UPDATE Produto SET quantidade = {nova_quantidade} WHERE idProduto = {id_produto}'
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'Erro: Falha na atualização: {erro}')

    print("OK! Atualização realizada com sucesso!")

# alterar preços
def alterar_preco():
    imprimir_header()
    print("*** ALTERAR PREÇO ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("Erro! ID deve ser numérico.")
        return
   
    produto = get_produto(id_produto)
    if not produto:
        print(f"Produto com o ID {id_produto} não encontrado!")
        return

    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]} - PREÇO ATUAL: {produto[3]}")

    try:
        novo_preco = float(input("Informe o novo preço: "))
    except ValueError:
        print("Erro! O preço deve ser número inteiro!")
        return
    
    if novo_preco == produto[3]:
        print("O valor informado é igual ao preço atual.")
        return
    if novo_preco <= 0 or novo_preco > 1000:
        print("Erro! Esse valor é inválido.")
        return
    
    try:
        comandoSQL = f'UPDATE Produto SET preco = {novo_preco} WHERE idProduto = {id_produto}'
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'Erro: Falha na atualização: {erro}')

    print("OK! Atualização realizada com sucesso!")

# excluir um produto
def excluir():
    imprimir_header()
    print("*** Excluir Produto ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("Erro! ID deve ser numérico!")
        return
   
    produto = get_produto(id_produto)
    if not produto:
        print(f"Produto com o ID {id_produto} não encontrado!")
        return

    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]}")

    confirma = input("Digite S para confirmar a exclusão: ")
    if confirma != 'S' and confirma != "s":
        print("Exclusão cancelada!")
        return #Volta para o MENU Principal

    try:
        cursorDB = conexaoDB.cursor()
        comandoSQL = f'DELETE FROM Produto WHERE idProduto = {id_produto}'
        cursorDB.execute(comandoSQL)

        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'Erro: Falha na exclusão: {erro}')
        return
   
    print("OK! Exclusão realizada com sucesso!")
    cursorDB.close()

#Programa Principal
while True:
    imprimir_header()
    print(" MENU - Informe a opção desejada: ")
    print("1 - Cadastrar produto;")
    print("2 - Alterar quantidade;")
    print("3 - Alterar preço;")
    print("4 - Mostrar todos os produtos;")
    print("5 - Excluir um produto;")
    print("6 - Sair;")

    opcao = input("Informe a opção desejada: ")
    if opcao == '1':
        cadastrar()
    
    elif opcao == '2':
        alterar_quant()
    
    elif opcao == '3':
        alterar_preco()
    
    elif opcao == '4':
        listar()
    
    elif opcao == '5':
        excluir()
    
    elif opcao == '6':
        break

    else:
        print("Opção inválida!")

    os.system('pause')