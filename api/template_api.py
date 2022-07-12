# -*- coding: utf-8 -*-
__author__ = 'Guibin'

import app
import json
from tools.config_info import get_header


class TemplateAPI:

    #api_add_url = app.BASE_URL + "/xxx/xxxx/add"

    #api_upd_url = app.BASE_URL + "/xxx/xxxx/upd"

    api_get_url = app.BASE_URL + "/"

    #api_del_url = app.BASE_URL + "/xxx/xxxx/del/{id}"

    '''
    def api_add(self, session, attr1, attr2):
        post_data = {
            "attr1": attr1,
            "attr2": attr2
        }
        return session.post(self.api_add_url, headers=get_header(), data=json.dumps(post_data))
    '''

    '''
    def api_upd(self, session, attr1, attr2):
        put_data = {
            "attr1": attr1,
            "attr2": attr2
        }
        return session.put(self.api_upd_url, headers=get_header(), data=json.dumps(put_data))
    '''

    def api_get(self, session, attr1, attr2):
        params = {
            "attr1": attr1,
            "attr2": attr2
        }
        return session.get(self.api_get_url, headers=get_header(), params=params)


    '''
    def api_del(self, session, uid):
        return session.delete(self.api_del_url.format(id=uid), headers=get_header())
    '''