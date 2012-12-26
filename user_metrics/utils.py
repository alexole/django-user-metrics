import memcache
import hashlib
import base64
import uuid

def get_visitor_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not x_forwarded_for:
        return request.META.get('REMOTE_ADDR', '')
    return x_forwarded_for.split(',')[0]

def get_visitor_hash(request):
    h = hashlib.md5()

    ip = get_visitor_ip(request)

    h.update(ip)
    h.update('\n')
    h.update(request.META.get('HTTP_USER_AGENT', ''))

    return base64.b64encode(h.digest()).replace('=', '')

def create_visitor_id(request, visitor_hash=None):
    if visitor_hash is None:
        visitor_hash = get_visitor_hash(request)

    visitor_id = base64.b64encode(uuid.uuid4().bytes).replace('=', '')

    mc = memcache.Client(['127.0.0.1:11211'])
    if not mc.add(visitor_hash, visitor_id, time=3):
        return visitor_id

    value = mc.get(visitor_hash)
    if not value:
        return visitor_id

    return value
