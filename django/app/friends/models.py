from django.db import models


class School(models.Model):
    name = models.CharField(max_length=50)


class Student(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(
        'School',
        on_delete=models.CASCADE
    )

    friend = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
    )

    def follow(self, students):
        if not self.from_students_relations.filter(to_students=students).exists():
            self.from_students_relations.create(
                to_students=students,
            )
        return self.from_user_relations.get(to_user=students)

    def __str__(self):
        return self.name


class Relation(models.Model):
    from_friend = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='from_students_relations',
        # related_query_name의 기본값
        # 기본값:
        #  이 모델 클래스명의 소문자화
        # related_name이 지정되어 있을 경우:
        #  related_name의 값
        related_query_name='from_students_relation',
    )
    to_user = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='to_students_relations',
        related_query_name='to_students_relation',
    )
