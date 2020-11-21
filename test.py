import argparse

from sampledbapi import *

parser = argparse.ArgumentParser()
parser.add_argument("address", help="Address of the SampleDB server to use.")
parser.add_argument("api_key", help="API token.")
args = parser.parse_args()

authenticate(args.address, args.api_key)
# print(objects.getList())
# print(objects.get(123))
print(instruments.getList())
print(instruments.get(1))
