from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
line_handler = WebhookHandler('LINE_CHANNEL_SECRET')



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def fA(info):
    url = 'https://tw.stock.yahoo.com/quote/'+info+'.TW'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    #title = soup.find('h1')
    

    try:
        title = soup.select('.Fw\(b\)')[0]
        a = soup.select('.Fz\(32px\)')[0]
        b = soup.select('.Fz\(20px\)')[0]
        s = ''
    except IndexError:
        return '沒有此股票'


    try:    
        if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-down\)')[0]:
            s = '-'
    
    except:

                try:

                    if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C\(\$c-trend-up\)')[0]:
                        s = '+'
                except:

                    s = '-'
                

    return title.get_text()+' '+a.get_text()+' '+s+b.get_text()

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text               
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(fA(getA))))    
        


if __name__ == "__main__":
    app.run()