from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def validate(self,post_data):
        errors={}
        for field,value in post_data.iteritems():
            if len(value)<1:
                errors[field]="{} field is required".format(field.replace('_',''))
            if field == "name":
                if not field in errors and len(value) < 5:
                    errors[field]="{} field must be at least 5 characters".format(field.replace('_',''))
            if field == "description":
                if not field in errors and len(value) < 15:
                    errors[field]="{} field must be at least 15 characters".format(field.replace('_',''))
            else:
                if len(self.filter(name=post_data['name']))> 1:
                    errors['name']= "Course already exist"
        return errors


class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)       # needs add
    update_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    def __repr__(self):
        return "id:: {} course:: {} desc:: {} ".format(self.first_name,self.last_name)