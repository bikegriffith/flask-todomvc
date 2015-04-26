# Flask TodoMVC

[![Build Status](https://secure.travis-ci.org/bikegriffith/flask-todomvc.png)](http://travis-ci.org/bikegriffith/flask-todomvc)

## Overview

This project is a fork from [kevinbeaty/flask-todomvc][1] based on his well written [tutorial][2] using Flask/SQLAlchemy/BackboneJS.

It establishes a few different patterns and adds features I think are important in a web app that will grow to moderate complexity.

1. JS/CSS minification (DONE)
2. Database migrations (NOT DONE)
3. Admin portal (HALF DONE)
4. Separation of config for dev/test/stage/prod (NOT DONE)

## Getting Started

1. Clone repo
2. Create a virtual environment and install requirements `virtualenv . && . bin/activate && pip install -r requirements.txt && npm install`
3. Run tests `pip install nose && nosetests`
4. Run dev server `gulp`
5. Log in using `me@example.com` : `password`

[1]: https://github.com/kevinbeaty/flask-todomvc
[2]: http://simplectic.com/blog/2014/flask-todomvc-part1/
