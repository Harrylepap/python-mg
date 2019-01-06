#!/bin/python3.6

import math
c = 50
h = 30
resultats = []

items = [x for x in input().split(",")]
for d in items:
          resultats.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(" . ".join(resultats))