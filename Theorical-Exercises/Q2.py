import hashlib
import random

# Create an empty dictionary to store hash values and their corresponding inputs
hash_dict = {}

while True:
    # Generate a random input (you can customize this as needed)
    input_data = str(random.getrandbits(256)).encode('utf-8')

    # Calculate the MySHA hash (first 8 hex digits)
    mysha_hash = hashlib.sha256(input_data).hexdigest()[:8]

    # Check if this hash already exists in the dictionary
    if mysha_hash in hash_dict:
        # If a collision is found, print the colliding inputs and their hash
        print("Collision Found!")
        print("Input 1:", input_data)
        print("Input 2:", hash_dict[mysha_hash])
        print("Collision Hash:", mysha_hash)
        break
    else:
        # Otherwise, add this hash and its input to the dictionary
        hash_dict[mysha_hash] = input_data
