#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python Programming Tutorial - 5 - Lists
# by thenewboston
# https://youtu.be/1yUn-ydsgKk

players = [29, 58, 66, 71, 87]
# Nothing printed on sys.stdout

players[2]
# 66

players[2] = 68
# Nothing printed on sys.stdout

players
# [29, 58, 68, 71, 87]

players + [90,91,98]
# [29, 58, 68, 71, 87, 90, 91, 98]

players.append(120)
# Nothing printed on sys.stdout

players
# [29, 58, 68, 71, 87, 120]

players[:2]
# [29, 58]

players[:2] = [0, 0]
# Nothing printed on sys.stdout

players
# [0, 0, 68, 71, 87, 120]

players[:2] = []
# Nothing printed on sys.stdout

players
# [68, 71, 87, 120]

players[:] = []
# Nothing printed on sys.stdout

players
# []
