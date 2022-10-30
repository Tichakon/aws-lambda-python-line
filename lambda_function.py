import json
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


def lambda_handler(event, context):
    line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])
    handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])

    msg = json.loads(event['body'])

    line_bot_api.reply_message(
        msg['events'][0]['replyToken'],
        TextSendMessage(text=msg['events'][0]['message']['text'])
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": 'ok'})
    }