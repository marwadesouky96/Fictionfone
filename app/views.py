from django.http import HttpResponse
from app.models import Tweet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import render
from django.conf import settings
from slackclient import SlackClient                               
from .collect_tweets import *
from .serializers import TweetSerializer



SLACK_VERIFICATION_TOKEN = getattr(settings,
'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,                          
'SLACK_BOT_USER_TOKEN', None)                                     
Client = SlackClient(SLACK_BOT_USER_TOKEN) 


def index(request):
  
    return HttpResponse("Hello! Welcome to Zappy")
    # return render(request, 'index.html')


class TweetListAPIView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    # return HttpResponse({queryset})
    
class Events(APIView):
    def post(self, request, *args, **kwargs):
        
        slack_message = request.data
        print("slack message = ", slack_message)
        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            print("token is not right")
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        if slack_message.get('type') == 'url_verification':        
            return Response(data=slack_message,                    
                            status=status.HTTP_200_OK)
        
        if 'event' in slack_message:
            event_message = slack_message.get('event')            
            
            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':     
                return Response(status=status.HTTP_200_OK)        
            
            # process user's message
            user = event_message.get('user')                      
            text = event_message.get('text')                      
            channel = event_message.get('channel')                
            bot_text = 'Collecting tweets'.format(user)             
            if 'go' in text.lower(): 
                print("hello from slack yooo ")                             
                Client.api_call(method='chat.postMessage',        
                                channel=channel,                  
                                text=bot_text) 
                collect_tweets()
                bot_text = "Tweets dispalyed here : http://localhost:4200/tweets"
                Client.api_call(method='chat.postMessage',        
                                channel=channel,                  
                                text=bot_text) 

                return Response(status=status.HTTP_200_OK)        

                            
        return Response(status=status.HTTP_200_OK)
