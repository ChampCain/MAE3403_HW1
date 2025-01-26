# region imports
from Die import rollFairDie as rfd
from Die import rollUnFairDie


# endregion

# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0]*6  # create a list with 6 elements/items initialized to 0's
    n = 1000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rfd()  # score = 1 to 6
        scores[roll - 1] += 1  # increment score-1 item b/c 0 indexing start
    # print the result
        print(f"After rolling the die {n} times:")
        for i in range(6):
            probability = scores[i] / n
    print(f"Probability of rolling a {i + 1}: {probability:.4f}")



def main2():
    """
    This function rolls a fair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    n = 10000  # Number of rolls
    scores = [0] * 6  # Initialize counts for numbers 1 through 6

    # Simulate rolling the die `n` times
    for _ in range(n):
        roll = rfd()  # Roll the die
        scores[roll - 1] += 1  # Increment count for the rolled number (adjusted for 0-indexing)

    # print the result
    print(f"\nAfter rolling the die {n} times:")
    for i in range(6):
        probability = scores[i] / n
        print(f"Probability of rolling a {i + 1}: {probability:.4f}")




def main3():
    """
    This function rolls an unfair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    n = 10000  # Number of rolls
    scores = [0] * 6  # Initialize counts for numbers 1 through 6

    # Simulate rolling the die `n` times
    for _ in range(n):
        roll = rollUnFairDie()  # Roll the unfair die
        scores[roll - 1] += 1  # Increment count for the rolled number (adjusted for 0-indexing)

    # Print the probabilities
    print(f"\nAfter rolling the unfair die {n} times:")
    for i in range(6):
        probability = scores[i] / n
        print(f"Probability of rolling a {i + 1}: {probability:.4f}")





# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()
    main3()



