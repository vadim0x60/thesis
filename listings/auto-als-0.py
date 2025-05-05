import sys
import math


def main():
    for step in range(350):
        observations = list(map(float, input().strip().split()))

        # Extract observations
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        # Extract specific vital signs
        heart_rate = vital_signs_values[0] if vital_signs_times[0] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None
        glucose = vital_signs_values[2] if vital_signs_times[2] > 0 else None
        temperature = vital_signs_values[3] if vital_signs_times[3] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        resps = vital_signs_values[6] if vital_signs_times[6] > 0 else None

        # Check for cardiac arrest
        if (sats and sats < 65) or (map_value and map_value < 20):
            print(17)  # StartChestCompression
            continue

        # ABCDE assessment
        if not events[3]:  # AirwayClear
            print(3)  # ExamineAirway
            continue
        if not resp_rate or resp_rate < 8:
            print(4)  # ExamineBreathing
            continue
        if not map_value or map_value < 60:
            print(5)  # ExamineCirculation
            continue
        if not events[21]:  # AVPU_A
            print(6)  # ExamineDisability
            continue
        if not temperature:
            print(7)  # ExamineExposure
            continue

        # Stabilization
        if sats and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if resp_rate and resp_rate < 8:
            print(29)  # UseBagValveMask
            continue
        if map_value and map_value < 60:
            print(15)  # GiveFluids
            continue

        print(48)  # Finish


if __name__ == "__main__":
    main()