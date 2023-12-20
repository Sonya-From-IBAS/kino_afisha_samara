import os
import datetime

from flask import Flask, render_template, redirect, url_for, Response
from apscheduler.schedulers.background import BackgroundScheduler

from my_form import DateForm
from file_work import read_sessions_from_file, write_sessions_to_file


# initializing the application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


# rendering all movies on the selected date
@app.route("/films/<year>-<month>-<day>", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index(year: int = None, month: int = None, day: int = None) -> str | Response:
    if (not year and not month and not day):
        current_date = datetime.date.today()
        year = current_date.year
        month = current_date.month
        day = current_date.day

    if not os.path.isfile(os.path.join(os.path.join(os.getcwd(), 'sessions'), f'{year}-{month}-{day}.txt')):
        return render_template("wait.html")
    else:
        form = DateForm()
        if form.is_submitted():
            selected_date = form.date.data
            if selected_date:
                return redirect(url_for("index", year=selected_date.year, month=selected_date.month, day=selected_date.day))
        data = read_sessions_from_file(year, month, day)
        films = []
        sessions = []
        for i in data:
            if i["title"].lower() not in films:
                sessions.append(i)
                films.append(i["title"].lower())
        return render_template("index.html", sessions=sessions, form=form, year=year, month=month, day=day)


# rendering the selected movie
@app.route('/films/<year>-<month>-<day>/<name>')
def film(name: str, year: int, month: int, day: int) -> str:
    sessions = read_sessions_from_file(year, month, day)
    image = ""
    for i in sessions:
        if i["title"] == name:
            image = i["img"]
            genre = i["genre"]
            break
    return render_template("film.html", sessions=sessions, genre=genre, name=name,  image=image, len=len(sessions), year=year, month=month, day=day)


# Invalid URL
@app.errorhandler(404)
def page_not_found(e) -> str:
    return render_template('404.html'), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e) -> str:
    return render_template('500.html'), 500


if __name__ == '__main__':
    write_sessions_to_file()

    # scheduling constant content updates once an half hour
    scheduler = BackgroundScheduler()
    scheduler.add_job(write_sessions_to_file, 'interval', minutes=30)
    scheduler.start()

    # running the application
    app.run(debug=True, use_reloader=False)
