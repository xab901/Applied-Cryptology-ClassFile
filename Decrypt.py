import matplotlib.pyplot as plt
from collections import Counter

def analyze_message(msg):
    """
    Analyzes the frequency of each letter in the given message.

    Parameters:
        msg (str): The message to be analyzed.
    
    Returns:
        dict: A dictionary with letters as keys and their frequencies as values.
    """
    # Filter out only alphabetic characters and convert to lowercase
    filtered_msg = [char.lower() for char in msg if char.isalpha()]
    
    # Count occurrences of each letter
    letter_count = Counter(filtered_msg)
    
    # Calculate total letters
    total_letters = sum(letter_count.values())
    
    # Calculate frequency for each letter
    letter_frequency = {char: count / total_letters for char, count in letter_count.items()}
    
    return letter_count, letter_frequency

def plot_letter_frequency(letter_frequency):
    """
    Plots the frequency of letters using a bar chart.

    Parameters:
        letter_frequency (dict): A dictionary with letters as keys and their frequencies as values.
    """
    # Sort the frequency dictionary by letters
    sorted_letters = sorted(letter_frequency.items(), key=lambda x: x[0])
    letters, frequencies = zip(*sorted_letters)

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(letters, frequencies, color='skyblue', edgecolor='black')

    # Add titles and labels
    plt.title('Letter Frequency in Message', fontsize=16)
    plt.xlabel('Letters', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)

    # Display grid and chart
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Input the message
    msg = input("Enter the encrypted message: ")
    
    # Analyze the message
    letter_count, letter_frequency = analyze_message(msg)
    
    # Print results
    print("\nLetter Count:")
    for char, count in letter_count.items():
        print(f"{char}: {count}")
    
    print("\nLetter Frequency:")
    for char, freq in sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True):
        print(f"{char}: {freq:.4f}")

    # Plot the letter frequency
    plot_letter_frequency(letter_frequency)