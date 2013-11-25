DatDash
=======

![Datdash](http://cdn.memegenerator.net/instances/500x/43245340.jpg)

This is a python dashboard framework inspired by
[Dashing](http://shopify.github.io/dashing/)/
[pyDashie](https://github.com/evolvedlight/pydashie) but without
the ruby and the ponies.

The aim of this project is to have the best aproximation possible to
[Dashing](http://shopify.github.io/dashing/) and possibly total compatibility.

## Instructions:

    git clone https://github.com/LuRsT/datdash
    mkvirtualenv datdash
    pip install -r requirements *
    python setup.py install
    cd /tmp # or whatever you want
    datdash new
    datdash start
    # Go to localhost:5000 in your browser

And that's it, you're ready to go!


* There's a bug right now where you have to do this since setup.py is not
installing Markup
