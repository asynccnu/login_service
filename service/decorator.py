import functools
import json
import base64
from aiohttp.web import Response
from .spider import info_login, info_cookie_login

def require_info_login(f):
    @functools.wraps(f)
    async def decorated_function(request, *args, **kwargs):
        authorized = False
        headers = request.headers # .keys()
        req_headers = dict(headers)

        JSESSIONID = req_headers.get('Jsessionid')
        BIGipServerpool_jwc_xk = req_headers.get('Bigipserverpool_Jwc_Xk')
        sid = req_headers.get('Sid')

        # if JSESSIONID and BIGipServerpool_jwc_xk and sid:
        #     # 客户端爬虫
        #     cookies = {'JSESSIONID': JSESSIONID, 'BIGipServerpool_jwc_xk': BIGipServerpool_jwc_xk}
        #     s, sid = await info_cookie_login(sid, cookies)
        #     if s is None:
        #         return Response(body = b'{}',
        #         content_type = 'application/json', status = 403)
        #     else: authorized = True

        basic_auth_header = req_headers.get('Authorization')
        if basic_auth_header and not authorized:
            auth_header = basic_auth_header[6:]
            uid, pwd = base64.b64decode(auth_header).decode().split(':')
            # session, sid
            s, sid = await info_login(uid, pwd)
            if s is None:
                return Response(body = b'{}',
                content_type = 'application/json', status = 403)
            else: authorized = True

        if authorized:
            response = await f(request, s, sid, *args, **kwargs)
            return response
        else:
            return Response(body = b'{}',
            content_type = 'application/json', status = 401)
    return decorated_function
