import asyncio
import aiohttp

info_login_url = "http://portal.ccnu.edu.cn/loginAction.do"
link_url = "http://portal.ccnu.edu.cn/roamingAction.do?appId=XK"
login_ticket_url = "http://122.204.187.6/xtgl/login_tickitLogin.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
}

async def info_login(sid, pwd):
    _cookie_jar = None
    payload = {'userName': sid, 'userPass': pwd} # 模拟登录表单(表单名userName, userPass分别对应学号密码)
    async with aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True),
            headers=headers) as session:
        async with session.post(info_login_url, data=payload) as resp: # 模拟登录信息门户
            resp_text = await resp.text() # 模拟登录后返回的HTML
            if resp_text.split('"')[1] == 'index_jg.jsp':
                async with session.get(link_url, timeout=4):
                    async with session.get(login_ticket_url, timeout=4):
                        _cookie_jar = session.__dict__.get('_cookie_jar')
                        return _cookie_jar, sid
            else: return (None, sid)
