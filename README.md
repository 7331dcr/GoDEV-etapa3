# Gerenciador - Treinamento ProWay

Projeto feito em Python (v. 3.8.6) utilizando Django (v. 3.1.5) como framework, com interface em HTML puro.

## Instalação:

Dentro do folder `/event_manager/manager`, iniciar o servidor executando `python manage.py runserver` no terminal de sua escolha.

Por padrão, o endereço do servidor será `http://127.0.0.1:8000/`.

## Recursos:

`/cadastro`

Permite cadastrar, em ordem:
- quantidade de salas para eventos que serão disponibilizadas; (redirecionando para `/pre_cadastro_sala`)
- nome e capacidade de cada sala; (redirecionando para `/cadastro_sala`)
- nome e capacidade dos 2 espaços para café; (redirecionando para para `/cadastro_cafe`)
- participantes por nome e sobrenome. (quando os cadastros anteriores estiverem satisfatoriamente finalizados)

`/consulta`

Permite consultar o nome do espaço para café e das salas de evento designadas para o participante especificado.

`/consulta_sala`

Permite consultar a lista de participantes cadastrados na sala de evento especificada.

`/consulta_cafe`

Permite consultar a lista de participantes cadastrados no espaço para café especificado.