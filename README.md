# Benchmark de Bancos de Dados em Memória

Este projeto tem como objetivo comparar o desempenho de diferentes bancos de dados em memória, focando nas operações de leitura e escrita. Os bancos de dados avaliados são:

- **Redis**
- **Valkey**
- **Dragonfly**
- **KeyDB**

## Arquitetura do Projeto

O projeto utiliza Docker para containerizar os bancos de dados e ferramentas de monitoramento, facilitando a execução e comparação em um ambiente controlado. Todos os bancos estão configurados com os mesmos recursos (8 CPUs e 8GB de memória) para garantir uma comparação justa.

### Componentes Principais:

1. **Bancos de Dados**:
   - Redis na porta 6379
   - Valkey na porta 6380
   - Dragonfly na porta 6381
   - KeyDB na porta 6382 (com otimização de threads)

2. **Monitoramento**:
   - Exportadores Redis/Prometheus para cada banco de dados
   - Prometheus para coleta de métricas
   - Grafana para visualização de dados
   - Portainer para gerenciamento de containers

3. **Scripts de Benchmark**:
   - `redis_benchmark.py` - Utiliza a ferramenta `redis-benchmark` para diversos cenários
   - `redis_benchmark_python.py` - Implementa teste via biblioteca Python `redis`

## Como Usar

### Pré-requisitos

- Docker e Docker Compose
- Python 3.x
- Biblioteca `redis` para Python

### Instalação

1. Clone este repositório:
   ```
   git clone [url-do-repositório]
   cd databases-in-memory-benchmarks
   ```

2. Instale as dependências Python:
   ```
   pip install redis
   ```

3. Inicie os containers:
   ```
   docker-compose up -d
   ```

### Executando os Benchmarks

#### Utilizando o script redis_benchmark.py
```bash
python redis_benchmark.py
```