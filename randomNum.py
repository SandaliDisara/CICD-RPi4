import random
import time

def generate_random_number():
    # Generate a random number between 10 and 30
    return random.randint(10, 30)

def main():
    try:
        while True:
            # Generate a random number
            random_number = generate_random_number()
            # Print the random number
            print("Random number:", random_number)
            # Wait for 2 minutes
            time.sleep(10
                       )  # 120 seconds = 1 minutes
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    main()

