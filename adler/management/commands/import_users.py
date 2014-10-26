from django.core.management.base import CommandError, BaseCommand
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from personal.models import UserProfile
import os.path
import json
import uuid


class Command(BaseCommand):
    args = '<file_path>'
    help = 'Import users from json file'

    def handle(self, *args, **options):
        file_path = args[0]
        if not os.path.isfile(file_path):
            self.stdout.write('File %s not exists' % args[0])

        json_file = open(file_path)
        users = json.loads(json_file.read())

        for user in users:
            user_id = user['id']
            email = user['login']
            password = str(uuid.uuid4()).split('-')[0]

            name = name_len = None

            if user['fullname']:
                name = user['fullname'].split(' ')
            else:
                name = None

            name_len = len(name) if name else 0
            #last_name, first_name, second_name = user['fullname'].split(' ')
            first_name = second_name = last_name = None
            if name_len > 0:
                last_name = name[0]
                if name_len > 1:
                    first_name = name[1]
                    if name_len > 2:
                        second_name = name[2]

            try:
                user_field = User.objects.create_user(str(user_id), password=password)
            except IntegrityError:
                continue

            new_user = UserProfile(last_name=last_name, old_ID=user_id, email=email, user=user_field)
            new_user.save()
            self.stdout.write(email)