# gae-flask-html5

## What is this?

It's just a simple [Flask](http://flask.pocoo.org/) skeleton for
[Google App Engine](http://appengine.google.com/),
but made with all the baked-in-goodness of
[html5 boilerplate](https://github.com/paulirish/html5-boilerplate).

I'm planning on using this for my GAE projects going forward (I really
like the speed of [Flask](http://flask.pocoo.org/) compared to
[Django-Nonrel](http://code.google.com/appengine/articles/django-nonrel.html)
on GAE), so I thought someone else might find it useful, too.

Just about everything is ready to go right out of the box -- including
`qunit` for JavaScript tests and a `tests.py` file for Python `unittest`.
Also, I included a `style.less` file since I primarily only use the
[Less app](http://incident57.com/less/) when writing stylesheets nowadays.


## Why should I use it?

I stumbled a bit figuring out how to add the `unittest` module and setup an
`appengine_console.py` file to connect to GAE's remote API, so this skeleton
might come in handy for you.

I looked at two other Flask GAE skeletons on Github
([flask-gae-skeleton](https://github.com/blossom/flask-gae-skeleton)
and [flask-gae-template](https://github.com/jugyo/flask-gae-template)
-- both of which were awesome for learning), and I adapted what
I felt were some of their best parts.

Also, this is my first Github project, so I felt it'd be a good challenge.

Lastly, as an added bonus, the scripts are PEP8 compliant.


## How do I use it?

Make sure you have the [Google App Engine SDK](http://appengine.google.com/)
installed on your computer, and you've created an application for your
Google account.

### Setup

    git clone https://github.com/zachwill/gae-flask-html5.git <your_app_name_here>

### Run

    cd /path/to/your/app
    dev_appserver.py .

### Test

    cd /path/to/your/app
    python tests.py

### Deploy

    cd /path/to/your/app
    appcfg.py update .


# Todo

* add more tests to `tests.py`
