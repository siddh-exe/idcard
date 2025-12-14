from django import forms
from .models import Department
from django.contrib.auth import get_user_model

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name']
        widgets = {
            'dept_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter department name'
            })
        }

# your_app/forms.py

User = get_user_model()

class AdminCreateForm(forms.ModelForm):
    # We define the password field here to ensure it's a password input
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a strong password'})
    )

    class Meta:
        model = User
        fields = ['email', 'password']
        # You can also add widgets here, but the __init__ method is more flexible
        # widgets = {
        #     'email': forms.EmailInput(attrs={'placeholder': 'e.g., admin@example.com'})
        # }

    def __init__(self, *args, **kwargs):
        """
        This method is called when the form is instantiated.
        We use it to add CSS classes and other attributes to our fields.
        """
        super(AdminCreateForm, self).__init__(*args, **kwargs)

        # Add a class and placeholder to the email field
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',  # This is the class our CSS will target
            'placeholder': 'e.g., admin@example.com',
            'autofocus': True # Optional: automatically focus on this field when the page loads
        })

        # The password field already has a placeholder, but we can add the class here too
        self.fields['password'].widget.attrs.update({
            'class': 'form-input' # This is the class our CSS will target
        })

    def save(self, commit=True):
        """
        Override the default save method to handle password hashing and
        setting staff/superuser status.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
