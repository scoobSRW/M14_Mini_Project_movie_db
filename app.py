from flask import Flask
from flask_graphql import GraphQLView
from models import db
from schemas import schema
from confidential import password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/movie_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)