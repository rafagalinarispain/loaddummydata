import argparse
import loaddata as ldm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Loading documents into MongoDB.')
    parser.add_argument('--uri', required=True, help='The MongoDB connection URL.')
    parser.add_argument('--database', required=True, help='The MongoDB database name.')
    parser.add_argument('--collection', required=True, help='The MongoDB collection name.')
    parser.add_argument('--deep', type=int, required=True, help='How deep is the array size of the documents - number of inner documents.')
    parser.add_argument('--numdocs', type=int, required=True, help='How many docs wil be loaded')
    parser.add_argument('--batchsize', type=int, required=True, help='How many docs wil be loaded')
    args = parser.parse_args()
    load = ldm.LoadDataManager(args.deep, args.uri, args.database,args.collection,args.numdocs,args.batchsize)
    load.conn()
    load.lodddata()
