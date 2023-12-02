from flask import Flask, render_template, request
from post import Posts
from notification_manager import Message, NotificationManager

app = Flask(__name__)
posts = Posts()
notification_manager = NotificationManager()

@app.route("/")
def home_endpoint():
    all_posts = posts.get_all()
    return render_template(template_name_or_list="index.html",
                           title="Fake Kpop'Blog",
                           subtitle="A Blog Theme by Start Bootstrap",
                           bg_image="static/assets/img/home-bg.jpg",
                           all_posts=all_posts)


@app.route("/post/<post_id>")
def post_endpoint(post_id):
    post = posts.get_by_id(post_id)
    return render_template(template_name_or_list="post.html",  post=post)


@app.route("/about")
def about_endpoint():
    return render_template(template_name_or_list="about.html",
                           title="About Me",
                           subtitle="This is what I do.",
                           bg_image="static/assets/img/about-bg.jpg")


@app.route("/contact")
def contact_endpoint():
    return render_template(template_name_or_list="contact.html",
                           title="Contact Me",
                           subtitle="Have questions? I have answers.",
                           bg_image="static/assets/img/contact-bg.jpg")


@app.route("/form-entry", methods=["POST"])
def contact_form_entry():
    message = Message(data=request.form)
    notification_manager.send_email(message)
    return render_template(template_name_or_list="contact.html",
                           title="Successfully sent message",
                           subtitle="Have questions? I have answers.",
                           bg_image="static/assets/img/contact-bg.jpg")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
