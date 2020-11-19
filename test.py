import argparse

from sampledbapi import SampleDB

parser = argparse.ArgumentParser()
parser.add_argument("address", help="Address of the SampleDB server to use.")
parser.add_argument("api_key", help="API token.")
args = parser.parse_args()

sdb = SampleDB(args.address, args.api_key)
print(sdb.getObjectList())
