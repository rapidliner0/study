#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
