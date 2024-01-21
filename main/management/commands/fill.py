from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Петров', 'first_name': 'Петр'},
            {'last_name': 'Семенов', 'first_name': 'Семен'},
            {'last_name': 'Антонов', 'first_name': 'Антон'},
            {'last_name': 'Иванов', 'first_name': 'Иван'},
            {'last_name': 'Асянова', 'first_name': 'Ася'},
            {'last_name': 'Беляев', 'first_name': 'Леха'},
        ]

        # for student_item in student_list:
        #    Student.objects.create(**student_item)

        student_for_create = []
        for student_item in student_list:
            student_for_create.append(
                Student(**student_item)
            )

        Student.objects.bulk_create(student_for_create)
