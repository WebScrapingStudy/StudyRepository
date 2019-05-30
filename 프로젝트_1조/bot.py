# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.decorators import channel
from .boannews import boann

class Bot(BaseBot):
    """Represent a Bot logic which interacts with a user.

    BaseBot superclass have methods belows:

    * Send message
      * self.send_message(message, chat_id=None, channel=None)
    * Data Storage
      * self.set_project_data(data)
      * self.get_project_data()
      * self.set_user_data(data, user_id=None, channel=None)
      * self.get_user_data(user_id=None, channel=None)
    * Channel Handler
      from bothub_client.decorators import channel
      @channel('<channel_name>')
      def channel_handler(self, event, context):
        # Handle a specific channel message
    * Command Handler
      from bothub_client.decorators import command
      @command('<command_name>')
      def command_handler(self, event, context, args):
          # Handle a command('/<command_name>')
    * Intent Handler
      from bothub_client.decorators import intent
      @intent('<intent_id>')
      def intent_result_handler(self, event, context, answers):
          # Handle a intent result
          # answers is a dict and contains intent's input data
            {
              "<intent slot id>" : <entered slot value>
              ...
            }
    """
    @channel()
    def default_handler(self, event, context):
        """Handle a message received

        event is a dict and contains trigger info.

        {
           "trigger": "webhook",
           "channel": "<name>",
           "sender": {
              "id": "<chat_id>",
              "name": "<nickname>"
           },
           "content": "<message content>",
           "raw_data": <unmodified data itself webhook received>
        }
        """
        message = event.get('content')
        if message[0] == '!':
            response = message[1:]+'의 검색 결과입니다.\n'+ boann().search(message[1:])
            self.send_message(response)
        elif message == '보안뉴스' or message == '최신' or message == '전체기사':
            response = '최신뉴스 입니다 \n' + boann().All_News()
            self.send_message(response)
        elif message == '취약점' or message == '취약':
            response = '최근 취약점 뉴스 입니다 \n' + boann().vulnerability()
            self.send_message(response)
        elif message == '시큐리티월드' or message == '월드':
            response = '시큐리티월드 입니다 \n' + boann().securityworld()
            self.send_message(response)
        elif message == '랜섬웨어' or message == 'ransomware':
            response = '랜섬웨어 뉴스 입니다 \n' + boann().ransomware()
            self.send_message(response)
        elif message == '인공지능' or message == 'AI' or message == 'ai' or message == 'Ai':
            response = '인공지능 뉴스 입니다 \n' + boann().AI()
            self.send_message(response)
        elif message == '시큐리티' or message == 'security':
            response = '시큐리티 뉴스 입니다 \n' + boann().security()
            self.send_message(response)
        elif message == '사건' or message == '사고' or message == '사건사고':
            response = '사건사고 뉴스 입니다 \n' + boann().event()
            self.send_message(response)
        elif message == '안전' or message == 'SAFETY':
            response = 'SAFETY 뉴스 입니다 \n' + boann().SAFETY()
            self.send_message(response)
        elif message == '국제' or message == 'international':
            response = '국제 뉴스 입니다 \n' + boann().international()
            self.send_message(response)
        elif message == '공공' or message == '정책':
            response = '공공/정책 뉴스 입니다 \n' + boann().pub()
            self.send_message(response)
        elif message == '인터뷰' or message == 'interview' or message == '오피니언':
            response = '인터뷰/오피니언 뉴스 입니다 \n' + boann().pub()
            self.send_message(response)
        elif message == '주말판' or message == '주말' or message == 'weekend':
            response = '주말판 뉴스 입니다 \n' + boann().weekend()
            self.send_message(response)
        else:
            self.send_message('알 수 없는 명령어입니다 : {} \n'
                              '보안뉴스,최신,전체기사,취약점,취약,시큐리티월드,'
                              '월드,랜섬웨어,인공지능,AI,Ai,ai,시큐리티,사건,사고,사건사고,안전,국제,공공,정책,'
                              '인터뷰,오피니언,주말판,주말 등의 명령어가 있습니다.\n'
                              '검색을 원하신다면 !키워드 를 이용하여 검색할 수 있습니다.'.format(event['content']))
