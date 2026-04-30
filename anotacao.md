# Principais Comandos do Git
## Enviando a primeira versão
1. git init -> Inicializar a pasta como repositório local
2. git branch -M main -> Altera a branch master para main
3. git add -> Adiciona os arquivos para o repositório local
4. git commit -m "Primeira versão do sistema"
5. git remote add origin https://github.com/JoaquimMagal/sistema_medico.git
6. git push -u origin main

## Enviando as proximas versões
1. git add . -> Adiciona os arquivos para o repositório local
2. git commit -m "Segunda verão do sistema"
3. git push

# Configuração de usuário Git
git config --global user.name "Joaquim Magalhaes"
git config --global user.email "jocamagal25@gmail.com"

# Comandos do Ambiente Virtual
1. python -m venv venv -> Gera o ambiente virtual do tipo venv
2. .\venv\Scripts\activate -> Ativa o ambiente virtual
3. pip install django -> Instala o django
4. django-admin startproject sistema .
5. python manage.py runserver

## Comandos do Django
1. Ativando o ambiente virtual -> .\venv\Scripts\activate
2. Instalando o django -> pip install django
3. Criando o projeto django -> django-admin startproject nome_do_projeto . 
4. Subindo o servidor -> python manage.py runserver
5. Criando um novo app -> python manage.py startapp nome_do_app
6. Criando um superusuario -> python manage.py createsuperuser
7. Alterando a senha, caso voce esqueça -> python manage.py changepassword nome_do_usuario
8. Gerando o pacote de migração -> python manage.py makemigrations
9. Rodando as alterações do pacote de migração -> python manage.py migrate
10. Comando para manipular imagens no django -> python -m pip install Pillow 

## OBSERVAÇÕES
1. Em python, podemos ter mais de uma classe por arquivo

## Tipos de dados do framework ORM
``CharField()`` -> é um campo de texto.
    -max_length -> é o tamanho máximo do campo.
    - choices = -> é a possibilidade definida para aquele campo.
``EmailFiel`` -> é um campo d email, ele valida se o email é valido (@,.).
``DateTimeField()`` -> é um campo de data e hora.
    - default-> é o valor padrão
    - timezone.now -> é a data e hora atual(local).
``BooleanField`` -> é um campo booleano.
    -default=True -> é por padrão verdadeiro.
``TextField()`` -> é um campo de texto.
    -blank=True -> permite que o campo seja vazio.
``ImageField`` -> é um campo de imagem.
    -upload_to -> é o caminho onde a imagem será salve.
    -%Y é o ano
    -%m é o mês
    -%d é o dia
``ForeignKey()`` -> é um campo de chave estrangeira.
    - on_delete=models.CASCADE -> significa que quando um paciente/médico for deletado, a consulta tambem será deletada
    - verbose_name -> é o nome do campo que será exibido no admin