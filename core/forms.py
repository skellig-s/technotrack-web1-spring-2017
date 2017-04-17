from django import forms
from .models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class RegistrationForm(UserCreationForm):

    username = forms.CharField(required=True)
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'avatar')

    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if not user.avatar:
            user.avatar = "/avatars/default.jpg"

        if commit:
            user.save()
        return user


