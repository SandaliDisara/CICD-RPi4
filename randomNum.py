import random
import time
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Path to the Firebase service account JSON file
firebase_credentials_file = os.path.join(os.path.dirname(__file__), 'Firebase', 'serviceAccountKey.json')

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate(firebase_credentials_file)
firebase_admin.initialize_app(cred)
db = firestore.client()

def generate_random_number():
    # Generate a random number between 10 and 30
    return random.randint(10, 30)

def send_to_firebase(random_number):
    # Get current timestamp
    timestamp = firestore.SERVER_TIMESTAMP

    # Define data to be sent to Firebase
    data = {
        "timestamp": timestamp,
        "value": random_number
    }

    # Add data to Firestore collection
    db.collection("random_numbers").add(data)

def main():
    try:
        while True:
            # Generate a random number
            random_number = generate_random_number()
            # Print the random number
            print("Random number:", random_number)
            # Send the random number to Firebase
            send_to_firebase(random_number)
            # Wait for 20 seconds
            time.sleep(20)
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    main()


    #CICD test pipeline
