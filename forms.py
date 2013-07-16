from django import forms

class LoginForm1(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'input-block-level', 'autocomplete':'OFF', 'placeholder':'Email Address'}))
    #password = forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={'class' : 'txt-box1', 'autocomplete':'OFF', 'placeholder':'Password'}), max_length=50)
    #recaptcha = forms.CharField(max_length = 50, required=False,widget=forms.TextInput(attrs={'class' : 'txt-box1', 'autocomplete':'OFF', 'placeholder':'Enter Above Number'}))

  
class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()

class UploadForm(forms.Form):
    file = forms.FileField() 
    description = forms.CharField ( widget=forms.widgets.Textarea() )
