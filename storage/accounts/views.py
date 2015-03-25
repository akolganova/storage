from registration.backends.simple.views import RegistrationView


class RegisterView(RegistrationView):
    def get_success_url(self, request, user):
        return '/'
