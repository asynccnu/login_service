import asyncio
import aiohttp

info_login_url = "http://portal.ccnu.edu.cn/loginAction.do"

async def info_login(sid, pwd):
    _cookie_jar = None
    payload = {'userName': sid, 'userPass': pwd}
    async with aiohttp.ClientSession() as session:
        async with session.post(info_login_url, data=payload) as resp:
            resp_text = await resp.text()
            if resp_text.split('"')[1] == 'index_jg.jsp':
                _cookie_jar = session.__dict__.get('_cookie_jar')
                return _cookie_jar, sid
            else: return (None, sid)
