from flask import Flask, render_template, request

from smartpassgen import generator


app = Flask(__name__)


@app.route('/api/gen')
def api_generate():
    res = ''
    num = int(request.args['num']) if 'num' in request.args else 12
    sylls = int(request.args['sylls']) if 'sylls' in request.args else 4

    for _ in range(num):
        res += str(generator.create_pass(sylls, 'caps' in request.args, 'nums' in request.args,
                                         'symbs' in request.args)) + '<br>'
    return res


@app.route('/gen')
def generate():
    res = '<a href="/">Back</a><hr>'
    num = int(request.args['num']) if 'num' in request.args else 12
    sylls = int(request.args['sylls']) if 'sylls' in request.args else 4

    for _ in range(num):
        res += str(generator.create_pass(sylls, 'caps' in request.args, 'nums' in request.args,
                                         'symbs' in request.args)) + '<br>'
    return res


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()