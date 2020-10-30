# CF Sample App Python

A sample [Flask](http://flask.pocoo.org/) application to deploy to Cloud Foundry which works out of the box.

## Run locally

1. Run `python3 -m venv penv`
1. Run `source penv/bin/activate` on Mac OS X/Linux
1. Run `pip install -r requirements.txt`
1. Run `python app.py`
1. Visit [http://localhost:3000](http://localhost:3000)

## Run in the cloud

1. Run `pip download -r requirements.txt --no-binary=:none: -d vendor`
1. Run `cf push`
1. Visit the given URL
