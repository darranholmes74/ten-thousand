import random
from collections import Counter

scoring_combinations = [((1, 1, 1), 1000), ((1, 1, 1, 1), 2000)]


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        """
        Rolls a specified number of dice with a specified number of sides per die.
        Returns a tuple of the individual rolls.
        """
        rolls = []
        for i in range(num_dice):
            roll = random.randint(1, 6)
            rolls.append(roll)
        return tuple(rolls)

    @staticmethod
    def calculate_score(dice):
        """
        Calculates the score for a given roll of dice according to the rules of the game.
        Returns an integer representing the score earned by the roll.
        """
        score = 0

        # setting imported python function Counter to iterate through the dice results
        counter = Counter(dice)

        # if dice result returns nothing return the score
        if len(dice) == 0:
            return score

        # if the dice results come back as these combos return the scores below
        if all(d in dice for d in [1, 2, 3, 4, 5, 6]):
            score = 1500
        elif all(d in dice for d in [2, 2, 3, 3, 4, 6]):
            score = 0
        elif all(d in dice for d in [2, 2, 3, 3, 6, 6]):
            score = 1500
        elif all(d in dice for d in [1, 1, 1, 2, 2, 2]):
            score = 1200
        else:


        # Checking if ones are in the results and adding the score based on how much are present
            if counter[1] == 1:
                score += 100

            if counter[1] == 2:
                score += 200

            if counter[1] == 3:
                score += 1000

            if counter[1] == 4:
                score += 2000

            if counter[1] == 5:
                score += 3000

            if counter[1] == 6:
                score += 4000

        # # Checking if twos are in the results and adding the score based on how much are present

            if counter[2] == 4:
                score += 400

            if counter[2] == 5:
                score += 600

            if counter[2] == 6:
                score += 800

        # # Checking if threes are in the results and adding the score based on how much are present

            if counter[3] == 4:
                score += 600

            if counter[3] == 5:
                score += 900

            if counter[3] == 6:
                score += 1200

        # Checking if fours are in the results and adding the score based on how much are present
            if counter[4] == 4:
                score += 800

            if counter[4] == 5:
                score += 1200

            if counter[4] == 6:
                score += 1600

        # Checking if fives are in the results and adding the score based on how much are present
            if counter[5] == 3:
                score += 500
                counter[5] -= 3
            score += counter[5] * 50

            if counter[5] == 4:
                score += 1000

            if counter[5] == 5:
                score += 1500

            if counter[5] == 6:
                score += 2000

        # Checking if sixes are in the results and adding the score based on how much are present
            if counter[6] == 4:
                score += 1200

            if counter[6] == 5:
                score += 1800

            if counter[6] == 6:
                score += 2400
            else:

            # Checking if any number besides 1 and 5 show up 3 times or less and * them be 100
                for i in range(2, 7):
                    if i == 5:
                        continue
                    if counter[i] == 3:
                        score += i * 100
        return score


if __name__ == '__main__':
    game = GameLogic()
    dice_results = game.roll_dice(6)
    print("Dice rolls:", dice_results)
    score = game.calculate_score(dice_results)
    print("Dice rolls:", dice_results)
    print("Score:", score)
