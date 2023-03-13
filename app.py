# Esse código serve ao propósito demonstrar como se daria a conexão com o Database da calculadora Minerva
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    nm_job = request.form['nm_job']
    qt_ganho_mensal = int(request.form['qt_ganho_mensal'])
    qt_dias_trabalho_semana = int(request.form['qt_dias_trabalho_semana'])
    qt_hora_prevista_dia = int(request.form['qt_hora_prevista_dia'])
    qt_estimativa_total = int(request.form['qt_estimativa_total'])
    qt_valor_hora = int(request.form['qt_valor_hora'])
    qt_valor_projeto = int(request.form['qt_valor_projeto'])

    con = psycopg2.connect(host="exemplo",
                           database="calculadora_minerva",
                           user="exemplo",
                           password="exemplo")
    cur = con.cursor()

    cur.execute("""
        UPDATE calculo_estimativa
        SET qt_ganho_mensal = %s,
            qt_dias_trabalho_semana = %s,
            qt_hora_prevista_dia = %s,
            qt_estimativa_total = %s,
            qt_valor_hora = %s,
            qt_valor_projeto = %s
        WHERE nm_job = %s;
    """, (qt_ganho_mensal, qt_dias_trabalho_semana, qt_hora_prevista_dia, qt_estimativa_total, qt_valor_hora, qt_valor_projeto, nm_job, job))

    con.commit()
    con.close()

    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)