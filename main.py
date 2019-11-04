import argparse
import game

parser = argparse.ArgumentParser(description='Play the Wiki Game!')
parser.add_argument('--start', type=str, help='Starting Wikipedia URL')
parser.add_argument('--end', type=str, help='Ending Wikipedia URL')
parser.add_argument('--limit', type=int, help='Limit the maximum distance of pages to check before quitting (number of pages will grow exponentially)')

args = parser.parse_args()
args.limit = args.limit or 6 # RIP your RAM; at your own risk

print(args)

game.play(args.start,args.end,args.limit)