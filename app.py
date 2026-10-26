# Starts the TrailTrack website and decides which page to show for each address
from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_home_page():
    return 'TrailTrack is running.'


if __name__ == '__main__':
    app.run(debug=True)
