import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    for score_dict in score_list:
        print(
            f"Nickname: {score_dict['name']}, attempts: {score_dict['attempts']}, secret number: {score_dict['secret number']}, date: {score_dict['date']}")

nick_name = input("Please enter your name: ")
wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append(
            {"name": nick_name, "attempts": attempts, "secret number": secret, "date": str(datetime.datetime.now()), "wrong guesses": wrong_guesses})
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break

    elif guess > secret:
        wrong_guesses.append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        wrong_guesses.append(guess)
        print("Your guess is not correct... try something bigger")
