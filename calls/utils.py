import calls.get_raw as raws
import calls.custom_dialogue as cd


all_function = {'raw': raws.latest(),
                'pad': raws.pad(),
                'joke: get_joke()}

 

def get_function(msg):
    if msg == 'help':
        return all_function.keys()
    elif msg in all_function.keys():
        return all_function[msg]
    else:
        return get_dialogue(msg)


def get_dialogue(msg):
    bank = cd.dialogue_bank()
    msg = msg.strip()
    if msg in bank.keys():
        convo = bank[msg]
        if convo[1] is None:
            return convo[0]
        else:
            if convo[1](msg):
                return convo[0]
            else:
                return None
    else:
        return None

                
# Get random joke from custom dialogue
# Note: due to legacy implementation,
# number of jokes is hardcoded to
# be randomized, as well as line #.                
NUM_JOKES = 6
                
def get_joke(msg):
    bank = cd.dialogue_bank()
    msg = msg.strip()
    num = randint(1,NUM_JOKES)
    joke = str(num) + msg
    if joke in bank.keys():
        convo = bank[joke]
            if convo[1] is None:
                return convo[0]
            else:
                if convo[1](joke):
                    return convo[0]
                else:
                    return None
     else:
        return None
