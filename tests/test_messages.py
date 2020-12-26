from helpers.messge_process_helper import MessageProcessHelper


class TestMessage:

    def test_random_replies(self):
        user_input = "真的喔？"
        replies = []
        for _ in range(6):
            reply = MessageProcessHelper(user_input).calc_reply()
            replies.append(reply)

        assert len(set(replies)) > 3

    def test_mandarin_input_thankful(self):
        """
        (Mandarin)
        Make sure thankful message is returned when user input contains keywords
        """
        user_input = "好感謝今天..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "感謝", "確實" in reply

        user_input = "真的很感恩今天..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "感恩", "確實" in reply

        user_input = "很謝謝今天..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "謝謝", "確實" in reply

        user_input = "凡事謝恩..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "謝恩", "確實" in reply

    def test_en_input_thankful(self):
        """
        (English)
        Make sure thankful message is returned when user input contains keywords
        """
        user_input = "I am thankful for ...."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "thankful","indeed" in reply

        user_input = "I am grateful for..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "grateful","indeed" in reply

        user_input = "so blessed for..."
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "blessed","indeed" in reply

    def test_language_input_random(self):
        """
        Make sure random message is returned in language of user input
        """
        user_input = "是喔"
        mph = MessageProcessHelper(user_input)
        reply = mph.calc_reply()
        assert mph.detect_language(reply) == 'mandarin'

        user_input = "Oh really?"
        mph = MessageProcessHelper(user_input)
        reply = mph.calc_reply()
        assert mph.detect_language(reply) == 'english'

    def test_en_upper(self):
        """
        Make sure different cases are read correctly
        """
        # Upper case
        user_input = "I AM SO GRATEFUL FOR"
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "GRATEFUL", "indeed" in reply

        # Mixed case
        user_input = "Extremely Grateful for"
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "Grateful", "indeed" in reply

    def test_mixed_language(self):
        """
        Make sure mixed languages are replied correctly
        """
        user_input = "I AM SO GRATEFUL FOR 你這個朋友！"
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "GRATEFUL", "indeed" in reply

        user_input = "我很感謝你 as a friend"
        reply = MessageProcessHelper(user_input).calc_reply()
        assert "感謝", "indeed" in reply

    def test_foreign_language(self):
        """
        Make sure a third language is handled properly with default to mandarin
        """
        user_input = "Ahoj" # 捷克文
        reply = MessageProcessHelper(user_input).calc_reply()

        # Make sure a reply is returned
        assert MessageProcessHelper.detect_language(user_input) == 'mandarin'


