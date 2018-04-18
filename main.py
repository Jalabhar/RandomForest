import sys
from forest import Forest
from utils import *


def main():
    debug = False
    threshold = 1
    for i in range(0, len(sys.argv)):
        if sys.argv[i] == '-d':
            debug = True
        elif sys.argv[i] == '-t':
            threshold = sys.argv[i+1]
        elif sys.argv[i] == '-h':
            print "Usage: python main.py [OPTIONS]\n"
            print "--------- Options -------------"
            print "'-d' : debug mode"
            print "'-t [VALUE]' : set mean square error threshold to value"
            return

    (data, training, test) = readData(
                filename = 'whitewine.csv',
                debug = False,
                label_index = 11,
                variable_index = (0,10),
                separator= ';')

    forest = Forest(filename = 'whitewine.csv',
                    label_index = 11,
                    variable_index = (0,10),
                    separator=';',
                    mse_threshold= 0.02,
                    debug = debug,
                    num_trees=5)
    forest.build()

    best = forest.predict(test)
    print best

if __name__ == "__main__":
    main()