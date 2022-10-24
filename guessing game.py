import random

min_val = 1
max_val = 10
guess_count = 0
guess_limit= 5
random_number = (random.randint(min_val , max_val))
guess_again = "Yes"
print("Im guessing...")
print("I guessed! Try to find my number you have 5 tries! ")
while guess_count < guess_limit:
    guess = int(input( "Guess: "))
    guess_count += 1
    if guess == random_number:
        print("You guessed it right! ")
        break
    elif random_number!=guess:
        print("Your guess is wrong!")
        if random_number<guess:
            print("Secret number is smaller than your guess!")
        elif random_number>guess:
            print("Secter number is grater than your guess")
    else:
        print("You failed :( ")


    
