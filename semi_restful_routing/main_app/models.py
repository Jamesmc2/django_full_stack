from django.db import models

class ShowManager(models.Manager):
    def basic_validator_create(self, postData):
        errors={}
        if len(Show.objects.filter(title = postData['title'])) > 0:
            errors['title'] = 'Title already exists in database'
        elif len(postData['title']) <2:
            errors['title'] = 'Show title should be at least 2 characters long'
        if len(postData['network']) <3:
            errors['network'] = 'Show network should be at least 3 characters long' 
        if len(postData['description']) <10 and len(postData['description']) != 0:
            errors['description'] = 'Show description should be at least 10 characters long if given'      
        return errors     
    def basic_validator_edit(self, postData):
        errors={}
        if len(postData['title']) <2:
            errors['title'] = 'Show title should be at least 2 characters long'
        if len(postData['network']) <3:
            errors['network'] = 'Show network should be at least 3 characters long' 
        if len(postData['description']) <10 and len(postData['description']) != 0:
            errors['description'] = 'Show description should be at least 10 characters long if given'      
        return errors     

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

