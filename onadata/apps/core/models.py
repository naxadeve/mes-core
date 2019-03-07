from django.db import models


class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	sector = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	reporting_period = models.IntegerField(choices=((1,"Monthly"),(2, "Bi-annually"), (3, "Quaterly")))
	beneficiaries = models.BooleanField(default=True)

	def __str__(self):
		return self.name

# class Output(models.Model):
# 	name = models.CharField(max_length=200)
# 	description = models.CharField(max_length=500)
#   PID = models.IntegerField('Project Id')

# 	def __str__(self):
# 		return self.name


# class Group(models.Model):
# 	name = models.CharField(max_length=200)

# 	description = models.CharField(max_length=500)


# class Activity(models.Model):
# 	name = models.CharField(max_length=200)
# 	description = models.CharField(max_length=500)

# 	AG_Id = models(IntegerField, 'Activity Group ID')
# 	target_number = models.IntegerField()
# 	target_unit = models.CharField(max_length=200)

# 	start_date = models.DateTimeField()
# 	end_date = models.DateTimeField()

# 	form_id = models.IntegerField()

# 	target_complete = models.BooleanField(default=True)
# 	beneficiary_level = models.BooleanField(default=True)

# 	published = models.BooleanField(default=True)
# 	target_met = models.BooleanField(default=True)