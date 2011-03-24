gae-flask-html5
===============

<pre><code>

         DD
        EiGL                                             jjjjjjjjjjjjjjjjj 
        DttG                      E                      fffffffffffffffff 
        DtjLD                      K                     fffffffffjjjjjjjf 
        GjjfG; EDL,tD             #KW#                   fffffffffjjjjjjjf 
        GjffLD:.::::::G          #L#jK:K                 fff......     jjf 
        GfLL::.::ffjt::j        D.t. fW                  fff......     jff 
        GLi::..:;i;tii:j        jW##  G                  tff...fffjjjjjjff 
        L::::.:i,;,iii,:;        ##W#                    :ff,..fffjjjjjjff 
       D:::::.:i:,.iiii:D        ##f                      fff.....     jfL 
      ::::::::.fLL;,iii:E        ###i j;                  fff.....     jfj 
      E::::::..LLf:iiii:L         ##;  ,                  ffffffffjj  ,jf: 
      E,;tjL::.LLf,,tii:E         ;### .                  fff..fffjj  tjf  
    EDitfL;G:::LG;,.iii:D:         ##W; :                 fff..fffjj  jjf  
 ;DLfti;GGGG:::t:,,;ii::LLL        D#W#  K                fff...,f;   jjf  
 jitiLLGDE;:::::ii.iii:GGGD         W##i# W               fff.....    jjf  
 EDjLDE E;;::::::iii;::fL.           W###f  L  #          ffffff.. jjjjjf  
         D::::::::::::f                jW##;# # ##L       ffffffffjjjjjff  
          fDt::::::;D                    ff;Lf##f         tfffffffjjfffff  
              iDDL                                           jfffffffL     
                                                                 j         


                      github.com/zachwill/gae-flask-html5

</code></pre>


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
`QUnit` for JavaScript tests and a `test` directory for Python's `unittest`.
Also, I included a `style.less` file since I primarily only use the
[Less app](http://incident57.com/less/) when writing stylesheets nowadays.


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
[another project skeleton](https://github.com/franciscosouza/labs).

Lastly, as an added bonus, the scripts are PEP8 compliant.


How do I use it?
----------------

Make sure you have the [Google App Engine SDK](http://appengine.google.com/)
installed on your computer, and you've created an application for your
Google account.

### Setup

    git clone https://github.com/zachwill/gae-flask-html5.git <your_app_name_here>

### Run

    dev_appserver.py .

### Deploy

    appcfg.py update .

### Test

Run your application with the `dev_appserver.py .` command, and then point
your browser to `http://localhost:<YOUR-PORT-NUMBER>/test`

### Remote Console

    python appengine_console.py .


Todo
----

* add more tests to `tests.py`
* add pep8.py to libs
  * create PEP8 TestCase, too
