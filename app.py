import argparse
import sys
import collection as c
import GUI


def createParser(col):
    parser = argparse.ArgumentParser()

    parser.add_argument('-g', '--gui', action='store_true')
    parser.add_argument('-i', '--imp', nargs='?',
                        default=col.archiveName, type=open)

    return parser


def main():
    col = c.Collection()
    params = createParser(col).parse_args(sys.argv[1:])

    if params.imp:
        col.reload(params.imp)

    if params.gui:
        GUI.main(col)

    col.archive()


main()
