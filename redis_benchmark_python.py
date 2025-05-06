import redis
import time

NUM_OPERATIONS = 10000

databases = {
    "Redis": 6379,
    "Valkey": 6380,
    "Dragonfly": 6381,
    "KeyDB": 6382
}


def redis_benchmark(host='localhost', port=6379, db=0, num_operations=10000):
    client = redis.Redis(host=host, port=port, db=db)

    data = {f'key{i}': f'value{i}' for i in range(num_operations)}

    start_time = time.time()
    for key, value in data.items():
        client.set(key, value)
    write_duration = time.time() - start_time
    print(f"Tempo de gravação para {num_operations} operações: {write_duration:.4f} segundos")

    start_time = time.time()
    for key in data.keys():
        _ = client.get(key)
    read_duration = time.time() - start_time
    print(f"Tempo de leitura para {num_operations} operações: {read_duration:.4f} segundos")

    start_time = time.time()
    for key in data.keys():
        client.delete(key)
    read_duration = time.time() - start_time
    print(f"Limpeza dos dados p/ {num_operations} operações: {read_duration:.4f} segundos")


def execute_benchmark():
    for db_name, port in databases.items():
        start_time = time.time()
        print(f"Rodando benchmark em {db_name}...")
        redis_benchmark(port=port, num_operations=NUM_OPERATIONS)
        total_duration = time.time() - start_time
        print(f"Tempo total do {db_name}: {total_duration:.4f} segundos")


if __name__ == "__main__":
    execute_benchmark()
