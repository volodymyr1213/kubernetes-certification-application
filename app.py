from flask import Flask, jsonify
import argparse

## Testing application for kubernetes or docker hosting
## Very useful when you testing loadbalancer

parser = argparse.ArgumentParser(description="Small application to print name of the applcation.")
optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')


required.add_argument('-d', '--depends', help='Depends application.', required=True)
required.add_argument('-Q', '--Quite', help='Quite mode.',  action="store_true", required=True)
args = parser.parse_args()


app = Flask(__name__)
@app.route('/depends', methods=['GET'])
def depends():
    data = {'depends': args.depends, 'message': 'The applcation is up.'}
    return jsonify(data), 200


@app.route('/', methods=['GET'])
def index():
    data = {'name': 'Testing application'}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
