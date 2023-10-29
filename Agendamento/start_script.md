Passos para agendar a execução do script usando cron:

Abra um terminal.
Digite o comando crontab -e para editar as tarefas cron do usuário atual.
Adicione a seguinte linha ao arquivo de tarefas cron para agendar a execução do script todos os dias às 3 da manhã, por exemplo:

0 3 * * * /Documents/desafio/script.py
Isso configurará a execução diária do script às 3 da manhã.

Após fazer as alterações, salve o arquivo e saia do editor. O script agora será executado automaticamente uma vez ao dia de acordo com a programação definida no cron.