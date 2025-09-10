from flask import Flask, request, jsonify

app = Flask(__name__)




# 1) GET / -> mensaje
@app.get("/")
def root_get():
    return jsonify(message="Prueba de GET /)!"), 200




@app.post("/")
def root_post():
    if not request.is_json:
        return jsonify(error="El mensaje debe ser en formato JSON"), 415
    data = request.get_json(silent=True) or {}
    mensaje = data.get("mensaje")
    if not mensaje:
        return jsonify(error="No se ingreso ningun msj en el JSON"), 400
    return jsonify(respuesta=f"{mensaje}"), 200





@app.get("/color_favorito/<color>")
def color_favorito(color: str):
    return jsonify(message=f"Tu color favorito es: {color}"), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)  # http://127.0.0.1:5000
