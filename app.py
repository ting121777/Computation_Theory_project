from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "1234567890987654321"

machine = TocMachine(
    states=[
        'user',
        'hello',
        'usage',
        'song',
        'joke',
        'joke1',
        'joke2',
        'joke3',
        'Audio',
        'q2',
        'Grow',
        'q3',
        '2002',
        'q4',
        '9420',
        'q5',
        'FU',
        'QQ'

    ],
    transitions=[
        {
            'trigger': 'hello',
            'source': ['user', 'hello', 'usage', 'song', 'joke', 'joke1', 'joke2', 'joke3', 'Audio', 'q2', 'Grow', 'q3', '2002', 'q4', '9420', 'q5', 'FU', 'QQ'],
            'dest': 'hello'
        },
        {
            'trigger': 'usage',
            'source': ['hello', 'song', 'joke', 'usage', 'joke1', 'joke2', 'joke3', 'Audio', 'q2', 'Grow', 'q3', '2002', 'q4', '9420', 'q5', 'FU', 'QQ'],
            'dest': 'usage'
        },
        {
            'trigger': 'song',
            'source': ['hello', 'usage', 'joke', 'song', 'joke1', 'joke2', 'joke3', 'Audio', 'q2', 'Grow', 'q3', '2002', 'q4', '9420', 'q5', 'FU', 'QQ'],
            'dest': 'song'
        },
        {
            'trigger': 'joke',
            'source': ['hello', 'usage', 'song', 'joke', 'joke3', 'Audio', 'q2', 'Grow', 'q3', '2002', 'q4', '9420', 'q5', 'FU', 'QQ'],
            'dest': 'joke'
        },
        {
            'trigger': 'joke1',
            'source': 'joke',
            'dest': 'joke1'
        },
        {
            'trigger': 'joke2',
            'source': 'joke1',
            'dest': 'joke2'
        },
        {
            'trigger': 'joke3',
            'source': 'joke2',
            'dest': 'joke3'
        },
        {
            'trigger': 'yes_q1',
            'source': 'song',
            'dest': 'Audio'
        },
        {
            'trigger': 'no_q1',
            'source': 'song',
            'dest': 'q2'
        },
        {
            'trigger': 'yes_q2',
            'source': ['Audio','q2'],
            'dest': 'Grow'
        },
        {
            'trigger': 'no_q2',
            'source': ['Audio', 'q2'],
            'dest': 'q3'
        },
        {
            'trigger': 'yes_q3',
            'source': ['Grow','q3'],
            'dest': '2002'
        },
        {
            'trigger': 'no_q3',
            'source': ['Grow', 'q3'],
            'dest': 'q4'
        },
        {
            'trigger': 'yes_q4',
            'source': ['2002','q4'],
            'dest': '9420'
        },
        {
            'trigger': 'no_q4',
            'source': ['2002', 'q4'],
            'dest': 'q5'
        },
        {
            'trigger': 'yes_q5',
            'source': ['9420','q5'],
            'dest': 'FU'
        },
        {
            'trigger': 'no_q5',
            'source': ['9420', 'q5'],
            'dest': 'QQ'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page" and machine.state == 'user':
        event = body['entry'][0]['messaging'][0]
        machine.hello(event)
        return 'OK'
    elif body['object'] == "page" and machine.state == 'hello':
        if body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'usage':
        if body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        else: 
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'joke':
        if body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke1(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'joke1':
        if body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke2(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'joke2':
        if body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke3(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'joke3':
        if body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'song':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q1(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q1(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'Audio':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q2(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q2(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'q2':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q2(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q2(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'Grow':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q3(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q3(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'q3':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q3(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q3(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == '2002':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q4(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q4(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'q4':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q4(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q4(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == '9420':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q5(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q5(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'q5':
        if body['entry'][0]['messaging'][0]['message']['text'] == "yes":
            event = body['entry'][0]['messaging'][0]
            machine.yes_q5(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "no":
            event = body['entry'][0]['messaging'][0]
            machine.no_q5(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'FU':
        if body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'
    elif body['object'] == "page" and machine.state == 'QQ':
        if body['entry'][0]['messaging'][0]['message']['text'] == "usage":
            event = body['entry'][0]['messaging'][0]
            machine.usage(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "song":
            event = body['entry'][0]['messaging'][0]
            machine.song(event)
            return 'OK'
        elif body['entry'][0]['messaging'][0]['message']['text'] == "joke":
            event = body['entry'][0]['messaging'][0]
            machine.joke(event)
            return 'OK'
        else:
            #body['entry'][0]['messaging'][0]['message']['text'] = "hello"
            event = body['entry'][0]['messaging'][0]
            machine.hello(event)
            return 'OK'

@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
