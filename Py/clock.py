import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("time")
    args = parser.parse_args()
    hr = int(args.time[0:2])
    min = int(args.time[3:5])
    if len(args.time) != 5 or hr > 23 or hr < 0 or min > 59 or min < 0: #this still has weakness of 5 len any, not :
        sys.exit("usage: py clock.py hh:mm")
    minAngle = int((min/60)*360)
    hrAngle = int((hr/12)*360 + (min/60)*(360/12))
    print((minAngle - hrAngle) % 360)

if __name__== "__main__":
    main()