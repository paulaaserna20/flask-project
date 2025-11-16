from doctest import debug
from enum import nonmember

from flask import Flask, request, render_template
from flask import render_template
app= Flask (__name__)


@app.route('/')
def inicio():
 return render_template("inicio.html")

@app.route('/ejercicio1',methods=["GET", "POST"])
def ejercicio1():
    resultado= None
    error= None
    if request.method == 'POST':
        # Capturar datos del formulario
        try:
            n1 = float(request.form.get("Nota1", 0))
            n2 = float(request.form.get("Nota2", 0))
            n3 = float(request.form.get("Nota3", 0))
            asistencia = float(request.form.get("Asistencia", 0))
        except:
            return render_template("ejercicio1.html", resultado=resultado, error=error)

        # Validaciones
        if not (10 <= n1 <= 70): return render_template("ejercicio1.html")
        if not (10 <= n2 <= 70): return render_template("ejercicio1.html")
        if not (10 <= n3 <= 70): return render_template("ejercicio1.html")
        if not (0 <= asistencia <= 100): return render_template("ejercicio1.html")

        # Cálculo de promedio
        promedio = round((n1 + n2 + n3) / 3, 1)

        # Determinar aprobación
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"


        resultado = {
            "promedio": promedio,
            "estado": estado,
        }

    return render_template("ejercicio1.html", resultado=resultado)



@app.route('/ejercicio2', methods=["GET","POST" ])
def ejercicio2():
    resultado= None
    error= None



    if request.method == 'POST':
        # 1) Leer los datos del formulario
        n1 = request.form.get('Nombre1', '').strip()
        n2 = request.form.get('Nombre2', '').strip()
        n3 = request.form.get('Nombre3', '').strip()


        if not n1 or not n2 or not n3:
            error = "Debes ingresar los 3 nombres."
        elif len({n1, n2, n3}) < 3:
            error = "Los nombres deben ser diferentes."
        else:

            nombres = [n1, n2, n3]
            nombre_mas_largo = max(nombres, key=len)
            cantidad_caracteres = len(nombre_mas_largo)

            resultado = {
                "nombre": nombre_mas_largo,
                "cantidad": cantidad_caracteres
            }


    return render_template(
        "ejercicio2.html",
        resultado=resultado,
        error=error
    )


if __name__ == '__main__':
    app.run(debug=True)



