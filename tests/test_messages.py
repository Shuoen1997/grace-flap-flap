from helpers.messge_process_helper import MessageProcessHelper


class TestMessage:

    def test_grateful_reply(self):
        user_input = "我今天要感恩的事情是～"
        reply = MessageProcessHelper(user_input).calc_reply()
        print(reply)
        assert "確實" in reply

    def test_randomized_reply(self):
        user_input = "真的喔？"
        replies = []
        for _ in range(6):
            reply = MessageProcessHelper(user_input).calc_reply()
            replies.append(reply)

        assert len(set(replies)) > 3