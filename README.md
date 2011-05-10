Flask Engine
===============

<pre><code>
                                                           EE                   
                                                          EtjK                  
                                                          EtjG                  
                f                                         EjfLE                 
              ###                     ##                  EffLGE  KEKKE         
   #########  ###                     ##                  ELLLGDK:.:::::K       
    ##     #   ##                      #                  ELLLG,,:::LLt:,K      
    ##         ##                      #                  ELL:,,.:,Ltfjt::.     
    ##         ##                      #                  EG,,,:.:i,itttt:K     
    ##         ##                      #                  E,,,,.:;;:;.ttt::     
    ##   #     ##     ####     ####    #  #####          E,,,,,,:LLL.i;tt,,     
    ######     ##    ## .#    #   #.   #   ##           E,,,,,,::LLti,:tti,     
    ##   #     ##    t   #    ##       #  #             K,,,,,,::GGGGiitti,.    
    ##         ##        #    ###.     # ##             EKKKKE,,:GGG,,,tt,,     
    ##         ##    L## #      ###    ## ##         EEjtjLtGD:::ff;itttt,:KE   
    ##         ##   ##   #        ##   #  ##;      EDLLfiDDDDD,,::t:,;itt,DGGE  
    ##         ##   ##   #   :#   ##   #.  ##.    ,jtffLGGEE;,,,,,ittftt,,GGDf  
   ####i      f###  ########  #####   ###K  ###L   KELDEK Eii,,,,,,,jtt,,EGj    
                                                           Kj,,,,,,,,,,:E       
                                                             ED:,,,,,,ED        
                                                                jEKEt           


                      github.com/zachwill/flask-engine

</code></pre>


Changelog
---------

###V1.0.3
* Renamed repo to `Flask Engine`
  * Run `git remote set-url upstream https://github.com/zachwill/flask-engine`

Sorry about any headaches this causes, but the name `gae-flask-html5` had become
a little too verbose. You can still `git pull upstream` from any changes/updates
I make -- just make sure you either `git remote set-url` or do the following:
`git remote rm upstream` and then `git remote add upstream
https://github.com/zachwill/flask-engine`.

###V1.0.2

* Minor fixes to `views.py` file.
* Ajax functionality for adding todos.

###V1.0.1

* Fixed bug with `werkzeug_debugger_appengine` submodule.
* Minor changes to files (fixed grammar issues, deleted comments, etc).

### V1.0

* Added send email functionality.
    * **NOTE**: You'll have to update the `from_address` variable in `views.py`
      for it to work properly.
    * Don't forget to run the development server with the
      `dev_appserver.py --enable_sendmail .` command.
* Added `test.py` file for running unittest. Deleted `gaeunit.py`.
    * Tests kept in `tests` directory.
    * Now uses GAE v1.4.3's `testbed` functionality.


What is this?
-------------

It's just a simple [Flask](http://flask.pocoo.org/) skeleton for
[Google App Engine](http://appengine.google.com/),
but made with all the baked-in-goodness of
[html5 boilerplate](https://github.com/paulirish/html5-boilerplate).

I'm planning on using this for my GAE projects going forward (I really
like the speed of [Flask](http://flask.pocoo.org/) compared to
[Django-Nonrel](http://code.google.com/appengine/articles/django-nonrel.html)
on GAE), so I thought someone else might find it useful, too.

Just about everything is ready to go right out of the box -- including
`QUnit` for JavaScript tests and a `tests` directory for Python's `unittest`.
Also, I included a `style.less` file since I primarily only use the
[Less.app](http://incident57.com/less/) when writing stylesheets nowadays.


Why should I use it?
---------------------

I stumbled a bit figuring out how to add tests and use the `unittest` module,
and also setup an `appengine_console.py` file to connect to GAE's remote API,
so this skeleton might come in handy for you.

I looked at two other Flask GAE skeletons on Github
([flask-gae-skeleton](https://github.com/blossom/flask-gae-skeleton)
and [flask-gae-template](https://github.com/jugyo/flask-gae-template)
-- both of which were awesome for learning), and I adapted what
I felt were some of their best parts. Recently, I've updated this project's
structure after browsing the source code of
[another GAE project skeleton](https://github.com/franciscosouza/labs).

Lastly, as an added bonus, the scripts are PEP8 compliant.


How do I use it?
----------------

Make sure you have the [Google App Engine SDK](http://appengine.google.com/)
installed on your computer, and you've created an application for your
Google account. The SDK will also install symlinks to its packages on your
computer.

### Steps to Get Up and Running

1. Create a new application on [Google App Engine](http://appengine.google.com/).

2. `git clone` this repo into your personal project folder.

3. Amend the `app.yaml` file with your application's name.

4. Run the project from your development server (use the `dev_appserver.py .`
command or use the Google App Engine Launcher GUI).

5. Browse the sample application in your web browser: `http://localhost:8080`

6. Once you're ready to read the source code, check out the `app` directory.

7. All static media is stored in the `static` directory.
    * This includes your favicon, `robots.txt`, and `humans.txt`

8. Before you deploy, don't forget to:
    * Update the `humans.txt` file.
    * Uncomment the `default_expiration` in `app.yaml`
    * Change the `SECRET_KEY` in `settings.py` using Python's [`os.urandom` function](http://docs.python.org/library/os.html#os.urandom).
<pre><code>
    >>> import os
    >>> os.urandom(24)
    '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
</pre></code>


Useful Commands
---------------

### Setup

    git clone https://github.com/zachwill/flask-engine.git <your_app_name_here>

### Run

    dev_appserver.py .

If you're planning on using email functionality with the development server,
use the following command:

    dev_appserver.py --enable_sendmail .

### Deploy

    appcfg.py update .

### Test

Tests are written using GAE v1.4.3's `testbed` functionality. Currently, [there
is a known bug](http://goo.gl/tDQTz) for users without `PIL` installed.

    python test.py

### Remote Console

    python appengine_console.py <your_app_name_here>


Todo
----

* add more tests
* add pep8.py to libs
  * create PEP8 TestCase, too


License
-------

**Author**: Zach Williams

All of my code is released under [the Unlicense](http://unlicense.org/) (a.k.a.
Public Domain).
