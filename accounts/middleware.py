from django.contrib.sessions.models import Session
from accounts.models import LoggedInUser
from django.contrib.auth.models import User

class OneSessionPerUserMiddleware:
    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated and not request.user.is_staff:
            session_key = request.session.session_key
            try:
                logged_in_user = request.user.logged_in_user
                stored_session_key = logged_in_user.session_key
                count = logged_in_user.count
                # stored_session_key exists so delete it if it's different
                if count <=3:
                    if stored_session_key != session_key:
                        count = count+1
                    logged_in_user.session_key = session_key
                    logged_in_user.count =count
                    logged_in_user.save()
                else:
                    user = User.objects.get(id = request.user.id)
                    logged_in_user.count = 0
                    logged_in_user.save()
                    user.is_active = False
                    user.save()

            except LoggedInUser.DoesNotExist:
                LoggedInUser.objects.create(user=request.user, session_key=session_key)




        response = self.get_response(request)

        # This is where you add any extra code to be executed for each request/response after
        # the view is called.
        # For this tutorial, we're not adding any code so we just return the response

        return response