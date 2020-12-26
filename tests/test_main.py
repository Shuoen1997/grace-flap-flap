class TestMain:

    def test_home_status_is_200(self, client):
        # Thank you stranger!
        #
        r = client.get('/')
        assert '200' in r.status

    def test_home_failed_access(self, client):
        r = client.post('/main')
        assert '400' in r.status




