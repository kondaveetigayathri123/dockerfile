# Create your models here.
# models are actually database ORM 
# technically a creating a class is creating a table on the database

from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateField('date published')
    body = models.TextField() #used to store large text data
    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    # It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        # It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
        return self.choice_text

    # can also have custom method for getting expected values from the database
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# the whole class we created looks like this here as a SQL Query
'''
BEGIN;
--
-- Create model Question
--
CREATE TABLE "sample_application_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "sample_application_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "sample_application_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "sample_application_choice_question_id_e79bb585" ON "sample_application_choice" ("question_id");
COMMIT;
'''