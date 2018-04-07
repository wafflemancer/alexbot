import calls.get_raw as raws
import calls.custom_dialogue as cd


all_function = {'raw': raws.latest(),
                'pad': raws.pad(),
                'joke': rand_joke()}

 

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
# be randomized.                
# NUM_JOKES = 6
                
def rand_joke():
    NUM_JOKES = 6
    bank = cd.dialogue_bank()
    msg = msg.strip()
    num = randint(1,NUM_JOKES)
    jokeselect = str(num) + 'joke'
    if jokeselect in bank.keys():
        convo = bank[jokeselect]
            if convo[1] is None:
                return convo[0]
            else:
                if convo[1](jokeselect):
                    return convo[0]
                else:
                    return None
    else:
        return None
