#!/usr/bin/python
import sys
def main():
    #speed=sys.argv[1] #command line argument(speed) is needed.
    speed=101
    print'speed is:', speed
    if speed > 80 and speed<100:
        print("License and registration please")
    elif speed>=100:
        print("You will have to pay paynalty as R.S.2000/-")
    elif speed < 80:
        print("You are safe to go")   
    
if __name__=='__main__':
    main()
