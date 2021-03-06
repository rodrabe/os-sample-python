from jumpgate.common import error_handling


class UserProjectsV3(object):
    def on_get(self, req, resp, user_id):
        client = req.sl_client
        account = client['Account'].getObject()
        currentUser = client['Account'].getCurrentUser()
        if currentUser['username'] != user_id:
            return error_handling.error(resp,
                                        'notMatch',
                                        'Invalid user',
                                        details=None,
                                        code=400)

        projects = [{
            'domain_id': str(account['id']),
            'enabled': True,
            'description': None,
            'name': currentUser['username'],
            'id': str(account['id']),
            }]

        resp.body = {'projects': projects, 'tenant_links': []}
