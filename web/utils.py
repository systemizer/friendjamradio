import soundcloud
from requests.exceptions import HTTPError
from social.apps.django_app.utils import load_strategy

class DjangoSoundcloudClient(soundcloud.Client):
    """
    Simple Wrapper Around Soundcloud Client that will
    refresh the access token if it receives a 401
    """

    def __init__(self, django_user, *args, **kwargs):
        self.django_user = django_user
        super(DjangoSoundcloudClient, self).__init__(
            access_token = django_user.social_auth.get().access_token,
            *args, **kwargs)

    def __getattr__(self, name, **kwargs):
        """Translate an HTTP verb into a request method."""
        try:
            return super(DjangoSoundcloudClient, self).__getattr__(name,
                                                                   **kwargs)
        except HTTPError:
            strategy = load_strategy()
            django_user.social_auth.get().refresh_token(strategy)
        finally:
            return super(DjangoSoundcloudClient, self).__getattr__(name,
                                                                   **kwargs)
