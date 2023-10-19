import mysql.connector

# configuração da conexão com o banco de dados
config = {
        'user':'root',
        'password':'root',
        'host':'127.0.0.1',
        'database': 'mydb'}

try:
        con = mysql.connector.connect(**config)
        if con.is_connected():
            print("Deu certo!")
            con.close()
except mysql.connector.Error as err:
    print("Deu erro", err)