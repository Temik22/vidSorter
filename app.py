import argparse
import sys
import collection as c
import GUI


def createParser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-g', '--gui', action='store_true')
    parser.add_argument('-i', '--imp', type=open)

    return parser


def main():
    params = createParser().parse_args(sys.argv[1:])

    col = c.Collection()

    if params.imp:
        col.reload(params.imp)

    if params.gui:
        GUI.main(col)
        # here must be function that turn on gui mode


main()
