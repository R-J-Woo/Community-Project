from django.shortcuts import redirect


def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:  # user값이 None이거나 비어있으면
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap
