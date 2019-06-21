
from django import forms
from runaway.models import UserProfile
 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','name', 'bio', 'residence') 

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile