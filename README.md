# IP Response Time

Uma ferramenta simples para testar o tempo de resposta via ICMP ping para determinados endereços IP.

## Executando

Clone o projeto e instale as dependências:

```bash
git clone https://github.com/henriquesebastiao/ip-response-time.git
cd ip-response-time
poetry install
```

Execute o script:

```bash
python main.py
```

Será solicitado os hosts que deseja testar, basta informar os IPs separados por espaços. Por fim será solicitado a quantidade de pings que deseja realizar para cada host.

## Exemplo

<img src="screenshots/terminal.png" width="734">

Gráfico gerado:

<img src="screenshots/pdf.png" width="734">

