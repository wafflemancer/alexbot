import calls.get_raw as raws
import calls.custom_dialogue as cd


all_function = {'!raw': raws.latest(),
                '!pad': raws.pad()}


def get_function(msg):
    if msg == '!help':
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
