def auth(request):
    if not request.user.is_authenticated():
        return {}
    return dict(
        webauth=dict(
            [(a.provider, a) for a in request.user.social_auth.all()]
        )
    )
