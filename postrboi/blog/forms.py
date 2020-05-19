from django import forms
from blog.models import Tag , UserProfile , Post



class PostForm(forms.ModelForm) : 


    tag_1 = forms.CharField(max_length=8)
    tag_2 = forms.CharField(max_length=8)
    tag_3 = forms.CharField(max_length=8)
    tag_4 = forms.CharField(max_length=8)

    content = forms.CharField(widget = forms.Textarea , max_length=256)

    article_hyperlink = forms.URLField(max_length=256)
    image_hyperlink = forms.URLField(max_length=256)

    action = forms.CharField(max_length = 10 ,  initial='post')

    def clean(self) : 
        
        

        cleaned_data = super(PostForm , self).clean()

        print('cleaned_data before processing : ')
        print(cleaned_data)

        print('any(self.errors) : ')
        print(any(self.errors))
        
        cleaned_data['tag_1'] = Tag.objects.get(tag_name = cleaned_data.get('tag_1' , ''))
        cleaned_data['tag_2'] = Tag.objects.get(tag_name = cleaned_data.get('tag_2' , ''))
        cleaned_data['tag_3'] = Tag.objects.get(tag_name = cleaned_data.get('tag_3' , ''))
        cleaned_data['tag_4'] = Tag.objects.get(tag_name = cleaned_data.get('tag_4' , ''))

        print('cleaned_data AFTER processing : ')
        print(cleaned_data)

        return cleaned_data
    

    class Meta : 

        model = Post
        fields = ['content' , 'article_hyperlink' , 'image_hyperlink' , 'tag_1' , 'tag_2' , 'tag_3' , 'tag_4' , 'action']

    
class TagForm(forms.ModelForm) : 

    tag_name = forms.CharField(max_length=8 ) 

    action = forms.CharField(max_length = 10 , widget=forms.HiddenInput() , initial='tag')

    class Meta : 

        model = Tag
        fields = ['tag_name']