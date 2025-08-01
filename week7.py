import random
def simulate_zkp(trials=20):
    success_count = 0
    for _ in range(trials):
        path_entered = random.choice(['A', 'B'])
    challenge = random.choice(['A', 'B'])
    knows_password = False # Set to False to simulate an attacker
    if knows_password:
        success = True
    else:
        success = path_entered == challenge
    if success:
        success_count += 1
    print(f"Successful responses: {success_count}/{trials}")
    print(f"Success rate: {success_count / trials * 100:.2f}%")

simulate_zkp()


def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
    