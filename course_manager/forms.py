from django import forms
from multiselectfield import MultiSelectField
from datetime import timedelta

SUBJECT_CHOICES = [
    ('STEM', 'STEM'),
    ('Business', 'Business'),
    ('Arts', 'Arts'),
    ('Politics', 'Politics'),
    ('Other', 'Other'),
    ]



class NewCourseForm(forms.Form):
    DAYS_OF_WEEK_CHOICES = (
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
)


    title = forms.CharField(label="Course Title:", max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Ex. History of Magic 101'}))
    professor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex. Severus Snape'}))
    description = forms.CharField(label="Description:", widget=forms.Textarea(attrs={"rows":10, "cols":80, 'placeholder': 'Ex. History of Magic is a core class and subject taught at Hogwarts School of Witchcraft and Wizardry. This class is a study of magical history.[1] This is one of the subjects where the use of magic practically is not necessary. History of Magic is taught from the first year to the fifth, and is completed with an O.W.L. exam with only a written section'}))
    subject = forms.CharField(label="Subject",max_length=100, widget=forms.Select(choices=SUBJECT_CHOICES))
    day = forms.MultipleChoiceField(label="Day(s):", choices=DAYS_OF_WEEK_CHOICES)
    start_time = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': 'Ex. 14:40'}))
    end_time = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': 'Ex. 15:40'}))

    def __init__(self, *args, **kwargs):
        super(NewCourseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    def clean_title(self):
        return self.cleaned_data['title'].capitalize()
