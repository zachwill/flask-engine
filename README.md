gae-flask-html5
===============

# What is this?

Just a simple Flask skeleton for Google App Engine, but made with all the
baked-in-goodness of html5 boilerplate.

I'm planning on using this for my projects going forward (really like the
speed of Flask compared to Django-Nonrel on GAE), so I thought someone
else might find it useful, too.

Also, I included a style.less file since I primarily only use the Less app
(http://incident57.com/less/) when writing stylesheets nowadays.


Setup
------

    git clone https://github.com/zachwill/gae-flask-html5.git <your_app_name>

Run
------

    dev_appserver.py .

Deploy
------

    appcfg.py update .
