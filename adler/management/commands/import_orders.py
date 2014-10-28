from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

import json
import os.path

from order.models import Order, OrderItem
from catalog.models import Item


class Command(BaseCommand):
    args = '<file_path>'
    help = 'Import orders from json file'

    def handle(self, *args, **options):
        file_path = args[0]
        if not os.path.isfile(file_path):
            self.stdout.write('File %s not exists' % args[0])

        json_file = open(file_path)
        orders = json.loads(json_file.read())

        for order in orders:
            print(order['id'])

            try:
                user = User.objects.get(username=str(order['user_id']))
            except User.DoesNotExist:
                continue

            try:
                new_order = Order.objects.get(pk=order['id'])
            except Order.DoesNotExist:
                print('Does.NotExist')
                new_order = Order(user=user, total_price=0)

            new_order.city = order['city']
            print(order['address'])
            new_order.address_street = order['address'][:63]
            new_order.total_price = float(order['total'])
            #new_order.payment_method = order['payment_method']
            new_order.phone = order['phone'][:31]
            new_order.address_zipcode = order['zip_code']
            new_order.add_time = order['timestamp']
            new_order.user = user
            client_name = client_name_len = None

            if order['fullname']:
                client_name = order['fullname'].split(' ')
            else:
                client_name = None
            client_name_len = len(client_name) if client_name else 0

            client_first_name = client_second_name = client_last_name = None
            if client_name_len > 0:
                client_last_name = client_name[0]
                if client_name_len > 1:
                    client_first_name = client_name[1]
                    if client_name_len > 2:
                        client_second_name = client_name[2]
            new_order.client_name = client_first_name or ""
            new_order.client_second_name = client_second_name
            new_order.client_last_name = client_last_name
            new_order.save()

            items = order['items']
            for item in items:
                new_item = OrderItem()
                new_item.order = new_order
                new_item.scale = item['scale']
                new_item.name = item['title']
                #new_item. = item['url']
                new_item.price = float(item['price'])
                new_item.article = item['article']
                new_item.quantity = item['quantity']
                new_item.manufacturer = item['manufacturer']
                try:
                    new_item.item = Item.objects.get(article=new_item.article)
                except Item.DoesNotExist:
                    continue
                new_item.save()

                # order['shipping_method']
                # order['comments']
                # discount = order['discount']
                # order['state']
                # order['total_without_discount']
                # order['shipping_price']
                #
                # order['fullname']
                #