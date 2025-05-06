import subprocess
import os
import re
import time


# Criar diretório de resultados
os.makedirs("benchmark_results", exist_ok=True)
os.chdir("benchmark_results")

SCENARIOS = [
    {"name": "Teste Padrão 100k", "connections": 100, "requests": 100000, "extra_args": ""},
    {"name": "Teste Padrão 1M", "connections": 500, "requests": 1000000, "extra_args": ""},
    {"name": "Teste de Pipeline 50 comandos 1M", "connections": 500, "requests": 1000000, "extra_args": "-P 50"},
    {"name": "Teste de Alta Conexão 100k", "connections": 1000, "requests": 100000, "extra_args": ""},
    {"name": "Teste de Grandes Valores 1M", "connections": 500, "requests": 1000000, "extra_args": "-d 524288"},
    {"name": "Teste de Workload Pesado 5M", "connections": 500, "requests": 5000000, "extra_args": ""},
    {"name": "Teste Padrão Grande Valores 100k", "connections": 1500, "requests": 10000, "extra_args": "-d 524288"},
]


DATABASES = {
    "redis": {"host": "localhost", "port": 6379},
    "valkey": {"host": "localhost", "port": 6380},
    "dragonfly": {"host": "localhost", "port": 6381},
    "keydb": {"host": "localhost", "port": 6382},
}


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\W_]+', '-', s)
    return s.strip('-')

def run_benchmark(host, port, db_name, scenario):
    start_time = time.time()
    output_file = f"{db_name}_{slugify(scenario['name'])}_benchmark.csv"
    command = f"redis-benchmark -h {host} -p {port} -n {scenario['requests']} -c {scenario['connections']} -t set,get {scenario['extra_args']} --csv >>  {output_file}"

    print(f"Executando benchmark para {db_name} cenario {scenario['name']}")
    print(f"Comando: {command}")
    subprocess.run(command, shell=True, check=True)
    duration = time.time() - start_time
    print(f"Duração {duration} segundos")
    print(f"Resultados salvos em {output_file}\n")


# Executar benchmarks
for db_name, config in DATABASES.items():
    for scenario in SCENARIOS:
        try:
            run_benchmark(config["host"], config["port"], db_name, scenario)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar benchmark para {db_name}: {e}")