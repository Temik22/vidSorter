import argparse
import sys
import collection as c


def createParser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-g', '--gui', action='store_true')
    parser.add_argument('-i', '--imp', type=open)

    return parser


def main():
    params = createParser().parse_args(sys.argv[1:])

    col = c.Collection()

    if params.gui:
        pass
        # here must be function that turn on gui mode

    if params.imp:
        col.reload(params.imp)


main()
