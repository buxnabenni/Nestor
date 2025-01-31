from django.db import models
from company.models import Company
from common.models import ZipCode, Skills, JobCategory
from applicant.models import Applicant, Experience, Education, References
from django.utils import timezone
from django.contrib.auth.models import User


class JobType(models.Model):
    '''Class that contains a list of all type of jobs
    Types: summer/internship/part-time/fulltime'''
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)


class Job(models.Model):
    '''Class that contains all the data for all job offers'''
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    job_category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    job_image = models.CharField(max_length=9999, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    date_of_offering = models.DateField(default=timezone.now)
    application_due_date = models.DateField()
    starting_date = models.DateField()
    num_of_applicants = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name) + ", " + self.company.name


class Application(models.Model):
    '''Class that contains all application-specific applicant data'''
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    cover_letter = models.TextField(max_length=1000, blank=True, null=True)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.applicant.full_name) + ' - ' + str(self.job.name)


class FavoriteJob(models.Model):
    '''Class that connects a user to a job
    This connection means that the user has favorited that job'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.get_full_name()) + ' - ' + str(self.job.name)


class hasSkills(models.Model):
    '''Class that connects a user's application to a skill'''
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.application.applicant.full_name) + ' - ' + str(self.skill.name)


class hasExperience(models.Model):
    '''class that connects a user's application to an experience'''
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.application.applicant.full_name) + ' - ' + str(self.experience.workplace_name) + str(self.experience.role)


class hasEducation(models.Model):
    '''Class that connects a user's application to an education'''
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.application.applicant.full_name) + ' - ' + str(self.education.school_name) + str(self.education.degree)


class hasReferences(models.Model):
    '''class that connects a user's application to a reference'''
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    reference = models.ForeignKey(References, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.application.applicant.full_name) + ' - ' + str(self.reference.name)
