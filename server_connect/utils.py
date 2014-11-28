import requests
import xml.etree.cElementTree as eTree
import re
import HTMLParser
from django.template import Context, Template
from datetime import datetime
from .models import ConnectSetting
from django.conf import settings


def get_1c_time(time=None):
    """ Deciseconds from 2014.01.01 """
    try:
        delta = time - datetime(2014, 1, 1)
        return int(delta.total_seconds() * 10)
    except TypeError:
        return 0


def request2server(method='get', article=''):
    last_updated_obj, created = ConnectSetting.objects.get_or_create(key='catalog_updated')
    if created:
        last_updated = 0
    else:
        last_updated = last_updated_obj.value
    # last_updated = 216528800
    last_updated = 0
    ip = settings.SERVER_1C_IP
    port = settings.SERVER_1C_PORT
    path = settings.SERVER_1C_PATH
    request_body_tpl = Template("""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:wsn="http://{{ ip }}{% if port %}:{{ port }}{% endif %}/wsNomenEx">
    <soap:Header/>
    <soap:Body>
        <wsn:{{ method }}>
            <wsn:numb>{{ data }}</wsn:numb>
            <wsn:article>{{ article }}</wsn:article>
        </wsn:{{ method }}>
    </soap:Body>
</soap:Envelope>
    """)
    c = Context({
        'ip': ip,
        'port': port,
        'method': method,
        'data': last_updated,
        'article': article,
    })
    server_url = "http://%s:%s/%s" % (ip, port, path)
    content_type = 'application/soap+xml;charset=UTF-8;action="http://%s:%s/wsNomenEx#wsNomenExchange:get"' % (ip, port)
    r = requests.post(
        server_url,
        data=request_body_tpl.render(c),
        headers={
            'content-type': content_type,
            'Authorization': 'Basic SVVTUjpXU3VyMXB3RA=='
        }
    )
    print(r.status_code)
    try:
        nt = re.search(r'.*<m:return[^>]*>(.*)</m:return>.*', r.text, re.MULTILINE | re.DOTALL)
        xml = HTMLParser.HTMLParser().unescape(nt.group(1))
    except:
        xml = None
    last_updated_obj.value = get_1c_time(datetime.now())
    last_updated_obj.save()
    return xml