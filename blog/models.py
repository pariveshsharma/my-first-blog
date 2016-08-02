from django.db import models
from django.utils import timezone

class Post(models.Model):
	author= models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	Created_date = models.DateTimeField( default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title
	"""docstring for Post"models.Model) __init__(self, arg):
	author= models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.
		super(Post,models.Model)__init__()
		author= models.ForeignKey('auth.User')
		title = models.CharField(max_length=200)
		text = models.
		self.arg = arg
		

# Create your models here."""
