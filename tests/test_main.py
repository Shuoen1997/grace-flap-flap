


class TestMain:

    def test_home_status_is_200(self, client):
        r = client.get('/')
        assert '200' in r.status

    def test_main_failed_access(self, client):
        r = client.get('/main')
        assert b'Not permitted!' in r.data

    def test_main_success_access(self, auth_client):
        r = auth_client.get('/main')
        assert b'Your message' in r.data

    def test_callback_is_400_if_invalid_x_signature(self, client):
        r = client.post('/callback', headers={'X-Line-Signature': 0})
        assert '400' in r.status

