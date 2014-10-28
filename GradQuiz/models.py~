# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Chapters(models.Model):
    chapters_title = models.CharField(max_length=100L)
    chapters_textisbn = models.ForeignKey('Textbook', db_column='chapters_textisbn')
    chapters_parenttitle = models.ForeignKey('Chapters', null=True, db_column='chapters_parenttitle', blank=True)
    class Meta:
        db_table = 'chapters'

class Correctanswer(models.Model):
    correctanswer_qid = models.ForeignKey('Questionbank', db_column='correctanswer_qid')
    correctanswer_explanation = models.CharField(max_length=100L, blank=True)
    correctanswer_text = models.CharField(max_length=100L)
    correctanswer_gid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'correctanswer'

class Course(models.Model):
    course_id = models.CharField(max_length=45L, primary_key=True)
    course_name = models.CharField(max_length=45L, blank=True)
    course_maxenroll = models.IntegerField(null=True, blank=True)
    course_numenrolled = models.IntegerField(null=True, blank=True)
    course_level = models.CharField(max_length=45L, blank=True)
    course_token = models.CharField(max_length=45L, blank=True)
    course_startdate = models.DateField(null=True, blank=True)
    course_enddate = models.DateField(null=True, blank=True)
    course_professor = models.ForeignKey('Professor', null=True, db_column='course_professor', blank=True)
    class Meta:
        db_table = 'course'

class CourseChapters(models.Model):
    course_chapters_title = models.ForeignKey(Chapters, db_column='course_chapters_title')
    course_chapters_cid = models.ForeignKey(Course, db_column='course_chapters_cid')
    class Meta:
        db_table = 'course_chapters'

class CourseStudent(models.Model):
    course_student_cid = models.ForeignKey(Course, db_column='course_student_cid')
    course_student_uid = models.ForeignKey('Student', db_column='course_student_uid')
    class Meta:
        db_table = 'course_student'

class CourseTa(models.Model):
    course_ta_uid = models.ForeignKey('Student', db_column='course_ta_uid')
    course_ta_cid = models.ForeignKey(Course, db_column='course_ta_cid')
    class Meta:
        db_table = 'course_ta'

class CourseTextbook(models.Model):
    course_textbook_isbn = models.ForeignKey('Textbook', db_column='course_textbook_isbn')
    course_textbook_cid = models.ForeignKey(Course, db_column='course_textbook_cid')
    class Meta:
        db_table = 'course_textbook'

class Homework(models.Model):
    homework_id = models.CharField(max_length=45L, primary_key=True)
    homework_startdate = models.DateField(null=True, blank=True)
    homework_enddate = models.DateField(null=True, blank=True)
    homework_numretries = models.IntegerField(null=True, blank=True)
    homework_mindifficulty = models.IntegerField(null=True, blank=True)
    homework_maxdifficulty = models.IntegerField(null=True, blank=True)
    homework_correctanswerpts = models.IntegerField(null=True, blank=True)
    homework_wronganswerpts = models.IntegerField(null=True, blank=True)
    homework_cid = models.ForeignKey(Course, null=True, db_column='homework_cid', blank=True)
    class Meta:
        db_table = 'homework'

class HomeworkChapters(models.Model):
    homework_chapters_hid = models.ForeignKey(Homework, db_column='homework_chapters_hid')
    homework_chapters_title = models.ForeignKey(Chapters, db_column='homework_chapters_title')
    class Meta:
        db_table = 'homework_chapters'

class HomeworkStudentMarks(models.Model):
    homework_student_marks_hid = models.ForeignKey(Homework, db_column='homework_student_marks_hid')
    homework_student_marks_uid = models.ForeignKey('Student', db_column='homework_student_marks_uid')
    homework_student_marks_attemptnum = models.IntegerField()
    homework_student_marks_marks = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'homework_student_marks'

class Paramquestions(models.Model):
    paramquestions_qid = models.ForeignKey('Questionbank', db_column='paramquestions_qid')
    paramquestions_gid = models.IntegerField()
    paramquestions_number = models.IntegerField()
    paramquestions_value = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'paramquestions'

class Professor(models.Model):
    professor_uid = models.CharField(max_length=45L, primary_key=True)
    professor_password = models.CharField(max_length=45L, blank=True)
    professor_name = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'professor'

class Questionbank(models.Model):
    questionbank_qid = models.IntegerField(primary_key=True)
    questionbank_text = models.CharField(max_length=100L, blank=True)
    questionbank_level = models.IntegerField(null=True, blank=True)
    questionbank_hint = models.CharField(max_length=100L, blank=True)
    questionbank_explanation = models.CharField(max_length=100L, blank=True)
    questionbank_type = models.CharField(max_length=45L, blank=True)
    questionbank_topic = models.ForeignKey(Chapters, null=True, db_column='questionbank_topic', blank=True)
    class Meta:
        db_table = 'questionbank'

class QuestionbankHomework(models.Model):
    questionbank_homework_qid = models.ForeignKey(Questionbank, db_column='questionbank_homework_qid')
    questionbank_homework_hwid = models.ForeignKey(Homework, db_column='questionbank_homework_hwid')
    class Meta:
        db_table = 'questionbank_homework'

class Student(models.Model):
    student_uid = models.CharField(max_length=45L, primary_key=True)
    student_password = models.CharField(max_length=45L, blank=True)
    student_level = models.CharField(max_length=45L, blank=True)
    student_name = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'student'

class Textbook(models.Model):
    textbook_isbn = models.CharField(max_length=45L, primary_key=True)
    textbook_title = models.CharField(max_length=45L, blank=True)
    textbook_author = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'textbook'

class Wronganswer(models.Model):
    wronganswer_qid = models.ForeignKey(Questionbank, db_column='wronganswer_qid')
    wronganswer_text = models.CharField(max_length=45L)
    wronganswer_explanation = models.CharField(max_length=45L, blank=True)
    wronganswer_gid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'wronganswer'

