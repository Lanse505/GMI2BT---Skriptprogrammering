from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/register", methods=['POST'])
def register():
  print(request.form.values)
  print(request.form.get('payment', 'Not Set'))
  return 'The /register app.route works!'

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=1337)