import couchdb
import json


class Couch_storage:

    def __init__(self, params):
        self.hostname = params['couchdb_hostname']
        self.port = params['couchdb_port']
        self.dbName = params['couchdb_name']
        self.couch = couchdb.Server('http://'+self.hostname+':'+self.port)
        self.db = self.couch[self.dbName]

    def returnAll(self):
        print(self.hostname+" "+self.dbName)
        result = []
        for id in self.db:
            item = self.db[id]
            result.append(
                    {"serialNumber": item['serialNumber'],
                        "ipAddress": item['ipAddress']}
                    )
        return result

    def createNew(self, params):
        print(params)
        print(type(params))
        self.db.save(params)
