from django.db import models


class Desc(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__ (self):
        return f"<Desc object id#:{self.id} >"


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = 'Enter a course name of at least 6 characters'
        if len(postData['description']) < 16:
            errors['description'] = 'Enter a description greater than 15 characters'
        all_courses = Course.objects.all()
        for course in all_courses:
            if postData['name'] == course.name:
                errors['name'] = 'That course has already been entered!'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Desc, on_delete=models.CASCADE, primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments = a list of comments associated with a given course
    objects = CourseManager()   # replaces default value of objects = models.Manager() to custom version for validations

    def __repr__ (self):
        return f"<Course object: {self.name} | id#:{self.id} >"


class Comment(models.Model):
    name = models.CharField(max_length=255, default='none')
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__ (self):
        return f"<Comment object: {self.comment} | id#:{self.id} >"



# Create your models here.
