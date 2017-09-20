from bottle import Bottle, template, route, run, static_file


@route('/')
def index():
	return template('template.tpl')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

if __name__ == "__main__":
	run(host="localhost", port=8080, debug='True', reloader='True')

