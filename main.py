from flask import Flask, request

app = Flask(__name__)

#la ruta a cual se nos dirige primeramente
@app.route('/')
def hello():

  #agregamos la ip del usuario
  user_ip = request.remote_addr
  
  return 'tu ip es {}'.format(user_ip)