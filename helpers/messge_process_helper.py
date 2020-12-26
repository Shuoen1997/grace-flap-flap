class MessageProcessHelper:
    random_replies = {
        "zh-cn": [
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
        "en": [
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
        "zh-cn": ["感恩", "感謝", "謝恩", "謝謝"],
        "en": ["thankful", "grateful"]
    }

    thank_reply = {
        "zh-cn": f"確實是很值得感恩的事呢！「{0}」，幫你記錄下來囉:)",
        "en": f"'{0}'!Something to be thankful for indeed! I have noted it down for you :)"
    }

    def __init__(self, user_input):
        self.user_input = user_input

    def detect_language(self, text) -> str:
        from langdetect import detect
        lan = detect(text)
        # if the detected language is not English nor Chinese
        if lan not in ['zh-cn', 'en']:
            # Correct the common mistake
            if lan == 'ko':
                return 'zh-cn'
            if lan == 'ro':
                return 'en'
        return lan

    def calc_reply(self) -> str:
        from random import choice
        lan = self.detect_language(self.user_input)

        # If the user input contains the thankful keyword for that language,
        # then reply with the thankful reply
        # Else, give a randomized reply of the language
        if any(k in self.user_input for k in self.thank_keywords[lan]):
            return self.thank_reply[lan].format(self.user_input)
        else:
            return choice(self.random_replies[lan])
