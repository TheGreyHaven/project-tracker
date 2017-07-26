"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html", first=first, last=last, github=github, grades=grades)
    return html

    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")



@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    # import pdb; pdb.set_trace()
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    github = request.form['github']
    hackbright.make_new_student(first_name, last_name, github)

    return render_template("success.html", first_name=first_name)



@app.route("/student-add-form")
def student_add_form():
    """add form"""

    return render_template("student_add_form.html")

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
