import csv
from PyQt5  import   uic , QtWidgets
import sqlite3
import pandas as pd
import qrcode
from PIL import Image




def  chama_segunda_tela ():
    primeira_tela.label_4.setText("")
    nome_usuario  =  primeira_tela.lineEdit.text()
    senha  =  primeira_tela.lineEdit_2.text()
    banco  =  sqlite3.connect( 'banco_cadastro.db' )
    cursor  =  banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    except:
        print("Erro ao validar o login")    
        
    
    if  senha == senha_bd[0][0]:
        primeira_tela.close()
        segunda_tela.show()
    else:
        primeira_tela.label_4.setText ( "Dados de login incorretos!" )
    

def  logout():
    segunda_tela.close()
    primeira_tela.show()

def  abre_tela_cadastro():
    tela_cadastro.show()


def  cadastrar():
    nome  =  tela_cadastro.lineEdit.text()
    login  =  tela_cadastro.lineEdit_2.text()
    senha  =  tela_cadastro.lineEdit_3.text()
    c_senha  =  tela_cadastro.lineEdit_4.text()

    if ( senha  ==  c_senha ):
        try:
            banco  =  sqlite3.connect( 'banco_cadastro.db' )
            cursor  =  banco.cursor()
            cursor.execute( "CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)" )
            cursor.execute( "INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "')" )

            banco.commit()
            banco.close()
            tela_cadastro.label_5.setText( "Usuario cadastrado com sucesso" )

        except  sqlite3.Error  as  erro :
            print( "Erro ao inserir os dados: " , erro )
    else:
        tela_cadastro.label.setText( "As senhas digitadas são diferentes" )
    

    


app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi( "Primeira_tela.ui" )
segunda_tela=uic.loadUi( "Segunda_tela.ui" )
tela_cadastro=uic.loadUi( "tela_cadastro.ui" )
primeira_tela.pushButton.clicked.connect( chama_segunda_tela )
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode( QtWidgets.QLineEdit.Password )
primeira_tela.pushButton_2.clicked.connect( abre_tela_cadastro )
tela_cadastro.pushButton.clicked.connect( cadastrar )


primeira_tela.show()
app.exec()





    

def listarProdutos():
    for i in range(0, len(produtos)):
        print("Produto {} - {} - R${:.2f} - Quantidade em estoque, {}".format(i, produtos[i][0], produtos[i][1], produtos[i][2]))
    
produtos = []

while True:
    opcao = int(input("Escolha sua opçao:\n\n1 - Admin/Cadastrar produto\n2 - Produtos disponiveis\n3 - Carrinho de compras\n4 - Finalizar sessão\n\n"))
    if opcao == 1:
        teste = 'n'
        teste = 's'
        while(teste != 'n'):
            teste = input(
                
                "Você deseja continuar? (s/n):\n"
                
                )
            if(teste == 'n'):
                 teste == 'n'

            else:
                nome = input("Qual o nome do produto?: ")
                preco = float(input("Qual o preço do  produto: "))
                quantidade = int(input("Qual a quantidade em estoque: \n"))

                produto = []

                produto.append(nome)
                produto.append(preco)
                produto.append(quantidade)
                produtos.append(produto)
                
    if opcao == 2:
        listarProdutos()
        
        #tabela = pd.read_csv("lasi.csv", sep=",")
        #print(tabela)
        
        
        f = open('lasi.csv','w', newline ='', encoding='utf-8')
        w = csv.writer(f)
        w.writerow(produtos)
        f = open('lasi.csv','w', newline ='', encoding='utf-8')
        w = csv.writer(f)
        w.writerow(produtos)
        
        
            
    
    if opcao == 3:
        listarProdutos()
        carrinho = 's'        
        while(carrinho != 'n'):
            carrinho = input("Você deseja continuar comprando? (s/n):\n\n")
            if(carrinho == 'n'):
               carrinho == 'n'
            else:
                
            
        
                numero = int(input("Informe o número do produto:\n"))
        
                quantidade = int(input("Qual a quantidade?\n"))
            
        pagamento = 's'        
        while(pagamento != 'n'):
            pagamento = input("Você deseja fazer o pagamento? (s/n):\n")
            if(pagamento == 'n'):
                pagamento == 'n'
            else:
                im = Image.open('qrc_python.png')
                im.show()
                
                print("PAGAMENTO REALIZADO COM SUCESSO!")
                 
        
        
   
        
        
        if produtos[numero][2]>= quantidade:
            print("Produto vendido com sucesso! informações da venda:\n Produto: {}\n Quantidade: {} \n Valor total de venda: R$ {:.2f}". format(produtos[numero][0], quantidade, quantidade * produtos[numero][1]))
            produtos[numero][2] -= quantidade
            produtos[numero][2] == quantidade     

        else: 
            print(
                "Quantidade indisponível no estoque: "
                ) 
            
          
              
            
    if opcao == 4:
        print(
            "\nAGRADECEMOS A SUA PREFERÊNCIA!\n\n"
            )
        break    
        
            
        