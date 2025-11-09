from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',         # mudar senha pro ceub
    'database': 'trab_bd'   
}

def init_db():
    # conecta e se não tiver BD cria um 
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS trab_bd")
    conn.commit()
    conn.close()

    # agora conecta com o banco descompactando as infos(senha, user etc)
    conn = mysql.connector.connect(**db_config)

    # PRIMEIRO COMANDO SQL que é o de fazer a tabela
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            curso VARCHAR(50) NOT NULL,
            cargo VARCHAR(50) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ao inves de colocar inde.html a / vai servir pra voltar pro inicio
@app.route('/')
def home():
    return render_template('index.html')

# Mesma coisa com o registrar, so por preferencia mesmo
# Aqui é salvo os dados dos inputs em variaveis que logo depois é feito um INSERT INTO delas
@app.route('/registrar', methods=['POST'])
def registrar():
    # pegando do form do index.html pelo id que eu criei la
    nome = request.form['login']
    email = request.form['email']
    curso = request.form['curso']
    cargo = request.form['cargo']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, email, curso, cargo)
        VALUES (%s, %s, %s, %s)
    ''', (nome, email, curso, cargo))
    conn.commit()
    conn.close()
    return redirect(url_for('listar'))

# Aqui é feito o comando select o qual vai ser mostrando em tipo uma "tabela" no proprio html
@app.route('/listar')
def listar():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, email, curso, cargo FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('listar.html', usuarios=usuarios)

# Aqui é como se fosse um update feito direto no HTML, ele da request nos dados e faz o UPDATE
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        curso = request.form['curso']
        cargo = request.form['cargo']
        cursor.execute('''
            UPDATE usuarios
            SET nome=%s, email=%s, curso=%s, cargo=%s
            WHERE id=%s
        ''', (nome, email, curso, cargo, id))
        conn.commit()
        conn.close()
        return redirect(url_for('listar'))
    cursor.execute("SELECT * FROM usuarios WHERE id=%s", (id,))
    usuario = cursor.fetchone()
    conn.close()
    return render_template('editar.html', usuario=usuario)

# Por fim a parte de excluir um usuario  ppegando o id la no listar.html
@app.route('/excluir/<int:id>')
def excluir(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
