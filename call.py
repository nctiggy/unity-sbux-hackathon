import couchdb


params1 = {
  "serialNumber": "00182672345",
  "ipAddress": "192.168.0.124",
  "model": "vmax",
  "vendor": "DellEMC",
  "installDate": "03/25/2017",
  "maintenanceContractEndDate": "12/25/2017",
  "location": "Ashburn",
  "environment": "production",
  "status": "ok",
  "tier": "performance"
        }

params2 = {
  "serialNumber": "VIRT1735TG8NVL",
  "ipAddress": "10.253.232.18",
  "model": "unity",
  "vendor": "DellEMC",
  "installDate": "03/25/2017",
  "maintenanceContractEndDate": "03/25/2021",
  "location": "Chandler",
  "environment": "production",
  "status": "Full",
  "tier": "standard"
        }

couch = couchdb.Server()
dbname = 'storage'
if not dbname in couch:
    db = couch.create(dbname)
db = couch[dbname]
#else:
#    db = couch.create(dbname)
db.save(params1)
db.save(params2)
