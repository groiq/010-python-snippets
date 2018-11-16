#!/usr/bin/env python3

from pprint import pprint

# data structure mockup for weekly timelogs

timelog = list()

day = 1
def date(day):
    return "12766-03-{}".format(day)
def mon(day):
    return date(day)
def sun(day):
    return date(day+6)

while (day+6) <= 31:
    # curWeek = dict()
    # curWeek["mon"] = mon(day)
    # curWeek["sun"] = sun(day)
    timelog.append(mon(day))
    timelog.append(sun(day))

    day += 7

pprint(timelog)
