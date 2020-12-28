import pytest


class TestMain:
    def test_index_redirect(self, client):
        r = client.get('/')
        assert '302' in r.status


    def test_home_status_is_200(self, client):
        r = client.get('/home')
        assert '200' in r.status

    def test_user_login_status_is_200(self, client):
        r = client.get('/login')
        assert '200' in r.status

    def test_admin_login_status_is_200(self, client):
        r = client.get('/admin/login')
        assert '200' in r.status

    def test_main_failed_access(self, client):
        r = client.get('/admin/tool')
        assert b'Not permitted!' in r.data

    # @pytest.mark.skip(reason="This test is failing on Github for some reason")
    def test_main_success_access(self, auth_client):
        r = auth_client.get('/admin/tool')
        assert b'Your message' in r.data

    def test_callback_is_400_if_invalid_x_signature(self, client):
        r = client.post('/callback', headers={'X-Line-Signature': 0})
        assert '400' in r.status

