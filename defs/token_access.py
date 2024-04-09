from config_reader import config
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat


token = config.gigachat_token.get_secret_value()
chat = GigaChat(credentials=token,
                model='GigaChat',
                verify_ssl_certs=False)


class MessageGenerator:
    def __init__(self, content):
        self.content = content
        self.messages = [(SystemMessage(content=self.content))]

    def restart(self):
        content = self.content
        self.messages = [(SystemMessage(content=content))]


async def take_response(user_input: str, mg: MessageGenerator):
    mg.messages.append(HumanMessage(content=user_input))
    res = chat(mg.messages)
    mg.messages.append(res)
    print(mg.messages)
    return res.content
