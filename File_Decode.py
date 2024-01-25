def decode(message_file):
    # Initialize an empty dictionary to store the key-value pairs
    data_dict = {}

    # Read the data from the file and populate the dictionary
    with open(message_file, 'r') as file:
        for line in file:
            # Split each line into a list of strings
            line = line.strip().split()

            # Convert the first element of the list to an integer (key)
            key = int(line[0])

            # Take the second element of the list as the value
            value = line[1]

            # Add the key-value pair to the dictionary
            data_dict[key] = value
            
    # Find the largest key in the dictionary
    largest_key = max(data_dict)

    # Initialize variables for loop control and tracking
    n = largest_key
    rows = 1
    current_number = 1
    last_numbers = []

    # Generate a list of numbers representing the last number in each row
    while current_number <= n:
        for _ in range(rows):
            if current_number <= n:
                current_number += 1
            else:
                break

        last_numbers.append(current_number - 1)

        rows += 1

    # Example array of keys
    keys_to_access = last_numbers

    # Access the values corresponding to the keys in the array
    values = [data_dict[key] for key in keys_to_access]

    # Initialize a list to store the decoded words
    decoded_words = []

    # Create a list of words based on the accessed values
    for key, value in zip(keys_to_access, values):
        decoded_words.append(value)

    # Return the decoded message as a string
    return ' '.join(decoded_words)

# Example usage:
decoded_message = decode("coding_qual_input.txt")
print(decoded_message.lower().strip())
