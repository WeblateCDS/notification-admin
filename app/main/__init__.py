from flask import Blueprint

main = Blueprint('main', __name__)  # noqa

from app.main.views import (  # noqa
    add_service,
    api_keys,
    choose_service,
    code_not_received,
    conversation,
    dashboard,
    email_branding,
    feedback,
    forgot_password,
    inbound_number,
    index,
    invites,
    jobs,
    letter_jobs,
    manage_users,
    new_password,
    notifications,
    organisations,
    platform_admin,
    providers,
    register,
    send,
    service_settings,
    sign_in,
    sign_out,
    styleguide,
    templates,
    two_factor,
    user_profile,
    verify
)
