import aiohttp

INFO_LOGIN = "http://portal.ccnu.edu.cn/loginAction.do"

async def info_login(sid, pwd):
    authorized = False
    payload = {'userName': sid, 'userPass': pwd}
    resp = await aiohttp.request(
        method = 'POST',
        url = INFO_LOGIN,
        data = payload
    )
    resp_text = await resp.text() 
    if 'index_jg.jsp' in resp_text:
        authorized = True
    return authorized
