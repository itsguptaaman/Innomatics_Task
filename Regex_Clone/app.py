from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    try:
        
        string_input = request.args.get("input_string")
        pattern_input = request.args.get("input_pattern")

        if (string_input != None) and (pattern_input != None):
            result = re.findall(pattern_input, string_input)
            if result == ['']:
                result = ''
            length = len(result)
        
        else:
            result = ''
            length = 0
        
        return render_template("home.html", result=result, length=length, string_input=string_input, pattern_input=pattern_input)
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)