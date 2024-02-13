from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer



bot = ChatBot('chatbot', read_only=False,
                logic_adapters=[
                    {
                        'import_path': 'chatterbot.logic.BestMatch',
                        #'default_response':  'sorry, I dont know what that means',
                        #'maximum_similarity_threshold': 0.90


                    }
                ])

list_to_train = [

    "hi", #question
    "how far my guy", #answer
    "What's your name?",
    "I'm sozorock bot",
    "what is your favorite food",
    "I like garri because sapa choke!",
    "what is your favorite layi's quote?",
    "hmm, i really like this one ...update cast but update don't finish because update is always up to date!",
    "what is the nigerian dream",
    "omo na to japa o!",
    "what is an average nigerian's watch word",
    "God Abeg!"

]


chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)


#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

chatterBotCorpusTrainer.train('chatterbot.corpus.english')




def index(request):
    return render(request, 'chat/index.html')

def specific(request):
    return HttpResponse('Specific page')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)