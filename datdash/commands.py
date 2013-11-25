import sys
from os.path import abspath as abs_path
from shutil import copytree as copy_tree
from os.path import dirname as dir_name

from datdash import datdash_app
from datdash import DATDASH_APP_NAME
from datdash import event_handler


def create_new_dashboard(dashboard_name):
    copy_tree(
        dir_name(abs_path(__file__)) + "/skeleton",
        DATDASH_APP_NAME,
    )


def start_dashboard(dashboard_name):
    sys.path.append('.')
    exec("import {} as app".format(DATDASH_APP_NAME))
    app.run(datdash_app, event_handler)

