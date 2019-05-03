#!/usr/bin/env python3

import random
import math

dist1 = [int(math.floor(random.gauss(100, 3))) for x in range(100)]
dist2 = [int(math.floor(random.gauss(1000, 30))) for x in range(100)]
dist3 = [int(math.floor(random.gauss(500, 50))) for x in range(20)]

dist = dist1 + dist2 + dist3

n = 0
drawlist = ["a","g","t","c"]
for i in dist:
    print(">" + str(n))
    outline = [random.choice(drawlist) for x in range(i)]
    print(''.join(outline))
    n += 1
