import argparse
import game

parser = argparse.ArgumentParser(description='Play the Wiki Game!')
parser.add_argument('--start', type=str, help='Starting Wikipedia URL')
parser.add_argument('--end', type=str, help='Ending Wikipedia URL')

args = parser.parse_args()

print(args)

game.play(args.start,args.end)