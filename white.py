import random

total_balls = 10
white_balls = 3
prob_white_given_white = white_balls / total_balls
print("Analytical Probability:", prob_white_given_white)

def simulate_white_given_white(trials=100000):
    white_given_white_count = 0

    for _ in range(trials):
        first_ball = random.choices(['R', 'B', 'W'], weights=[1, 6, 3])[0]

        if first_ball == 'W':
            second_ball = random.choices(['R', 'B', 'W'], weights=[1, 6, 3])[0]
            if second_ball == 'W':
                white_given_white_count += 1

    return white_given_white_count / (trials * (3/10))

simulated_prob = simulate_white_given_white()
print("Simulated Probability:", simulated_prob)
