from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

def fb_sc_login_required(function=None,
                         redirect_field_name=REDIRECT_FIELD_NAME,
                         login_url=None):
    def user_connected_soundcloud_and_facebook(user):
        if not user.is_authenticated():
            return False

        if set(["facebook", "soundcloud"]) != \
           set([auth.provider for auth in user.social_auth.all()]):
            return False

        return True

    actual_decorator = user_passes_test(
        user_connected_soundcloud_and_facebook,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
