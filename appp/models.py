import random

from django.db import models


class Users(models.Model):
    tg_id = models.BigIntegerField()
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    daily_score = models.IntegerField()


def create_new_ref_number():
    return str(random.randint(10000, 99999))


class Category(models.Model):
    call_back = models.CharField(max_length=10, blank=True,
                                 unique=True, default=create_new_ref_number)
    nomi = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi


class Quetions(models.Model):
    category = models.ForeignKey(Category, related_name='all_category', on_delete=models.CASCADE)
    savol = models.CharField(max_length=255)
    manbaa = models.CharField(max_length=255)
    javob_1 = models.CharField(max_length=55)
    javob_2 = models.CharField(max_length=55)
    javob_3 = models.CharField(max_length=55, null=True, blank=True)
    javob_4 = models.CharField(max_length=55, null=True, blank=True)
    FRESHMAN = '1'
    SOPHOMORE = '2'
    JUNIOR = '3'
    SENIOR = '4'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, '1'),
        (SOPHOMORE, '2'),
        (JUNIOR, '3'),
        (SENIOR, '4'),
    ]
    javobi = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    photo = models.CharField(verbose_name="Rasm file_id", max_length=300, null=True)

    def __str__(self):
        return self.savol
