# MongoDB Document Loader - loaddummydata

This Python script loads documents into a MongoDB database. It uses the `loaddata` module to manage the loading process.

## Requirements

- Python 3
- `pymongo` library
- `faker` library
- `tqdm` library
- `datetime` library
  
## Usage

The script is run from the command line and takes the following arguments:

- `--uri`: The MongoDB connection URL.
- `--database`: The name of MongoDB target database.
- `--collection`: The name of MongoDB target collection.
- `--deep`: The array size of the documents - number of inner documents.
- `--numdocs`: The number of documents to be loaded.
- `--batchsize`: The number of documents to be loaded per batch.

Here's an example of how to run the script:

```bash
python load.py --uri mongodb://localhost:27017/ --database mydatabase --collection mycollection --deep 1000 --numdocs 500 --batchsize 100
```

This will load 500 documents into the mycollection collection of the mydatabase database at mongodb://localhost:27017/. Each document will have an array size of 1000 and the documents will be loaded in batches of 100.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
