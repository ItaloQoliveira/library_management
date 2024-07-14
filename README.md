# library_management

Com pyhton e django instalado, primeiro sincronize o banco de dados executando

```
python manage.py makemigrations
python manage.py migrate
```
Para executar o projeto

```
python manage.py runserver
```

Se tudo ocorreu bem, acessar no endereço `http://127.0.0.1:8000`

###AS VIEWS FORAM REMOVIDAS, PROJETO TRANSFORMADO EM API REST, INTERAGIR COM JSON USANDO PLATAFORMA DE API DE SUA PREFERÊNCIA

##Exemplo de json para facilitar futuro uso:

```
{ 
    "title": "As aventuras de Katarina num mundo distopico", 
    "author": "Denilson Deniles ", 
    "published_date": "1975-08-15", 
    "isbn_number": "05777874", 
    "price": "19.17"
}

```
