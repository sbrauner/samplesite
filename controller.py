from _10gen import db, local

data = db.count.findOne()
if ( data is None ): 
   data = { 'count':0 }

data.count +=1
db.count.save(data)

local.templates.template1({ "theCount" : data.count })
local.templates.template2({"countThis" : data.count })
local.templates.template3({ "countThat" : data.count })



