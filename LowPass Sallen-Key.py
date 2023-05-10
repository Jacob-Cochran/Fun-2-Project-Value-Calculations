import math

resistors = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
   100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
   1e3, 1.2e3, 1.5e3, 1.8e3, 2.2e3, 2.7e3, 3.3e3, 3.9e3, 4.7e3, 5.6e3, 6.8e3, 8.2e3,
   10e3, 12e3, 15e3, 18e3, 22e3, 27e3, 33e3, 39e3, 47e3, 56e3, 68e3, 82e3,
   100e3, 120e3, 150e3, 180e3, 220e3, 270e3, 330e3, 390e3, 470e3, 560e3, 680e3, 820e3,
   1e6]

capacitors = [0.01e-6, 0.1e-6, 0.47e-6]

def calculateQValue(R1, R2, C1, C2):
   numerator = math.sqrt(R1*R2*C1*C2)
   denominator = R1*C1 + C2*C1
   return numerator / denominator

def calculateCornerFrequency(R1, R2, C1, C2):
   denominator = math.sqrt(R1*R2*C1*C2)
   return (1 / denominator)


qualityBottom = 0.5
qualityTop = 0.707
frequency = 350 * math.pi
freqTol = 100*2*math.pi
listComponentsAndValues = []

for R1 in resistors:
   for R2 in resistors:
      for C1 in capacitors:
         for C2 in capacitors:
            QValue = calculateQValue(R1, R2, C1, C2)
            corner = calculateCornerFrequency(R1, R2, C1, C2)
            if qualityBottom <= QValue <= qualityTop:
               if frequency - freqTol <= corner <= frequency + freqTol:
                  listComponentsAndValues.append([R1, R2, C1, C2, [QValue, corner]])

for components in listComponentsAndValues:
   print(components)