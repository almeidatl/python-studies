import sqlite3
import os
import csv


class Cliente:
    def __init__(self, nome, sobrenome, telefone, email, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return (f'Cliente: {self.nome} {self.sobrenome}'
                f'\nTelefone: {self.telefone} '
                f'\nEmail: {self.email}'
                f'\nEndereço: {self.endereco}')

    def salvar_banco_dados(self):
        try:
            # Obtém o caminho absoluto do diretório atual
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dbfile = os.path.join(base_dir, 'clientes.db')
            conexao = sqlite3.connect(dbfile)
            cursor = conexao.cursor()

            # Cria tabela
            cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                sobrenome TEXT NOT NULL,
                                telefone TEXT,
                                email TEXT NOT NULL,
                                endereco TEXT
                            )""")

            # Insere dados na tabela
            cursor.execute("""INSERT INTO clientes (nome, sobrenome, telefone, email, endereco) 
                                VALUES (?,?,?,?,?)""",
                           (self.nome, self.sobrenome, self.telefone, self.email, self.endereco))

            # Confirma alterações e fecha a conexão
            conexao.commit()
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
        finally:
            conexao.close()

    @staticmethod
    def exportar_para_csv():
        try:
            # Obtém o caminho absoluto do diretório atual
            base_dir = os.path.dirname(os.path.abspath(__file__))
            dbfile = os.path.join(base_dir, 'clientes.db')
            caminho_arquivo_csv = os.path.join(base_dir, 'clientes.csv')

            conexao = sqlite3.connect(dbfile)
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            conexao.close()

            with open(caminho_arquivo_csv, 'w', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv)
                escritor.writerow(['id', 'nome', 'sobrenome', 'telefone', 'email', 'endereco'])
                escritor.writerows(clientes)

        except sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
        except IOError as e:
            print(f"Erro ao escrever o arquivo CSV: {e}")


# Lista de clientes para adicionar ao banco de dados
clientes = [
    Cliente('Anderson', 'Vieira', '8883828999', 'anderson@bol.com', 'Rua dos Guararapes 124'),
    Cliente('Beatriz', 'Silva', '8883929000', 'beatriz@gmail.com', 'Av. Paulista 1000'),
    Cliente('Carlos', 'Santos', '8883929001', 'carlos@hotmail.com', 'Rua Augusta 200'),
    Cliente('Daniela', 'Ferreira', '8883929002', 'daniela@uol.com', 'Rua Bela Cintra 300'),
    Cliente('Eduardo', 'Oliveira', '8883929003', 'eduardo@yahoo.com', 'Rua Haddock Lobo 400'),
    Cliente('Fernanda', 'Almeida', '8883929004', 'fernanda@bol.com', 'Av. Rebouças 500'),
    Cliente('Gabriel', 'Ribeiro', '8883929005', 'gabriel@globo.com', 'Rua Consolação 600'),
    Cliente('Helena', 'Costa', '8883929006', 'helena@terra.com', 'Rua Oscar Freire 700'),
    Cliente('Igor', 'Martins', '8883929007', 'igor@outlook.com', 'Rua Teodoro Sampaio 800'),
    Cliente('Julia', 'Pereira', '8883929008', 'julia@icloud.com', 'Rua Pinheiros 900'),
    Cliente('Kevin', 'Gomes', '8883929009', 'kevin@gmail.com', 'Rua Faria Lima 100'),
    Cliente('Larissa', 'Barros', '8883929010', 'larissa@yahoo.com', 'Rua Clodomiro Amazonas 200'),
    Cliente('Marcos', 'Melo', '8883929011', 'marcos@uol.com', 'Rua Ibirapuera 300'),
    Cliente('Natália', 'Moreira', '8883929012', 'natalia@hotmail.com', 'Rua Itaim Bibi 400'),
    Cliente('Otávio', 'Moraes', '8883929013', 'otavio@gmail.com', 'Rua Vila Olímpia 500'),
    Cliente('Paula', 'Rocha', '8883929014', 'paula@terra.com', 'Rua Campo Belo 600'),
    Cliente('Ricardo', 'Carvalho', '8883929015', 'ricardo@globo.com', 'Rua Vila Mariana 700'),
    Cliente('Sabrina', 'Neves', '8883929016', 'sabrina@icloud.com', 'Rua Moema 800'),
    Cliente('Thiago', 'Nunes', '8883929017', 'thiago@bol.com', 'Rua Morumbi 900'),
    Cliente('Ursula', 'Araújo', '8883929018', 'ursula@gmail.com', 'Rua Santo Amaro 100'),
    Cliente('Vinícius', 'Santiago', '8883929019', 'vinicius@yahoo.com', 'Rua Brooklin 200'),
    Cliente('Wagner', 'Leite', '8883929020', 'wagner@uol.com', 'Rua Jardins 300'),
    Cliente('Xavier', 'Oliveira', '8883929021', 'xavier@hotmail.com', 'Rua Butantã 400'),
    Cliente('Yara', 'Azevedo', '8883929022', 'yara@gmail.com', 'Rua Tatuapé 500'),
    Cliente('Zé', 'Costa', '8883929023', 'ze@outlook.com', 'Rua Lapa 600'),
    Cliente('Alice', 'Fernandes', '8883929024', 'alice@hotmail.com', 'Rua Sé 700'),
    Cliente('Bruno', 'Moura', '8883929025', 'bruno@gmail.com', 'Rua Luz 800'),
    Cliente('Clara', 'Gonçalves', '8883929026', 'clara@icloud.com', 'Rua Anhangabaú 900'),
    Cliente('Diego', 'Rezende', '8883929027', 'diego@gmail.com', 'Rua São Bento 100'),
    Cliente('Elaine', 'Sousa', '8883929028', 'elaine@yahoo.com', 'Rua República 200')
]

# Salva os clientes no banco de dados
for cliente in clientes:
    cliente.salvar_banco_dados()

# Exporta os dados para CSV
Cliente.exportar_para_csv()
