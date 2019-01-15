#update, delete
#Atomic => id

import mlab
from models.character import Character

mlab.connect()

character=Character.objects().with_id("5c34a7ed6e512012742e6cea")
# character.update(inc__rate=1)
# character.reload()
# print(characte.rate)
character.delete()
#1. Delete
#1.1 read document
#1.2 Update document


#2. Delete
#2.1 Read document
