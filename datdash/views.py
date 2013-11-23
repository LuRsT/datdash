from Queue import Queue
from os import getcwd
from os.path import isfile as is_file
from os.path import join as join_path

from coffeescript import compile_file as compile_coffeescript_file
from flask import Response
from flask import current_app
from flask import render_template
from flask import request
from flask import send_from_directory
from flask_sockets import Sockets
from scss import Scss

from datdash import DATDASH_APP_NAME
from datdash import event_handler
from datdash import datdash_app
from datdash.views_utils import get_javascripts
from datdash.views_utils import get_stylesheets


sockets = Sockets(datdash_app)


@datdash_app.route('/')
def dashboard():
    return render_template("main.html", title="DatDash")


@datdash_app.route("/assets/application.js")
def serve_javascript():
    if not hasattr(current_app, "javascript"):
        javascripts = get_javascripts()

        output = []
        for path in javascripts:
            output.append("// JS: %s\n" % path)
            if ".coffee" in path:
                print("Compiling Coffee for %s " % path)
                contents = \
                    compile_coffeescript_file(path).encode("ascii", "ignore")
            else:
                print("Reading JS for %s " % path)
                f = open(path)
                contents = f.read()
                f.close()

            output.append(contents)

        current_app.javascripts = "\n".join(output)

    return Response(current_app.javascripts, mimetype="application/javascript")


@datdash_app.route("/assets/application.css")
def serve_css():
    parser = Scss()

    stylesheets = get_stylesheets()

    output = []
    for path in stylesheets:
        if ".scss" in path:
            contents = parser.compile(scss_file=path)
        else:
            f = open(path)
            contents = f.read()
            f.close()

        output.append(contents)

    return Response("\n".join(output), mimetype="text/css")


@datdash_app.route("/assets/images/<path:filename>")
def serve_image(filename):
    directory = join_path(getcwd(), DATDASH_APP_NAME, "assets", "images")
    return send_from_directory(directory, filename)


@datdash_app.route("/views/<widget_name>.html")
def serve_widget(widget_name):
    html = "%s.html" % widget_name
    path = join_path(
        getcwd(),
        DATDASH_APP_NAME,
        "widgets",
        widget_name,
        html
    )
    if is_file(path):
        f = open(path)
        contents = f.read()
        f.close()
        return contents


@datdash_app.route('/events')
def serve_events():
    event_stream_port = request.environ["REMOTE_PORT"]
    current_event_queue = Queue()
    event_handler.events_queue[event_stream_port] = current_event_queue
    current_app.logger.info(
        "New Client %s connected. Total Clients: %s" %
        (event_stream_port, len(event_handler.events_queue))
    )

    for event in event_handler.last_events.values():
        current_event_queue.put(event)

    return Response(
        event_handler.pop_queue(event_stream_port),
        mimetype="text/event-stream",
    )

