from pymongo import MongoClient
from faker import Faker
from datetime import datetime
from tqdm import tqdm

class LoadDataManager:
    def __init__(self, howlarge, targeturi, targetdb, targetcollection, numdocs, batchsize):
        self.targeturi = targeturi
        self.targetdb = targetdb
        self.targetcollection = targetcollection
        self.howlarge = howlarge
        self.numdocs = numdocs
        self.batchsize = batchsize
        self.client = None
        self.db = None

    def conn(self):
        self.client = MongoClient(self.targeturi)
        self.db = self.client[self.targetdb]

    def lodddata(self):
        coll = self.db[self.targetcollection]
        fake = Faker()
        try:
            highest_document = coll.find_one(sort=[('a', -1)])
            highest_a_document = highest_document["a"]
        except TypeError:
            highest_a_document = 1
        avalue = highest_a_document
        #total_batches = (highest_a_document + self.numdocs - 1) // self.batchsize + 1
        total_batches = (self.numdocs - 1) // self.batchsize + 1
        with tqdm(total=total_batches, desc="Inserting batches", ncols=70) as pbar:
            for i in range(highest_a_document, highest_a_document + self.numdocs, self.batchsize):
                batch = []
                for _ in range(self.batchsize):
                    large_document = {
                        "name": fake.name(),
                        "email": fake.email(),
                        "address": fake.address(),
                        "a": avalue,
                        "b": f"value {avalue}",
                        "c": f"value {avalue}",
                        "d": [
                            {
                                "sub_d_a": f"subvalue {avalue}",
                                "sub_d_b": f"subvalue {avalue}",
                                "updatedAt": "",
                                "insertedAt": datetime.now()
                            } for _ in range(self.howlarge)
                        ],
                        "e": [
                            {
                                "sub_e_a": f"subvalue {avalue}",
                                "sub_e_b": f"subvalue {avalue}",
                                "updatedAt": "",
                                "insertedAt": datetime.now()
                            } for _ in range(self.howlarge)
                        ],
                    }
                    batch.append(large_document)
                    avalue += 1
                coll.insert_many(batch)
                pbar.update()