from glob import glob
from os import getcwd
from os.path import abspath as absolute_path
from os.path import dirname as dir_name
from os.path import join as join_path

from datdash import DATDASH_APP_NAME


def get_javascripts():
    ordered_script_names = [
        "jquery.js",
        "es5-shim.js",
        "d3.v2.min.js",
        "batman.js",
        "batman.jquery.js",
        "jquery.gridster.js",
        "jquery.leanModal.min.js",
        "dashing.gridster.coffee",
        "jquery.knob.js",
        "rickshaw.min.js"
    ]

    javascripts = []
    for js in ordered_script_names:
        script_filename = join_path(
            dir_name(absolute_path(__file__)),
            "javascript",
            js
        )
        javascripts.append(script_filename)
    for ext in ["js", "coffee"]:
        javascripts.extend(
            glob(
                join_path(
                    getcwd(),
                    DATDASH_APP_NAME,
                    "assets/**/*.%s"
                ) % ext
            )
        )
    for ext in ["js", "coffee"]:
        javascripts.extend(
            glob(
                join_path(
                    getcwd(),
                    DATDASH_APP_NAME,
                    "widgets/**/*.%s"
                ) % ext
            )
        )
    return javascripts


def get_stylesheets():
    stylesheets = []
    for ext in ["css", "scss"]:
        stylesheets.extend(
            glob(
                join_path(
                    getcwd(),
                    DATDASH_APP_NAME,
                    "assets/**/*.%s"
                ) % ext
            )
        )
    for ext in ["css", "scss"]:
        stylesheets.extend(
            glob(
                join_path(
                    getcwd(),
                    DATDASH_APP_NAME,
                    "widgets/**/*.%s"
                ) % ext
            )
        )
    return stylesheets

