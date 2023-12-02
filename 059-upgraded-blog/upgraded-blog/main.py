from flask import Flask, render_template
from post import Posts

app = Flask(__name__)

posts = Posts()


@app.route("/")
def home_endpoint():
    return render_template("index.html",
                           title="Fake Kpop'Blog",
                           subtitle="A Blog Theme by Start Bootstrap",
                           bg_image="static/assets/img/home-bg.jpg",
                           all_posts=posts.get_all())


@app.route("/post/<post_id>")
def post_endpoint(post_id):
    post = posts.get_by_id(post_id)
    return render_template("post.html",  post=post)


@app.route("/about")
def about_endpoint():
    return render_template("about.html",
                           title="About Me",
                           subtitle="This is what I do.",
                           bg_image="static/assets/img/about-bg.jpg")


@app.route("/contact")
def contact_endpoint():
    return render_template("contact.html",
                           title="Contact Me",
                           subtitle="Have questions? I have answers.",
                           bg_image="static/assets/img/contact-bg.jpg")


if __name__ == "__main__":
    app.run(debug=True)
