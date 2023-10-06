from django.db import models


class GradeLevel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    grade_level = models.IntegerField(unique=True)

    class Meta:
        db_table = 'grade_levels'

    def __str__(self):
        return self.name

class SkillManager(models.Manager):
    def get_by_natural_key(self, name):
        '''This allows the `manage.py loaddata/dumpdata` serializer to use this unique
        field as the reference rather than the unstable primary key value.'''
        return self.get(name=name)


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    difficulty = models.FloatField()
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.PROTECT)

    class Meta:
        db_table = 'skills'

    objects = SkillManager()

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=100)
    is_using_scheduling = models.BooleanField()

    class Meta:
        db_table = 'schools'

    def __str__(self):
        return self.name
