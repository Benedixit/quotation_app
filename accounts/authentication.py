from django.contrib.auth import get_user_model


class EmailOrUsernameModelBackend(object):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        try:
            # Check if the input is an email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # If the input is not an email, try to get the user by username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None