from modules.SqlRel.models.oo_models import Bottle, Cap

# Basic Card Operation
#add

bottle  = Bottle.objects.create(bottle_name="sprite")
cap = Cap.objects.create(bottle=bottle)
#print(cap)

# retrive
bottle = Bottle.objects.filter(bottle_name="sprite")
cap = Cap.objects.filter(bottle__bottle_name="sprite")
#print(cap)

# update
Bottle.objects.filter(bottle_name="sprite").update(
    bottle_name = "Mirinda"
)
#print(Bottle.objects.filter(bottle_name="Mirinda")) 


# delete
Bottle.objects.filter(bottle_name="Thumbsup").delete()

