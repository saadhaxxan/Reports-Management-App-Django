from django import  forms

class SalesSearchForm(forms.Form):
    CHART_CHOICES = (
        ('#1','Bar Chart'),
        ('#2','Pie Chart'),
        ('#3','Line Chart')
    )
    date_from = forms.DateField(widget=forms.DateInput
    (attrs={
        'type':'date'
    }))
    date_to = forms.DateField(widget=forms.DateInput
    (attrs={
        'type':'date'
    }))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)