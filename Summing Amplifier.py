## Code to find best 3 resistors to give a specified value
import heapq as pq
resistors = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
   100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
   1e3, 1.2e3, 1.5e3, 1.8e3, 2.2e3, 2.7e3, 3.3e3, 3.9e3, 4.7e3, 5.6e3, 6.8e3, 8.2e3,
   10e3, 12e3, 15e3, 18e3, 22e3, 27e3, 33e3, 39e3, 47e3, 56e3, 68e3, 82e3,
   100e3, 120e3, 150e3, 180e3, 220e3, 270e3, 330e3, 390e3, 470e3, 560e3, 680e3, 820e3,
   1e6]

def resistorCalc(R1, R2, R3):
    numerator = R1 * R3 + R1 * R2 + R2 * R3
    denominator = R1
    return (numerator  / denominator)


def errorCalc(desired, actual):
    numerator = (actual - desired)
    denominator = desired
    return abs(100*(numerator/denominator))

desired = 3*82000
heap = []

for R1 in resistors:
    for R2 in resistors:
        for R3 in resistors:
            calculatedValue = resistorCalc(R1, R2, R3)
            error = errorCalc(desired, calculatedValue)
            pq.heappush(heap, (error, R1, R2, R3))

for value in range(len(heap)):
    print(pq.heappop(heap))
