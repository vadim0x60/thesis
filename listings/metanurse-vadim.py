just_work = 0
drink_coffee = 1
drink_beer = 2
sleep = 3

def vadim(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    """A reference strategy based on a certain PhD student named Vadim"""

    if time_since_slept == 0:
        return drink_coffee
    elif time_since_slept < 31:
        return just_work
    else:
        return sleep

while True:
    observations = list(map(float, input().strip().split()))
    print(vadim(*observations))