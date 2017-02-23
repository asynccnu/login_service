from aiohttp import web
from .decorator import require_info_login

api = web.Application()

# ====== async view handlers ======
@require_info_login()
async def info_login_api(request, s, sid):
    return web.json_response({})
# =================================

# ====== url --------- maps  ======
api.router.add_route('GET', '/info/login/', info_login_api, name='info_login_api')
# =================================
