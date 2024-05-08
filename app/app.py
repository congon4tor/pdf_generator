from flask import Flask, request, render_template, make_response, abort
import pdfkit


app = Flask(__name__)

events = [
    {
        'id': "1",
        'name': "In The Clouds",
        'image': "https://images.unsplash.com/photo-1524368535928-5b5e00ddc76b?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80",
        'date': "26 MAR 2021",
        'time': "08 PM - 01 AM",
        'description': "Signs rule there saying whales two appear fifth be subdue fruit upon without night day first from, isn't third fish darkness likeness under. You from, man was appear. Creature above abundantly fish. Multiply all, kind Male be fifth open heaven green herb dry, sea. Set was stars were fill face.",
        'capacity': 50,
        'price': 00.00
    },
    {
        'id': "2",
        'name': "Amplify Me",
        'image': "https://images.unsplash.com/photo-1429962714451-bb934ecdc4ec?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80",
        'date': "10 APR 2021",
        'time': "10 PM - 02 AM",
        'description': "Midst light first yielding. Two them seed very signs for. It Creature hath lesser. Light were thing which to good years years lesser cattle you're also spirit bearing. Blessed whose fruit you'll forth signs so multiply face is likeness. Moved whose years female give itself good, days thing moveth. Very.",
        'capacity': 80,
        'price': 00.00
    },
    {
        'id': "3",
        'name': "Electric Parrot",
        'image': "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80",
        'date': "20 JUN 2021",
        'time': "08 PM - 01 AM",
        'description': "Of there all upon lesser spirit third every signs darkness is signs creeping bring cattle waters one midst likeness created fruitful saw. Moveth don't you can't lesser he, over firmament. In yielding very were dry let living it which forth creature fruitful above green. Set. Were, doesn't very dominion firmament.",
        'capacity': 150,
        'price': 00.00
    },
    {
        'id': "4",
        'name': "FunkedUp",
        'image': "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80",
        'date': "8 JUL 2021",
        'time': "06 PM - 10 PM",
        'description': "Beginning fly darkness behold he Have grass us lesser. Earth seed there is above fish two darkness. Rule dry first it. Wherein hath moved you're fly. You, whose deep tree. Have be itself cattle morning face creeping fruitful under darkness behold them don't saw, itself give likeness stars may divide.",
        'capacity': 100,
        'price': 00.00
    },
    {
        'id': "5",
        'name': "Summer Sounds",
        'image': "https://images.unsplash.com/photo-1464375117522-1311d6a5b81f?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80",
        'date': "21 NOV 2021",
        'time': "10 PM - 01 AM",
        'description': "Gathered face years after subdue days two spirit form fifth have which let, a. Their they're unto moveth isn't subdue midst stars said moveth. Upon forth two, fruit seasons signs gathered dominion male subdue one earth male rule was open fruitful brought, open very. Face you're under, green moved.",
        'capacity': 120,
        'price': 00.00
    },
    {
        'id': "6",
        'name': "Flag Sounds",
        'image': "https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1350&q=80",
        'date': "25 DEC 2021",
        'time': "11 PM - 06 AM",
        'description': "Super exclusive event where the content of /flag.txt will finally be revealed. Don't miss your chance this is a once in a lifetime opportunity!",
        'capacity': 10,
        'price': 00.00
    },
]


options = {
    'enable-javascript':''
}


@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/event/<id>')
def event(id):
    event = next(filter(lambda x: x['id'] == id, events), None)
    if not event:
        abort(404,"Event not found")
    return render_template('event.html', event=event)
    
@app.route('/ticket/<id>', methods=['POST'])
def ticket(id):
    event = next(filter(lambda x: x['id'] == id, events), None)
    if not event:
        abort(404,"Event not found")

    name = request.form.get("name", None)
    email = request.form.get("email", None)

    if not name or not email:
        abort(400,"A full name and email must be provided")

    rendered = render_template("pdf_template.html", event=event, name=name, email=email)
    pdf = pdfkit.from_string(rendered, False, options=options)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=ticket.pdf"

    return response
