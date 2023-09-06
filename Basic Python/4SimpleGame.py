secret_number = 5
guess_count = 0
guess_limit = 3
limit_left = 3

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    limit_left -= 1
    if guess == secret_number:
        print("YOU WON!")
        exit(0)
    else:
        print("Eliminated! Try again. Chance left: ",limit_left )