import soundcloud


def soundcloud_client_for_user(user):
    return soundcloud.Client(
        access_token=user.social_auth.all()[0].access_token)
