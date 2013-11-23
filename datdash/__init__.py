import sys

from os import getcwd
from os.path import join as join_path

from event_handler import EventHandler
from flask import Flask

DATDASH_APP_NAME = 'datdash_app'

event_handler = EventHandler()

datdash_app = Flask(
    __name__,
    template_folder=join_path(getcwd(), DATDASH_APP_NAME, "templates"),
)

import datdash.views
