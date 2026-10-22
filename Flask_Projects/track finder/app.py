from flask import Flask, render_template
print(__name__)
app = Flask(__name__)
site_name = "Track Finder"
tracks = [
    {"name":"Mount Eden Loop", "length":2.0, "grade":"Easy", "image":"images/mount_eden_loop.jpg"},
    {"name":"Coast to Coast Walkway", "length":16.0,"grade": "Medium", "image":"images/caost_to_coast_walkway.jpg"},
    {"name":"Karekare Falls", "length":3.5, "grade":"Easy", "image":"images/karekare_falls.jpg"},
    {"name":"Hillar Trail", "length":70.0, "grade":"Hard", "image":"images/hillar_trail.jpg"},
    {"name":"Man", "length":30.0, "grade":"Impossible", "image":"images/logo.jpg"}
]

@app.route("/")
def home():
    return render_template("home.html", site_name=site_name, count=len((tracks)))

@app.route("/tracks")
def tracks_page():
    return render_template("tracks.html", site_name=site_name, tracks=tracks)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ =="__main__":
    app.run(debug=True)