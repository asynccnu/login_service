from aiohttp import web
from .decorator import require_info_login

api = web.Application()

# ====== async view handlers ======
@require_info_login
async def info_login_api(request, s, pwd, sid):
    cookies = s.__dict__.get('_cookies').get('portal.ccnu.edu.cn')
    BIGipServerpool_portal = cookies.get('BIGipServerpool_portal').__dict__['_value']
    JSESSIONID = cookies.get('JSESSIONID').__dict__['_value']
    return web.json_response({'cookie': {
        "UM_distinctid": "15b5d8be64f12e-0bf2dfe294ca19-396a7805-13c680-15b5d8be65e45",
        'BIGipServerpool_portal': BIGipServerpool_portal,
        'JSESSIONID': JSESSIONID
    }, 'sid': sid, 'pwd': pwd})
# =================================

# ====== url --------- maps  ======
api.router.add_route('GET', '/info/login/', info_login_api, name='info_login_api')
# =================================
