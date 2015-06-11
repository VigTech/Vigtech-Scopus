#!flask/bin/python
from flask import Flask, jsonify, request
from administradorConsultas import AdministradorConsultas

app = Flask(__name__)

    
@app.route('/consultaScopus/', methods=['GET'])
def get_taski():
	if request.method =='GET':
		consulta = request.args.get('consulta')
		proyecto = request.args.get('proyecto')
		limite = request.args.get('limite')
		user = request.args.get('user')
		ac = AdministradorConsultas()
		ac.descargar_papers(consulta, limite)
		ac.move_files(user,proyecto)
		ac.escribir_docs(user,proyecto)
		return jsonify({'titulos':ac.titulos_descargas})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
