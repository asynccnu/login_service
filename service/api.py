from aiohttp import web
from .decorator import require_info_login

api = web.Application()

# ====== async view handlers ======
@require_info_login
async def info_login_api(request, s, pwd, sid):
    cookies = s.__dict__.get('_cookies').get('122.204.187.6')
    BIGipServerpool_jwc_xk = cookies.get('BIGipServerpool_jwc_xk').__dict__['_value']
    JSESSIONID = cookies.get('JSESSIONID').__dict__['_value']
    return web.json_response({'cookie': {
        'BIGipServerpool_jwc_xk': BIGipServerpool_jwc_xk,
        'JSESSIONID': JSESSIONID
    }, 'sid': sid, 'pwd': pwd})
# =================================

# ====== url --------- maps  ======
api.router.add_route('GET', '/info/login/', info_login_api, name='info_login_api')
# =================================
