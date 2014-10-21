from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import force_text
from server_connect.utils import request2server
from ...xml_import import import_some_item_from_tmp, read_catalog_data
from django.conf import settings


class Command(BaseCommand):
    help = 'Import catalog from 1C'

    def handle(self, *args, **options):
        xml = force_text(request2server())
        self.stdout.write('xml loaded')
        file_name = "%s/catalog/xml/catalog.xml" % settings.BASE_DIR
        f = open(file_name, "w")
        f.write(xml.encode('utf-8'))
        f.close()
        read_catalog_data(xml)
        import_some_item_from_tmp()