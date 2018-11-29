import calls.get_raw as raws
import calls.custom_dialogue as cd
import calls.attribute as atb


basic_functions = {'raw': raws.latest(),
                'pad': raws.pad()}

def get_function(msg):
    if msg == 'help':
        return 'sorry i can\'t tell you'
    elif msg in basic_functions.keys():
        return basic_functions[msg]
    elif msg[0:8] == 'birthday':
        return atb.get_attributes(msg[9:])
    elif msg[0:8] == 'today':
        return atb.get_today()
    else:
        return get_dialogue(msg)


def get_dialogue(msg):
    bank = cd.dialogue_bank()
    msg = msg.strip()
    if msg in bank.keys():
        convo = bank[msg]
        return convo[0]
    else:
        return None
