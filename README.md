# 🚀 Projeto FastAPI - Middlewares do Henriques

Este projeto é uma implementação prática de middlewares utilizando o framework **FastAPI**, desenvolvido por Henriques500. O objetivo principal é demonstrar como utilizar middlewares personalizados para interceptar, modificar ou monitorar requisições HTTP em APIs modernas e performáticas com Python.

## 📦 Funcionalidades

- ✅ Middleware para logging de requisições
- ✅ Middleware para tratamento de erros
- ✅ Middleware de autenticação (em progresso)
- ✅ Geração de conteúdo via Blender script (exemplo)
- ✅ Organização modular de código

## 🧰 Tecnologias Usadas

- Python 3.11+
- FastAPI
- Uvicorn
- Blender Python API (Opcional)

## 📁 Estrutura do Projeto

meu_projeto/
├── middleware.py              # Middlewares personalizados
├── blender_generate.py       # Script de geração com Blender
├── README.md                 # Documentação do projeto
└── __pycache__/              # Cache do Python (ignorar)

## ▶️ Como Executar o Projeto

1. Clonar o repositório:

    git clone https://github.com/Henriques500/meu-projeto-fastapi.git
    cd meu-projeto-fastapi

2. Criar ambiente virtual:

    python -m venv venv
    venv\Scripts\activate     # Windows

3. Instalar dependências:

    pip install fastapi uvicorn

4. Executar o servidor:

    uvicorn middleware:app --reload

## 📌 Notas

- Certifique-se de estar com o Python 3.11 ou superior instalado.
- Se for usar o script de Blender, é necessário ter o Blender instalado e configurar a execução via terminal.

## 🤝 Contribuição

Fique à vontade para abrir pull requests ou issues com melhorias, sugestões ou correções.

## 🧑‍💻 Autor

**Henriques Cassimo Antinane**
📧 henriquescassimoantinane500@gmail.com
🔗 GitHub: Henriques500

## 📜 Licença

Este projeto está sob a Licença MIT. Veja o ficheiro LICENSE para mais detalhes.
