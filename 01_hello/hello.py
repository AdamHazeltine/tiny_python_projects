#!/usr/bin/env python3
"""
Author: Adam Hazeltine
Purpose: say hello
"""

import argparse


def get_args():
    """ Get the command-line arguments """

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar="name",
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """ main """

    args = get_args()
    name = args.name
    print("Hello, " + name + "!")


if __name__ == '__main__':
    main()
