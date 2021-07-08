
import argparse
import base64
import logging
import os
import sys

__version__ = "2017.06.04"


def main(argv):
    """
    Entry point for genpad.
    Arguments:
        argv: command line arguments
    """
    logging.basicConfig(level="WARNING", format="%(levelname)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        metavar="K",
        default=10,
        help="length of the key in kB (default 10)",
    )
    parser.add_argument("filename", type=str, help="name of the key-file.")
    args = parser.parse_args(argv)
    if args.length < 0:
        logging.error("Length must be a positive integer")
    keystring = genkey(args.length * 1024)
    if not args.filename.endswith(".key"):
        args.filename = args.filename + ".key"
    with open(args.filename, "w+") as kf:
        kf.write(keystring)


def genkey(length, chunklen=6, linelen=78):
    """
    Generate a one time pad.
    Arguments:
        length: Minimum length of the key in bytes.
        chuncklen: Length of the key segments (default 6 characters).
        linelen: Length of the output lines (default 78 characters).
    Returns:
        A string containing the base64 encoded key.
    """
    rem = length % 6
    if rem:
        length += 6 - rem
    nchunks = int(length // chunklen)
    rem = length % chunklen
    n = int(linelen // (4 * chunklen / 3))
    nums = [chunklen] * nchunks + [rem]
    chunks = [base64.b64encode(os.urandom(j)).decode("ascii") for j in nums]
    lines = [" ".join(chunks[i : i + n]) for i in range(0, len(chunks), n)]
    return "\n".join(lines)


if __name__ == "__main__":
        main(sys.argv[1:])