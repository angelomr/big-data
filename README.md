# BIG Data - A Technical Case

## Configurando o Ambiente

### Crie e ative o Virtualenv
Para executar o projeto, deverá ser executado e ativado o  virtual environment do Python diretamente na pasta raiz do projeto:
> virtualenv --system-site-packages -p python3 venv
> source venv/bin/activate

O primeiro comando acima, irá criar o Virtual Environment do Python e o segundo irá ativá-lo para a sessão que está sendo executada.

### Instale as extensões
> pip install -r requirements.txt

### Rode a API
> PYTHONPATH=./ FLASK_ENV=development  python ./src/app.py

No terminal irá exibir a mensagem abaixo, indicaindo que você já pode acessar o endereço http://localhost:5000 através do Navegador de internet e visualizar a documentação dos endpoints criados com Swagger
> >>>>> Starting development server at http://localhost:5000 <<<<<

## Tecnologias Utilizadas:
* python - Linguagem de Programação
* Flask - Micro-framework de python para agilizar o desenvolvimento
* Flask-RESTPlus - extensão do Flask para trabalhar com chamadas de API rest, inclusive gerando documentação interativa através do Swagger UI
* Flask-SQLAlchemy - extensão do Flask para facilitar as operações no banco de dados (ORM)
* unittest - Framework para Teste Unitário


### Execução dos testes
> python -m unittest -v

*Importante:* Somente criei 1 caso de teste para cada endpoint, testando se o mesmo está está online, retornando resultado na porta 200. Haveriam diversos casos de testes que poderiam ser acrescentados, porém como o tempo de desenvolvimento foi curto (envolvendo um final de semana cheio de compromissos), foram efetuados apenas estes testes.