#!/usr/bin/env python3

import random
import math

dist1 = [int(math.floor(random.gauss(100, 30))) for x in range(200)]
dist2 = [int(math.floor(random.gauss(200, 30))) for x in range(200)]
dist3 = [int(math.floor(random.gauss(250, 30))) for x in range(200)]

dist = dist1 + dist2 + dist3

n = 0
drawlist = ["a","g","t","c"]
for i in dist:
    if i > 0:
        print(">" + str(n))
        outline = [random.choice(drawlist) for x in range(i)]
        print(''.join(outline))
        n += 1
