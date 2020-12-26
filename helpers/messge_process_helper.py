class MessageProcessHelper:
    random_replies_list = [
        "你真的很可愛耶！哈哈哈哈哈",
        "沒什麼事的話我先去玩沙囉，疑不對，魟魚會玩沙嗎？",
        "有感恩的事嗎？沒有的話我先去玩沙囉！",
        "我聽著呢！",
        "其實我也沒有厲害到聽得懂你說的話啦...哈哈",
        "我要去跟我的貝殼玩了～薩呦那拉",
        "魟魚我今天感恩的事情是什麼事不用做耍廢了一天",
        "咕嚕咕嚕咕嚕嚕",
        "蛤？你說什麼！"
    ]

    def __init__(self, user_input):
        self.user_input = user_input

    def calc_reply(self) -> str:
        from random import choice
        if '感恩' in self.user_input:
            return f"確實是很值得感恩的事呢！「{self.user_input}」，幫你記錄下來囉:)"
        else:
            return choice(self.random_replies_list)
