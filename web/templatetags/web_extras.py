from django import template

register = template.Library()

def nice_duration(duration):
    """
    Converts duration (int) to a human readable duration
    like 2:35
    """
    total_seconds = duration / 1000
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)

    if h:
        return "%02d:%02d:%02d" % (h, m, s)
    return "%02d:%02d" % (m, s)



register.filter('nice_duration', nice_duration)
