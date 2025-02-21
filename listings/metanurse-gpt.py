import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Enforce rest if health conditions are risky or lack of sleep
    if hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 12:
        return 3  # Sleep
    
    # Sleep if alertness is critically low
    if alertness < 0.5:
        return 3  # Sleep

    # Drink coffee if alertness needs a boost but health parameters are safe
    if alertness < 0.8 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Default to just working to maintain productivity
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)