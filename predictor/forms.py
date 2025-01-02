from django import forms

class ExpenseForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[('M', 'Male'), ('F', 'Female')])
    bmi = forms.FloatField(label='BMI')
    children = forms.IntegerField(label='Children')
    smoker = forms.ChoiceField(label='Smoker', choices=[('Y', 'Yes'), ('N', 'No')])