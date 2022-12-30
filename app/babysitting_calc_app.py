from babysitter import Babysitter
import logging
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--start", required=True, help="(Required) Start times accepted in the following two formats: 5PM or 5:00PM")
argParser.add_argument("-f", "--finish", required=True, help="(Required) Finish times accepted in the following two formats: 5PM or 5:00PM")
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

if type(charge) != int and charge[1] != None:
    print(charge[1])
elif type(charge) != int:
    print(charge[0])
else:
    print("The nightly charge for the times entered is ${}".format(charge))