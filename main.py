#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
state_1.save()
state_2 = State(name="Arizona")
state_2.save()
"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    print("Find the city {} in the state".format(state))
print(all_states)

