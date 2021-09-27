import os

import dash
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required, LoginManager
import dash_bootstrap_components as dbc

def create_app():
    server = Flask(__name__)
    server.secret_key = os.environ.get("FLASK_SECRET_KEY", "")

    from app.dashboard.layout import layout as layout1
    from app.dashchat.layout import layout as layout2

    from app.dashboard.callbacks import register_callbacks as register_callbacks1
    from app.dashchat.callbacks import register_callbacks as register_callbacks2

    register_dashapp(server, 'Dashboard', 'dashboard', layout1, register_callbacks1,True)  # Create admin dashboard
    register_dashapp(server, 'Chat', 'chat', layout2, register_callbacks2,False)  # Create chat page

    register_extensions(server)
    register_blueprints(server)

    return server


# def register_dashapps(app):
#     from app.dashapp1.layout import layout
#     from app.dashapp1.callbacks import register_callbacks
#
#     # Meta tags for viewport responsiveness
#     meta_viewport = {
#         "name": "viewport",
#         "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}
#
#     dashapp1 = dash.Dash(__name__,
#                          server=app,
#                          url_base_pathname='/dashboard/',
#                          assets_folder=get_root_path(__name__) + '/dashboard/assets/',
#                          meta_tags=[meta_viewport])
#
#     with app.app_context():
#         dashapp1.title = 'Dashapp 1'
#         dashapp1.layout = layout
#         register_callbacks(dashapp1)
#
#     _protect_dashviews(dashapp1)


def register_dashapp(app, title, base_pathname, layout, register_callbacks_fun,is_protected):
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    my_dashapp = dash.Dash(__name__,
                           server=app,
                           external_stylesheets=[dbc.themes.BOOTSTRAP],
                           url_base_pathname=f'/{base_pathname}/',
                           assets_folder=get_root_path(__name__) + f'/{base_pathname}/assets/',
                           meta_tags=[meta_viewport])

    with app.app_context():
        my_dashapp.title = title
        my_dashapp.layout = layout
        register_callbacks_fun(my_dashapp)

    if is_protected:
        _protect_dashviews(my_dashapp)


def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(
                dashapp.server.view_functions[view_func])


def register_extensions(server):
    from app.extensions import login
    login.init_app(server)
    login.login_view = 'main.login'


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp)
