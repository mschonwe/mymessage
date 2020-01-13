
# A very simple Flask app to show pattern images based on text input

from flask import Flask, request
from processing import do_generate

app = Flask(__name__)
#app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def pattern_page():
    errors = ""
    if request.method == "POST":
        message = None
        try:
            message = str(request.form["message"])
        except:
            errors += "<p>{!r} not a valid string.</p>\n".format(request.form["message"])
        if message is not None:
                result = do_generate(message)
                return '''
                    <html>
                        <head>
                            <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.1/build/pure-min.css" integrity="sha384-oAOxQR6DkCoMliIh8yFnu25d7Eq/PHS21PClpwjOTeU2jRSq11vu66rf90/cZr47" crossorigin="anonymous">
                            <link rel="stylesheet" href="styles.css">
                        </head>
                        <body>
                            <div class="pure-g">
                                <div class="pure-u-1" style="margin: 25px;">
                                    <p>Here is the pattern image for: <b>{result}</b></p>
                                    <p><a href="/">Click here to try again</a></p>
                                </div>
                                <div class="pure-u-1" style="margin: 25px;">
                                    <p><img src="/static/images/{result}_plot.png" alt="{result}"></p>
                                    <p><img src="/static/images/{result}_plot4x4.png" alt="{result}2" style=clip_img></p>
                                </div>
                            </div>
                        </body>
                    </html>
                '''.format(result=result)
    return '''
        <html>
            <head>
                <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.1/build/pure-min.css" integrity="sha384-oAOxQR6DkCoMliIh8yFnu25d7Eq/PHS21PClpwjOTeU2jRSq11vu66rf90/cZr47" crossorigin="anonymous">
                <link rel="stylesheet" href="styles.css">
            </head>
            <body>
                <div class="pure-g" style="margin: 25px;">
                    {errors}
                    <div class="pure-u-1"><p>Enter your message string (short strings work best):</p></div>
                    <form method="post" action="." class="pure-form">
                        <p><input name="message" /></p>
                        <p><input type="submit" value="Generate Patterns" /></p>
                    </form>
                </div>
            </body>
        </html>
    '''.format(errors=errors)
