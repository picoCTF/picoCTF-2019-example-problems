from flask import Flask, render_template, request, url_for, redirect, flash
app = Flask(__name__)
app.secret_key = 'random string'
flag_value = '{{flag}}'

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/flag")
def flag():
    ua = request.headers.get('User-Agent')
    if "googlebot" in ua or "Googlebot" in ua:
        flash("Googlebot!", "success")
        return render_template('flag.html', value=flag_value)
    else:
        flash("You're not google!\n" + ua, "danger")
        return render_template('index.html')

@app.route("/unimplemented")
def unimplemented():
    flash("This isn't implemented yet.", "danger")
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run()
