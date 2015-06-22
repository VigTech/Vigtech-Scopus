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
        ac.descargar_papers(consulta, int(limite), user, proyecto)
        ac.escribir_docs(user,proyecto)
        return jsonify({'titulos':ac.titulos_descargas, 'eids': ac.eids_descargas})

@app.route('/obtenerEid/', methods=['GET'])
def get_eids():
    if request.method =='GET':
        consulta = request.args.get('consulta')
        ac = AdministradorConsultas()
        eids = ac.obtener_eid(100, consulta)

        return jsonify({'eids':eids})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
