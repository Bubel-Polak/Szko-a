from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class DropboxImageField(models.ImageField):
    def pre_save(self, model_instance, add):
        file = super(models.ImageField, self).pre_save(model_instance,add)
        if "dropboxusercontent" in file.name:
            return file
        file.name = self.storage.generate_url(file.name)
        return file

class teacher(models.Model):
	name = models.CharField(max_length=200)
	text = models.TextField()
	img = DropboxImageField(storage=dstorage)

         def publish(self):
        	self.save()

   	 def __str__(self):
        	return self.name
	
class Gallery(models.Model)
	title= models.CharField(max_length=200)
	img = DropboxImageField(storage=dstorage)

	
    	def publish(self):
        	self.save()

    	def __str__(self):
        	return self.name

class Absolvetns(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = DropboxImageField(storage=dstorage)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Patrons(models.Model):
   
    text = models.TextField()
    img = DropboxImageField(storage=dstorage)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
