import os
import sys
import logging
import wsgiref.simple_server
from argparse import ArgumentParser
# import dialogue and function call stuff
import calls.utils as cutil
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

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        # get message text
        msg = event.message.text
        msg = msg.lower()
        # function calls
        if (msg[0] == '!') and (len(msg) > 1):
            answer = cutil.get_function(msg[1:])
            if answer is not None:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=answer)
                )
        # normal dialogue calls
        elif (msg[0:5] == 'alex,') and (len(msg) > 5):
            answer = cutil.get_dialogue(msg[5:])
            if answer is not None:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=answer)
                )
        elif (msg[0:4] == 'alex') and (len(msg) > 4):
            answer = cutil.get_dialogue(msg[4:])
            if answer is not None:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=answer)
                )
        # greetings and goodbyes
        elif ('hello' in msg or 'hi' in msg) and ('alex' in msg):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Hello.')
            )
        elif ('hello' in msg or 'hi' in msg) and ('mister' in msg):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='*nods*')
            )
        elif ('goodbye' in msg or 'bye' in msg) and ('mister' in msg or
                                                     'alex' in msg):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='...Night.')
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
