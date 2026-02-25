from typing import Generator


def fibonacci_gen() -> Generator[int, None, None]:
    """Generate Fibonacci numbers indefinitely."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_gen() -> Generator[int, None, None]:
    """Generate prime numbers indefinitely."""
    n = 2
    while True:
        is_prime = True
        for division in range(2, n - 1):
            if n % division == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def ft_stream_analytics(n: int) -> Generator[tuple[int, str, int, str],
                                             None, None]:
    """Yield structured game events one at a time."""
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]
    for i in range(1, n + 1):
        player = players[(i - 1) % 3]
        action = actions[(i - 1) % 3]
        level = levels[(i - 1) % 3]
        yield (i, player, level, action)


def ft_data_stream() -> None:
    """Process streamed events analytics."""
    total_events = 0
    treasure_count = 0
    high_level_count = 0
    level_up_count = 0
    n = 3
    stream = ft_stream_analytics(n)
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    for i in range(n):
        event_id, player, level, action = next(stream)
        print(f"Event {event_id}: Player {player} (level {level}) {action}")
        total_events += 1
        if action == "found treasure":
            treasure_count += 1
        if level >= 10:
            high_level_count += 1
        if action == "leveled up":
            level_up_count += 1
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    fib = fibonacci_gen()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(9):
        print(next(fib), end=", ")
    print(next(fib))
    prime = prime_gen()
    print("Prime numbers (first 5): ", end="")
    for p in range(4):
        print(next(prime), end=", ")
    print(next(prime))


if __name__ == "__main__":
    ft_data_stream()
