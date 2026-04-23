from flask import Flask, render_template, request, jsonify, make_response, session

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/Usuarios')
def Usuarios():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005367_usr",
        password="Q4Q?ZfPc+k",
        database="u760464709_24005367_bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Usuarios")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))

@app.post('/Usuario')
def usuario():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005367_usr",
        password="Q4Q?ZfPc+k",
        database="u760464709_24005367_bd"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO Usuarios (correo, contrasena, nombre) VALUES (%s, %s, %s)"
    val = (request.form['txtNombre'], request.form['cboCategoria'], request.form['txtPrecio'], request.form['txtExistencias'])
    mycursor.execute(sql, val)
    mydb.commit()
    return "correcto"


