# 💻 Sistema de Cadastro Flask + MySQL (CRUD)

Projeto usando Python(FLASK), HTML, CSS e SQL(MySQL) para criar, listar, editar e excluir usuários.

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Pré-requisitos
- 🐍 Python 3.10+
- 🐬 MySQL instalado e rodando

---

### 2️⃣ Crie o Banco de Dados
Abra o MySQL e rode:
```sql
CREATE DATABASE trab_bd;
USE trab_bd;

CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  login VARCHAR(100),
  email VARCHAR(100),
  curso VARCHAR(50),
  cargo VARCHAR(50)
);
````

---

### 3️⃣ Configure o `app.py`

No topo do arquivo, ajuste suas credenciais MySQL:

```python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'trab_bd'
}
```

---

### 4️⃣ Instale as Dependências

```bash
pip install flask mysql-connector-python
```

---

### 5️⃣ Execute o Sistema

```bash
python app.py
```

## 📚 Funcionalidades

| Função    | Rota            | Descrição                |
| --------- | --------------- | ------------------------ |
| ➕ Criar   | `/`            | Adiciona novo usuário    |
| 📋 Listar | `/listar`       | Mostra todos os usuários |
| ✏️ Editar | `/editar/<id>`  | Altera um registro       |
| ❌ Excluir | `/excluir/<id>`| Remove um usuário        |

---

## 🎨 Interface

* HTML e CSS com design simples e centralizado
* Templates: `index.html`, `listar.html`, `editar.html`, `excluir.html`
* Estilo em: `static/estilo.css`

---

## 🧠 Tecnologias

* **Flask** (backend)
* **MySQL** (banco de dados)
* **HTML + CSS (Jinja2)** (frontend)

---

## 👨‍💻 Autor

**Gabriel Rosa**
📘 Projeto acadêmico — CRUD completo com Flask e MySQL.

---

