from flask import Flask, render_template, url_for, request, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from data import db_session, users, jobs, jobs_api
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from forms.add_work import AddJobForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ghjmvghjmnvghjmvnfgc'

login_manager = LoginManager()
login_manager.init_app(app)
params = {}


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def work_log():
    global params
    params["logo_image_url"] = url_for('static', filename='img/logo.jpg')
    db_sess = db_session.create_session()

    # output = []
    # for job in db_sess.query(jobs.Jobs):
    #     output.append([job.id, job.topic, db_sess.query(users.User).filter(users.User.id == job.team_leader)[0].name +
    #                    ' ' + db_sess.query(users.User).filter(users.User.id == job.team_leader)[0].surname,
    #                    str(job.work_size) + ' hours', job.collaborators,
    #                    job.is_finished, job.user])
    # params['table_data'] = output
    return render_template('base.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(users.User).filter(users.User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form, **params)
    return render_template('login.html', title='Авторизация', form=form, **params)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        if db_sess.query(users.User).filter(users.User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = users.User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            klasse=form.klasse.data,
            position=form.position.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', form=form, **params)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_work', methods=['GET', 'POST'])
def add_work():
    form = AddJobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = jobs.Jobs(
            topic=form.topic.data,
            project=form.project.data,
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect("/")
    return render_template('add_work.html', title='Добавление работы', form=form, **params)


@app.route('/job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = AddJobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(jobs.Jobs).filter(jobs.Jobs.id == id,
                                              ((jobs.Jobs.user == current_user) | (current_user.position == 'captain'))
                                              ).first()
        if job:
            form.topic.data = job.topic
            form.project.data = job.project
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(jobs.Jobs).filter(jobs.Jobs.id == id,
                                              ((jobs.Jobs.user == current_user) | (current_user.position == 'captain'))
                                              ).first()
        if job:
            job.topic = form.topic.data
            job.project = form.project.data
            db_sess.commit()
            return redirect("/")
        else:
            abort(404)

    return render_template('add_work.html', title='Редактирование работы', form=form, **params)


@app.route('/job_delete/<int:id>')
@login_required
def job_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(jobs.Jobs).filter(jobs.Jobs.id == id,
                                          ((jobs.Jobs.user == current_user) | (current_user.position == 'checker'))
                                          ).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(users.User).get(user_id)


def main():
    db_session.global_init('db/projects.db')
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
