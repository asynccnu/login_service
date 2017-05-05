import os
import base64
import aiohttp
from aiohttp.test_utils import TestClient, loop_context

def test_info_login_api(app):
    with loop_context() as loop:
        with TestClient(app, loop=loop) as client:
            
            async def _test_info_login_api():
                auth_header1 = {'Authorization': 'Basic %s' % base64.b64encode(b'2014210761:2014210761')}
                auth_header2 = {'Authorization': 'Basic %s' % base64.b64encode(b'2014210761:fuckccnu')}
                auth_header3 = {}
                resp = await client.get('/api/info/login/', headers=auth_header1)
                assert resp.status == 200
                resp = await client.get('/api/info/login/', headers=auth_header2)
                assert resp.status == 403
                resp = await client.get('/api/info/login/', headers=auth_header3)
                assert resp.status == 401
                print('... test info login api [ok]')

            loop.run_until_complete(_test_info_login_api())
            loop.close()
