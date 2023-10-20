import mysql.connector

# configuração da conexão com o banco de dados
config = mysql.connector.connect (
        user = "root",
        password = "root",
        host = "127.0.0.1",
        database = "mydb")

# criar um cursor para executar comandos SQL
cursor = config.cursor()

def criar_leitor(nome, sexo, email, endereco, cpf, idleitor):
    sql = "INSERT INTO leitor (nome, sexo, email, endereco, cpf) VALUE (%s, %s, %s, %s, %s)"
    val = (nome, sexo, email, endereco, cpf, idleitor)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente inserido cloacom sucesso!")
    
def listar_leitores():
    cursor.execute("SELECT * FROM leitor")
    leitores = cursor.fetchall()
    for leitor in leitores:
        print(leitor)
        
def atualizar_leitores (nome, sexo, email, endereco, cpf, idleitor):
        if atualizar_leitores in nome:
           def atualizar clientes( idcliente, nome, telefone, email, atraso, livros_idlivros, tempo_idtempo): 
            sql= "UPDATE cliente SET nome-Xs, email=%s, telefone=%s, atraso-Xs, livros_idlivros=%s, tempo_idtempo=%s WHERE idcliente = %s"
            val (nome, sexo, email, endereco, cpf, idleitor)
            

cursor.execute(sql,val)

config.commit()

print("cliente atualizado com suscesso!")
    def menu():    
        while True:
        # Exibe o menu e obtém a escolha do usuário
            menu = float(input(
            "Escolha uma opção para o menu:\n"
                "1 - Inserir\n"
                "2 - Imprimir\n"
                "3 - Atualizar\n"
                "4 - Deletar"))
    
            if menu == 1:
                nome = input("Escreva seu nome: ")
                sexo = input("Escreva seu sexo: ")
                email = input("Escreva seu melhor email: ")
                endereco = input("Digite seu endereço: ")
                cpf = input("Digite seu CPF: ")
                idleitor = input("Digite o ID do leitor: ")
                print("Salvo com sucesso!")
                criar_leitor (nome, sexo, email, endereco, cpf, idleitor)
            
            elif menu == 2:
                listar_leitores()
            
            elif menu == 3:
                nome = input("Escreva seu nome: ")
                sexo = input("Escreva seu sexo: ")
                email = input("Escreva seu melhor email: ")
                endereco = input("Digite seu endereço: ")
                cpf = input("Digite seu CPF: ")
                idleitor = input("Digite o ID do leitor: ")
                atualizar_leitor (nome, sexo, email, endereco, cpf, idleitor)
            
            elif menu == 4
              
if __name__=="__main__":
        menu()
    
        cursor.close()
        config.close()
    
        