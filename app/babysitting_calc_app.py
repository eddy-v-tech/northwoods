from babysitter import Babysitter
import logging
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--start", required=True, help="Start times accepted in the following two formats: 5PM or 5:00PM")
argParser.add_argument("-f", "--finish", required=True, help="Finish times accepted in the following two formats: 5PM or 5:00PM")
argParser.add_argument("-b", "--bedtime", help="bed times accepted in the following two formats: 5PM or 5:00PM")

args = argParser.parse_args()

newSitter = Babysitter()
if args.bedtime:
    newSitter.set_start(args.start)
    newSitter.set_finish(args.finish)
    newSitter.set_bed_time(args.bedtime)
else:
    newSitter.set_start(args.start)
    newSitter.set_finish(args.finish)

charge = newSitter.calculate_nightly_charge()

print("The nightly charge for the times entered is ${}".format(charge))