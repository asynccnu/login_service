import base64
from aiohttp import web
from .spiders import info_login

api = web.Application()

async def info_login_api(request):
    status = 401
    headers_dict = dict(request.headers)
    basic_auth_header = headers_dict.get('Authorization')

    if basic_auth_header:
        auth_header = basic_auth_header[6:]
        uid, pwd = base64.b64decode(auth_header).decode().split(':')
        authorized = await info_login(uid, pwd)
        if authorized:
            status = 200
        else:
            status = 403
    return web.Response(
        body = b'{}',
        content_type = 'application/json',
        status = status
    )

api.router.add_route('GET', '/info/login/', info_login_api, name='info_login_api')
