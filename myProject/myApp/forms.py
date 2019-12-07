from django import forms
from .models import Squirrel


class SquirrelForm(forms.ModelForm):

    class Meta:
        model = Squirrel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SquirrelForm, self).__init__(*args, **kwargs)
        self.fields['Date'].required = True


class SquirrelForm1(forms.ModelForm):

    class Meta:
        model = Squirrel
        fields = ('Latitude', 'Longitude', 'Unique_Squirrel_ID',
                  'Shift', 'Date', 'Age', 'Primary_Fur_Color',
                  'Location', 'Specific_Location', 'Running', 'Chasing',
                  'Climbing', 'Eating', 'Foraging', 'Other_Activities',
                  'Kuks', 'Quaas', 'Moans', 'Tail_Flags', 'Tail_Twitches',
                  'Approaches', 'Indifferent', 'Runs_From')

    def __init__(self, *args, **kwargs):
        super(SquirrelForm1, self).__init__(*args, **kwargs)
        self.fields['Date'].required = True
