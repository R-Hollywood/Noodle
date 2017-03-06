from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django.db import models
	
class Admin(models.Model):
	#name, password, email, forename and surname attributes are included with django's 'User' model
	#in our case we should simply set the username to be the same as the email address
	#because django has a lot involved in the underlying framework
	user = models.OneToOneField(User, blank = False)
	
	def save(self, *args, **kwargs):
		user.is_superuser = True
		super(Category, self).save(*args, **kwargs)
	
	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name

class Staff(models.Model):
	#'inheritance'
	user = models.OneToOneField(User, blank = False)
	
	subject = models.CharField(max_length = 128)
	status = models.CharField(max_length = 128)
	
	#is this field actually necessary?
	#I don't think so, but I included it for the time being
	maintainedBy = models.ManyToManyField(Admin, related_name = 'maintenanceOf')

	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name

class Student(models.Model):
	#'inheritance'
	user = models.OneToOneField(User, blank = False)
	
	subject = models.CharField(max_length = 128)
	yearOfStudy = models.IntegerField(default = 1)
	
	enrolledIn = models.ManyToManyField(Course, related_name = 'students')
	maintainedBy = models.ManyToManyField(Admin, related_name = 'maintenanceOf')
	
	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name
	
class Course(models.Model):

	name = models.CharField(max_length = 128)
	courseID = models.CharField(max_length = 128, primary_key = True)
	#I'm assuming we're going to need different urls for each course page here
	slug = models.SlugField(unique=True)
	#I'm treating this as another object for ease of implementation
	#but as in the ER diagram it's practically just an attribute
	subject = models.ForeignKey(Subject)
	
	staffManagers = models.ManyToManyField(Staff, related_name = 'courses')
	maintainedBy = models.ManyToManyField(Admin, related_name = 'maintenanceOf')
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name
		
class Subject(models.Model):
	name = models.CharField(max_length = 128)
	
	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name

class Material(models.Model):

	name = models.CharField(max_length = 128)
	visibility = models.BooleanField()
	#I'm assuming we're going to need different urls for each piece of material here
	slug = models.SlugField(unique=True)
	
	accessedBy = models.ManyToManyField(Student, related_name = 'hasAccess')
	courseFrom = models.ForeignKey(Course, related_name = 'material')
	createdBy = models.ForeignKey(Staff, related_name = 'createdMaterial', blank = False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
		
	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name

class File(models.Model):
	#'inheritance'
	material = models.OneToOneField(Material, blank = False)
	
	#should there be some other attribute here to hold the contents of a file?

	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name

class Assessment(models.Model):
	#'inheritance'
	material = models.OneToOneField(Material, blank = False)
	
	deadline = models.DateTimeField()
	submissionDate = models.DateTimeField()

	def __str__(self): 
		return self.name
		
	def __unicode__(self): 
		return self.name