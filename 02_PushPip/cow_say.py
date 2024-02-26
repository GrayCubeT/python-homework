from cowsay import cowsay
from cowsay import list_cows
import argparse

parser = argparse.ArgumentParser(prog="cowsay", description="write a message as a cow")
# -h is helper auto generated(?)
parser.add_argument("message", nargs="?", default="", help="the message for a cow")
parser.add_argument("-e", default="oo", help="eye string")
parser.add_argument("-f", help="file for a cow")
parser.add_argument("-I", action="store_true", help="list all cowfiles on COWPATH")
parser.add_argument("-n", action="store_false", help="no wrap around flag")
parser.add_argument("-T", default="", help="tongue string")
parser.add_argument("-W", default=40, type=int, help="width of a talking box")

args = parser.parse_args()
preset = ""

print(cowsay(args.message, preset=preset, eyes=args.e, tongue=args.T,width=args.W, wrap_text=args.n, cowfile=args.f))