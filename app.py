# import dependencies
import os
from flask import Flask, jsonify
from cfenv import AppEnv
from urllib.parse import unquote

# bootstrap the app
app = Flask(__name__)

# our base route which just returns a string
@app.route('/')
def hello_world():
    return 'Congratulations! Welcome to the Tanzu Application Service'

@app.route("/info")
def env_info():
    dict_env = {k:v for k,v in os.environ.items()}
    return jsonify(dict_env)

def credhub_secret(key):
    '''
    Read the VCAP_SERVICES env variable & extract the "demo-certificate" value
    :return: parsed credhub value as a dict
    '''
    cf_env = AppEnv()
    credhub_env = cf_env.get_service(label="credhub").get_url(key)
    
    return credhub_env

@app.route("/env/<key>")
def credhub_info(key):
    return jsonify(credhub_secret(key))

                    
# start the app
if __name__ == '__main__':
    # set the port dynamically with a default of 3000 for local development
    port = int(os.getenv('PORT', '3000'))
    app.run(host='0.0.0.0', port=port)
