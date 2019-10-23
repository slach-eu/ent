# -*- coding: utf-8 -*-
import argparse
import logging


def main():
    """Parse command line arguments and bootstap package."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='count', help="print debug messages")
    parser.add_argument('package', nargs='*', help='package name')
    args = parser.parse_args()

    # setup logging
    logging.getLogger().setLevel(logging.DEBUG if args.debug else logging.INFO)

    # print package name
    logging.info('Create package {}'.format(args.package))
