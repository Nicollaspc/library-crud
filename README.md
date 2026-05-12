<h1 align="center">Library System - Python 🏛️</h1>

Sistema de gerenciamento de biblioteca desenvolvido em Python utilizando Programação Orientada a Objetos (POO) e SQLite.

O objetivo do projeto é praticar conceitos reais de desenvolvimento backend, organização de código, persistência de dados, arquitetura e boas práticas de software.

---

# 💻 Ferramentas e Tecnologias

[![My Skills](https://skillicons.dev/icons?i=python,js,flask,tailwind,sqlite,git,github,vscode)](https://skillicons.dev)

---

# 🎯 Funcionalidades

- ✅ Cadastro de livros
- ✅ Listagem de livros
- ✅ Atualização de preço
- ✅ Remoção de livros
- ✅ Persistência de dados com SQLite
- ✅ Tratamento de exceções
- ✅ Organização modular do projeto

---

# 🧠 Conceitos Praticados

Este projeto foi desenvolvido com foco em aprendizado de conceitos importantes de engenharia de software:

- Orientação a Objetos
- Encapsulamento
- Separação de responsabilidades
- CRUD
- Persistência de dados
- Manipulação de banco de dados
- Estruturação de projetos Python
- Tratamento de erros
- Arquitetura básica backend

---

# 📂 Estrutura do Projeto

```bash
library/
│
├── banco.py
├── livro.py
├── main.py
├── banco.sqlite
└── README.md
```

---

# 🏗️ Estrutura das Classes

## 📖 Livro

Responsável por representar a entidade de domínio do sistema.

### Atributos

- id
- titulo
- autor
- paginas
- isbn
- preco

---

## 🗄️ BancoDeDados

Responsável pela comunicação com o SQLite.

### Funções principais

- conectar banco
- criar tabela
- inserir dados
- listar dados
- atualizar registros
- deletar registros

---



# ⚙️ Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/Nicollaspc/library-crud.git
```

---

## 2️⃣ Entre na pasta do projeto

```bash
cd library-crud
```

---

## 3️⃣ Execute o projeto

```bash
python main.py
```

---

# 💾 Banco de Dados

O sistema utiliza SQLite, portanto não é necessário instalar um servidor de banco de dados.

O arquivo será criado automaticamente:

```bash
banco.sqlite
```

---

# 📌 Exemplo de Fluxo

```text
1 - Cadastrar livro
2 - Listar livros
3 - Atualizar preço
4 - Deletar livro
5 - Sair
```

---

# 🧪 Exemplo de Cadastro

```python
livro = Livro(
    titulo="Hábitos Atômicos",
    autor="James Clear",
    paginas=320,
    isbn="9788550807560",
    preco=40.00
)
```

---

# 🔥 Melhorias Futuras

- [ ] Separação de responsabilidades
- [ ] Sistema de empréstimo de livros
- [ ] Busca por título
- [ ] Busca por autor
- [ ] Interface gráfica
- [ ] API REST com Flask
- [ ] API REST com FastAPI
- [ ] Sistema de usuários
- [ ] Testes automatizados
- [ ] Docker
- [ ] PostgreSQL

---

# 📈 Objetivo do Projeto

Este projeto faz parte dos estudos de desenvolvimento backend com Python, com foco na construção de aplicações organizadas, escaláveis e alinhadas com práticas utilizadas no mercado.

---

# 👨‍💻 Autor

Desenvolvido por Nicollas Nascimento
