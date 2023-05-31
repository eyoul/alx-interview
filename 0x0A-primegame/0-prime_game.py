 #!/usr/bin/python3

def isWinner(x, nums):
    # Define a function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Loop through each round
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        primes = [i for i in range(2, n+1) if is_prime(i)]
        turn = "Maria"
        while primes:
            # Choose the largest prime number available
            p = max(primes)
            primes = [i for i in primes if i % p != 0]
            turn = "Ben" if turn == "Maria" else "Maria"
        wins[turn] += 1

    # Determine the winner with the most wins
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
