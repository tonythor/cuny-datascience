from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def show_form():
    return main_page

@app.route("/calc", methods=["POST"])
def calculate():
    number = int(request.form['number'])
    result = number * 5
    return f"The result is {result}"

main_page = '''
<html>
    <head>
    <title>Multiplier</title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>
<!-- Form Name -->
<legend>Multiplier</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Number</label>  
  <div class="col-md-4">
  <input id="textinput" type="number" name='number' placeholder="Enter a number" class="form-control input-md" required>
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Calculate</button>
  </div>
</div>
</fieldset>
</form>
<script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)