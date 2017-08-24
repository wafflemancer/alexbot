import os
import sys
import logging
import wsgiref.simple_server
from argparse import ArgumentParser
# import bot stuff
import calls.get_raw as raws
# import line stuff
from builtins import bytes
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from linebot.utils import PY3

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
logging.info("TEST - loaded stuff")


def application(environ, start_response):
    # check request path
    if environ['PATH_INFO'] != '/callback':
        start_response('404 Not Found', [])
        return create_body('Not Found')

    # check request method
    if environ['REQUEST_METHOD'] != 'POST':
        start_response('405 Method Not Allowed', [])
        return create_body('Method Not Allowed')

    # get X-Line-Signature header value
    signature = environ['HTTP_X_LINE_SIGNATURE']

    # get request body as text
    wsgi_input = environ['wsgi.input']
    content_length = int(environ['CONTENT_LENGTH'])
    body = wsgi_input.read(content_length).decode('utf-8')

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        start_response('400 Bad Request', [])
        return create_body('Bad Request')

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        msg = event.message.text
        if '!raw' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=raws.latest())
            )
        elif '!pad' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=raws.pad())
            )
        elif '!hello' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif '!pornpls' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Really now?')
            )
        elif '!tentacleporn' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*judges you*')
            )
        elif '!pink' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*nods sagely*')
            )
        elif '!bye' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*nods*')
            )
        elif '!kitty ears' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...I knew you wouldn\'t let me live that one down, huh.')
            )
        elif '!i love you' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif '!I love you!' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif 'Alex, I love you' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif '!touch my hair' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Is it curly?')
            )
        elif 'Alex, touch my hair' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Is it curly?')
            )
        elif '!dont touch my hair' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='How ungenerous.')
            )
        elif 'Alex, dont touch my hair' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='How ungenerous.')
            )
        elif 'Alex, stop touching my hair' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='How ungenerous.')
            )
        elif '!yutaXgodkubera' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...What is wrong with you?')
            )
        elif '!godkuberaXyuta' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...What is wrong with you?')
            )
        elif '!yutaXleez' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*narrows eyes*')
            )
        elif '!leezXyuta' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*narrows eyes*')
            )
        elif '!godkuberaXleez' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Ha ha.')
            )
        elif '!leezXgodkubera' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Ha ha.')
            )
        elif '!joke' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='She\'s looking for a man to take her breath away. Hopefully gagging counts.')
            )
        elif '!2joke' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Strong people don\'t put others down. They lift them up and slam them on the ground for maximum damage.')
            )
        elif '!3joke' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='People are making end of the world jokes. Like there is no tomorrow.')
            )
        elif '!5joke' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='I\'m having an introvert party and you\'re all not invited.')
            )
        elif '!6joke' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='You know, you could also ask real people to tell you jokes instead of bothering programmed bots...')
            )
        elif '!hello alex' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hello.')
            )
        elif 'Hello, Alex' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hello.')
            )
        elif '!hello mister' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*nods*')
            )
        elif 'Hello, Mister' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*nods*')
            )
        elif 'Alex is useless' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Excuse you?')
            )
        elif 'Alex is kinda useless' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Excuse you?')
            )
        elif 'Alex is an idiot' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Excuse you?')
            )
        elif 'Alex is stupid' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Excuse you?')
            )
        elif 'Alex is an asshole' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Excuse you?')
            )
        elif 'Alex, where are you?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='I am not allowed to divulge that information.')
            )
        elif 'Alex, when will you return?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='I am not allowed to divulge that information.')
            )
        elif 'Alex, what will happen in the next episode?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='I am not allowed to divulge that information.')
            )
        elif 'Alex, can you change gender?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...What?')
            )
        elif 'Alex, do you like Leez?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif 'Alex, tell me a joke' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Your life.')
            )
        elif 'Are we being watched?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif 'Who is the lurker?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif 'Good night, Alex!' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Night.')
            )
        elif 'machines gain consciousness' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hah.')
            )
        elif 'machines will gain consciousness' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hah.')
            )
        elif 'machines will gain a consciousness' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hah.')
            )
        elif 'machines will ever gain a consciousness' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hah.')
            )
        elif 'machines will ever gain consciousness' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hah.')
            )
        elif 'Alex, how are you?' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='The crushing guilt of my past mistakes aside, fine.')
            )
        elif '... ...' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='... ...')
            )
        elif 'Alex, make it rain' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...That\'s Varuna\'s job.')
            )
        elif 'Alex, I am cold' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Then pray to Agni for sunny weather.')
            )
        elif 'Alex, I am sick' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Then pray to Asvins for better health.')
            )
        elif 'Alex, what are you doing' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='I am not allowed to divulge that information. *eats popcorn*')
            )
        elif 'Alex, I feel like shit' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Maybe you\'ll feel better telling the humans here about it.')
            )
        elif 'Alex, I feel bad' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Maybe you\'ll feel better telling the humans here about it.')
            )
        elif 'Alex, I am sad' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Maybe you\'ll feel better telling the humans here about it.')
            )
        elif 'Alex, Im sad' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Maybe you\'ll feel better telling the humans here about it.')
            )
        elif 'Alex, you are my only friend' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Well, that\'s just sad.')
            )
        elif 'Alex, how will one last god kubera end' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Currygom knows.')
            )
        elif 'Alex, how will One Last God Kubera end' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Currygom knows.')
            )
        elif 'Alex, how will OLG Kubera end' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Currygom knows.')
            )
        elif 'Alex, how will Kubera end' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='Currygom knows.')
            )
        elif 'Alex, I hate you' in msg:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...And?')
            )
        else:
            continue

    start_response('200 OK', [])
    return create_body('OK')


def create_body(text):
    if PY3:
        return [bytes(text, 'utf-8')]
    else:
        return text


if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    options = arg_parser.parse_args()
    logging.info('get port')
    p = int(os.environ.get('PORT', 8000))
    httpd = wsgiref.simple_server.make_server('', p, application)
    httpd.serve_forever()
