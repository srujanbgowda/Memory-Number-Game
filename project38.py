import random
import time

number = random.randint(100, 999)
print("Memorize this number:", number)
time.sleep(3)
print("\033c", end="")  # Clears the screen (works in some terminals)

answer = input("Enter the number you saw: ")
if answer == str(number):
    print("Correct! 👍")
else:
    print(f"Wrong. It was {number}.")