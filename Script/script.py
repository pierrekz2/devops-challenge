import datetime
import os

# Obtém o diretório atual
current_dir = os.getcwd()

# Obtém o diretório de arquivos a serem processados
arquivos_dir = os.path.join(current_dir, "ARQUIVOS")

# Obtém o diretório de arquivos processados
arquivos_processados_dir = os.path.join(current_dir, "ARQUIVOS_PROCESSADOS")

# Obtém a data e hora atuais
now = datetime.datetime.now()

# Cria uma lista com os arquivos no diretório de arquivos a serem processados
arquivos = os.listdir(arquivos_dir)

# Loop para mover os arquivos para o diretório de arquivos processados
for arquivo in arquivos:

    # Gera um novo nome para o arquivo incluindo a data e hora
    novo_nome = f"{now.strftime('%Y%m%d-%H%M')}_{arquivo}"

    # Move o arquivo para o diretório de arquivos processados
    os.rename(os.path.join(arquivos_dir, arquivo), os.path.join(arquivos_processados_dir, novo_nome))

    # Log no terminal
    print(f"Arquivo {arquivo} movido para {novo_nome}")