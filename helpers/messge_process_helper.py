class MessageProcessHelper:
    random_replies = {
        "mandarin": [
            "你真的很可愛耶！哈哈哈哈哈",
            "沒什麼事的話我先去玩沙囉，疑不對，魟魚會玩沙嗎？",
            "有感恩的事嗎？沒有的話我先去玩沙囉！",
            "我聽著呢！",
            "其實我也沒有厲害到聽得懂你說的話啦...哈哈",
            "我要去跟我的貝殼玩了～薩呦那拉",
            "魟魚我今天感恩的事情是什麼事不用做耍廢了一天",
            "咕嚕咕嚕咕嚕嚕",
            "蛤？你說什麼！",
            "能做你朋友我很榮幸，你帶給我好多快樂哦！",
            "你好好玩喔ＸＤ"
        ],
        "english": [
            "You are such a cutie :D",
            "Just chilling, I guess",
            "Any thankful things? If not I'm gonna go play with crab now!",
            "Go on, I am listening",
            "To be totally honest I don't understand what you are saying",
            "Gotta go play with them sea stars now, see-ya",
            "The thing I am thankful for is I can be a sea couch potato",
            "goo-loo-goo-loo",
            "Huh? What?",
            "I am glad we are friends :) You bring me so much happiness!",
            "You are so amusing XD"
        ],
    }

    thank_keywords = {
        "mandarin": ["感恩", "感謝", "謝恩", "謝謝"],
        "english": ["thankful", "grateful", "blessed"]
    }

    def __init__(self, user_input):
        self.user_input = user_input

    @staticmethod
    def get_thankful_reply(text, language):
        if language == 'mandarin':
            return f"確實是很值得感恩的事呢！「{text}」，幫你記錄下來囉:)"
        else:
            return f"'{text}' ! Something to be thankful for indeed! I have noted it down for you :)"

    @staticmethod
    def detect_language(text) -> str:
        """
        :param text:
        :return: Has to return one of ['zh-cn', 'en']
        """
        from langdetect import detect
        try:
            language = detect(text)
        except Exception as e:
            print("An exception has occurred! Exception: ", e)
            return 'mandarin'
        else:
            # if the detected language is not English nor Chinese
            if language in ['zh-cn', 'zh-tw', 'ko']:
                return 'mandarin'
            if language in ['en', 'ro', 'fr', 'af', 'it']:
                return 'english'

        raise KeyError("Language not caught in the condition. Lan is: " + language)

    def calc_reply(self) -> str:
        from random import choice
        language = self.detect_language(self.user_input)

        # If the user input contains the thankful keyword for that language,
        # then reply with the thankful reply
        # Else, give a randomized reply of the language
        if any(k in self.user_input.lower() for k in self.thank_keywords[lan]):
            return self.get_thankful_reply(text=self.user_input, language=language)
        else:
            return choice(self.random_replies[lan])


if __name__ == '__main__':
    while True:
        user_input = input("Enter your message: ")
        lan = MessageProcessHelper.detect_language(user_input)
        print("Detected language:" + lan)

        reply = MessageProcessHelper(user_input).calc_reply()
        print("Reply:" + reply)
