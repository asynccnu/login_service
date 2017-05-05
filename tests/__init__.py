from service import app
from .test_login_api import test_info_login_api

if __name__ == '__main__':
    test_info_login_api(app)
