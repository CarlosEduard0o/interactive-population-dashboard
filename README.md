# interactive-population-dashboard 🧮🌍

**Dashboard interativo para visualização de dados de população por país ao longo do tempo.**

Um projeto desenvolvido com Python, Dash, Plotly e PostgreSQL que permite a seleção de países em um dropdown e exibe gráficos interativos com base em dados armazenados no banco de dados PostgreSQL.

## Índice 📋
1. [Descrição](#descrição)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Instalação](#instalação)
5. [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
6. [Executando a Aplicação](#executando-a-aplicação)
7. [Estrutura do Projeto](#estrutura-do-projeto)
8. [Contribuição](#contribuição)
9. [Licença](#licença)

## Descrição
```mermaid
graph TD
    A[Usuário Seleciona um País] --> B[Dashboard Recebe Dados do Banco de Dados PostgreSQL]
    B --> C[Filtra os Dados da Tabela "Populacao"]
    C --> D[Gera Gráfico Interativo com Plotly]
    D --> E[Exibe Gráfico no Dashboard]
```

O **interactive-population-dashboard** é um dashboard interativo desenvolvido para visualizar dados de população por país ao longo dos anos, diretamente a partir de uma base de dados PostgreSQL.

## Funcionalidades ✅
- Dropdown para seleção de países.
- Gráficos interativos gerados dinamicamente.
- Integração com banco de dados PostgreSQL.

## Tecnologias Utilizadas 💻
- **Python**: Linguagem principal do projeto.
- **Dash**: Framework para desenvolvimento de dashboards.
- **Plotly**: Biblioteca para gráficos interativos.
- **Pandas**: Manipulação de dados.
- **PostgreSQL**: Banco de dados relacional.

## Instalação 🚀
1. Clone este repositório:
   ```bash
   git clone https://github.com/CarlosEduard0o/interactive-population-dashboard.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd interactive-population-dashboard
   ```
3. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração do Banco de Dados 🗄️
1. Certifique-se de que o **PostgreSQL** esteja instalado e em execução.
2. Use o script `database_setup.sql` para criar a tabela necessária no banco.
3. Popular a tabela com o script `populate_data.sql`.
4. Atualize as credenciais de conexão no arquivo `app.py`.

## Executando a Aplicação ▶️
1. Execute o aplicativo:
   ```bash
   python app.py
   ```
2. Abra no navegador: [http://127.0.0.1:8050](http://127.0.0.1:8050).

## Estrutura do Projeto 🗂️
- `app.py`: Código principal da aplicação Dash.
- `requirements.txt`: Dependências do projeto.
- `database_setup.sql`: Script para criação do banco de dados.
- `populate_data.sql`: Dados de exemplo para popular o banco.

## Contribuição 🤝
Contribuições são bem-vindas! Envie suas sugestões através de issues ou pull requests.

## Licença 📜
Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

