import couchdb


params = {
    'ipAddress': '192.168.0.34',
    'model': 'UnityVSA',
    'serialNumber': '123456789',
    'arrayName': 'myUnity',
    'softwareVersion': '4.2.0'}
couch = couchdb.Server()
dbname = 'unity'
#if dbname in couch:
db = couch[dbname]
#else:
#    db = couch.create(dbname)
db.save(params)
