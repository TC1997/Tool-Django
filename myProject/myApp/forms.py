from django import forms
from .models import Squirrel


class SquirrelForm(forms.ModelForm):

    class Meta:
        model = Squirrel
        fields = '__all__'
        widgets = {
            'Longitude': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Latitude': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Unique_Squirrel_ID': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Highlight_Fur_Color': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Combination_of_Primary_and_Highlight_Color': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Color_Notes': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Location': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Above_Ground_Sighter_Measurement': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Specific_Location': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Other_Activities': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Other_Interactions': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            'Lat_Long': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
        }



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
        widgets = {
            'Longitude': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'Latitude': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'Unique_Squirrel_ID': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'Location': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'Specific_Location': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
            'Other_Activities': forms.Textarea(attrs={'rows': 1, 'cols': 70}),
        }

    def __init__(self, *args, **kwargs):
        super(SquirrelForm1, self).__init__(*args, **kwargs)
        self.fields['Date'].required = True

