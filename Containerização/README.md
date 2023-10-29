# Shipay DevOps Challenge

Este repositório contém um exemplo de projeto que usa Docker para orquestrar vários serviços em Python, incluindo uma API REST, um worker assíncrono e um cluster Kafka. Ele também demonstra como usar SSL/TLS para segurança de rede.

## Estrutura do Projeto

O projeto é composto por quatro serviços principais, cada um com seu próprio Dockerfile:

- `api_rest`: Um serviço de API REST que expõe um aplicativo web Python.
- `async_worker`: Um serviço de worker assíncrono que executa tarefas em segundo plano.
- `base_image`: Uma imagem base Python que compartilha recursos comuns entre os serviços.
- `kafka`: Um cluster Kafka usado para mensagens e eventos.

## Build e Execução

Para construir e executar os serviços, siga estas etapas:

1. Certifique-se de que o Docker e o Docker Compose estejam instalados em sua máquina.

2. Obtenha os arquivos de certificado SSL, nomeie-os `cert.pem` e `key.pem`, e coloque-os no diretório raiz do projeto.

3. Execute o seguinte comando para construir as imagens dos serviços:

    ```bash
    docker build -t api_rest_image -f ./api_rest/Dockerfile_api_rest ./api_rest
    docker build -t async_worker_image -f ./async_worker/Dockerfile_async_worker ./async_worker
    docker build -t shipay_devops_challenge_base_image -f ./Dockerfile_base .
    ```

4. Depois de construir as imagens, você pode executar os serviços usando o Docker Compose:

    ```bash
    docker-compose up -d
    ```


## Configuração do SSL

Este projeto usa SSL/TLS para segurança de rede. Certifique-se de que os arquivos `cert.pem` e `key.pem` estejam presentes no diretório raiz do projeto. Você pode obter certificados SSL assinados por uma autoridade certificadora ou criar seus próprios certificados de teste. Os certificados fornecidos neste exemplo são para fins de teste e demonstração.

## Notas Adicionais

- Os serviços são configurados para reiniciar automaticamente (`restart: always`) em caso de falha.
- O projeto inclui um cluster Kafka configurado no serviço `kafka`. Certifique-se de configurar corretamente as variáveis de ambiente no arquivo `docker-compose.yml` para a comunicação com o Kafka.
