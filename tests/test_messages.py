from helpers.messge_process_helper import MessageProcessHelper


class TestMessage:

    def test_random_replies(self):
        user_input = "真的喔？"
        replies = []
        for _ in range(6):
            reply = MessageProcessHelper(user_input).calc_reply()
            replies.append(reply)

        assert len(set(replies)) > 3

    def test_language_input_thankful(self):
        user_input = "好感謝今天..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "感謝", "確實" in reply

        user_input = "真的很感恩今天..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "感恩", "確實" in reply

        user_input = "I am thankful for ...."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "I am thankful for" in reply

        user_input = "I am grateful for..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "I am grateful for" in reply

    def test_language_input_random(self):
        from langdetect import detect

        user_input = "是喔"
        mph = MessageProcessHelper(user_input)
        reply = mph.calc_reply()
        assert mph.detect_language(reply) == 'zh-cn'

        user_input = "Oh really?"
        mph = MessageProcessHelper(user_input)
        reply = mph.calc_reply()
        assert mph.detect_language(reply) == 'en'

    def test_en_upper(self):
        # Upper case
        user_input = "I AM SO GRATEFUL FOR"
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "GRATEFUL", "indeed" in reply

        # Mixed case
        user_input = "Extremely Grateful for"
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "Grateful", "indeed" in reply
