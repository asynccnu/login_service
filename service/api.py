from aiohttp import web
from .decorator import require_info_login

api = web.Application()

# ====== async view handlers ======
@require_info_login
async def info_login_api(request, s, sid):
    cookies = str(s.__dict__.get('_cookies').get('portal.ccnu.edu.cn'))
    BIGipServerpool_portal = cookies.split()[1].split('=')[1][:-1]
    JSESSIONID = cookies.split()[-3].split('=')[1][:-1]
    return web.json_response({'cookie': {
        'BIGipServerpool_portal': BIGipServerpool_portal,
        'JSESSIONID': JSESSIONID }})
# =================================

# ====== url --------- maps  ======
api.router.add_route('GET', '/info/login/', info_login_api, name='info_login_api')
# =================================
