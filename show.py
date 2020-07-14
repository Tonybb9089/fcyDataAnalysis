import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default="ls -al", help="the file name")
args = parser.parse_args()
file = args.f
print("*******************************************************p1****************************")
command_p1 = "cat "+file+" |strings|grep pre_commit_phase1|grep filcrypto"
os.system(command_p1)
print("******************************************************p2****************************")
command_p2 = "cat "+file+" |strings|grep pre_commit_phase2|grep filcrypto"
os.system(command_p2)

