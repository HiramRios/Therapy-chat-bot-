import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
import re
import random



sid = SentimentIntensityAnalyzer()

def get_sentiment(sentence):

    sentiment_score = sid.polarity_scores(sentence)

    positive_meter = round((sentiment_score['pos'] * 10), 2) 
    negative_meter = round((sentiment_score['neg'] * 10), 2)

    return positive_meter, negative_meter



# part 

list_words2=['hello','bye', "good", "bad"]
list_syn2={}
for word in list_words2:
    synonyms2=[]
    for syn2 in wordnet.synsets(word):
        for lem2 in syn2.lemmas():
            
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem2.name())
            synonyms2.append(lem_name)
   
    list_syn2[word]=set(synonyms2)







keywords2={}
keywords_dict2={}

# Defining a new key in the keywords dictionary
keywords2['greet']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn2['hello']):
    keywords2['greet'].append('.*\\b'+synonym+'\\b.*')
 
# Defining a new key in the keywords dictionary
keywords2['bye']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn2['bye']):
    keywords2['bye'].append('.*\\b'+synonym+'\\b.*')


keywords2['good']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn2['good']):
    keywords2['good'].append('.*\\b'+synonym+'\\b.*')





keywords2['bad']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn2['bad']):
    keywords2['bad'].append('.*\\b'+synonym+'\\b.*')



 
for intent, keys in keywords2.items():
    
    # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
    keywords_dict2[intent]=re.compile('|'.join(keys))
#print (keywords_dict)




responses2={
    'greet':['I know you might now want to talk about it but i can help you',"I know you might now want to talk about it but i can help you","I know you might now want to talk about it but i can help you"],
    'bye':['Please just breathe and rememebr that there is a lot to live for', "Please just talk to me a little longer", "If you give me the chance i can help you"],

    "good":["Awesome im glad that i was abel to change your mood", "Thats amazing im glad we were abel to make progress", "we were abel to accomplish so much awesome  "],
    "bad":["Hey everything is giong to be okay just focus on you", "Sometimes you just gotta start over from the basics", "I do believe that you future will be bright how are you felling now "],

    'fallback':'I dont quite understand. Could you repeat that?',
}

















#chatbot()
#chat = Chat(set_pairs, reflections)
#chat.converse()

'''username = input("Hi, I'm the chatbot you built i was just checking on your health how are you doing today ")
positive_meter, negative_meter = get_sentiment(username)
print("Positive", positive_meter)
print("Negative", negative_meter)

while(negative_meter> positive_meter or positive_meter<9.5):

  username= input("tell me how you are still feeling")
  positive_meter, negative_meter = get_sentiment(username)
  print("Positive", positive_meter)
  print("Negative", negative_meter)
'''

list_words=['hello','bye', "good", "bad"]
list_syn={}
for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
   
    list_syn[word]=set(synonyms)
    
print(list_syn)



print("")
print("")
print("")
print("")



keywords={}
keywords_dict={}

# Defining a new key in the keywords dictionary
keywords['greet']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['hello']):
    keywords['greet'].append('.*\\b'+synonym+'\\b.*')
 
# Defining a new key in the keywords dictionary
keywords['bye']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['bye']):
    keywords['bye'].append('.*\\b'+synonym+'\\b.*')


keywords['good']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['good']):
    keywords['good'].append('.*\\b'+synonym+'\\b.*')





keywords['bad']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
for synonym in list(list_syn['bad']):
    keywords['bad'].append('.*\\b'+synonym+'\\b.*')



 
for intent, keys in keywords.items():
    
    # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
    keywords_dict[intent]=re.compile('|'.join(keys))
#print (keywords_dict)




responses={
    'greet':['Hello! How can I help you?',"how are you doing","Hello how is your lovely day going so far"],
    'bye':['I hope you continue to work on yourself', "bye have a wonderful day", "I hope i was able to be of good use to you"],

    "good":["That is amazing im glad i was able to help", "awesome im doing pretty well myself", "well that is all i needed to hear awesome blossom "],
    "bad":["Im sorry to hear that lets talk about it", "Hey dont owrry it it going to get better lets discuss it ", "Hey don't worry it will get better maybe i can help boosts your spirrits"],

    'fallback':'I dont quite understand. Could you repeat that?',
}



print ("Welcome to Teddy Bear. How are you doing?")

# While loop to run the chatbot indefinetely
while (True):  
    
    # Takes the user input and converts all characters to lowercase
    user_input = input().lower()
    positive_meter, negative_meter = get_sentiment(user_input)
    print("Positive", positive_meter)
    print("Negative", negative_meter)
    
    # Defining the Chatbot's exit condition
    if user_input == 'quit': 
        print ("Thank you for visiting.")
        break    
    
    matched_intent = None 

    if(negative_meter>3.0):
      print("ahh no it really looks like your are down in the feels maybe there is something i can do to lift your spirits up more ")
      print("what is your emotion right now")
      while(negative_meter> positive_meter or positive_meter<6.1):
        user_input = input().lower()
        positive_meter, negative_meter = get_sentiment(user_input)
        print("Positive", positive_meter)
        print("Negative", negative_meter)
        for intent,pattern in keywords_dict2.items():
        
        # Using the regular expression search function to look for keywords in user input
          if re.search(pattern, user_input): 
              
              # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
            matched_intent=intent  
      
      # The fallback intent is selected by default
        key='fallback' 
        if matched_intent in responses2:
            
            # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
          key = matched_intent 
        
        # The chatbot prints the response that matches the selected intent
        n = random.randint(0,2)
        print (responses2[key][n]) 














    
    for intent,pattern in keywords_dict.items():
        
        # Using the regular expression search function to look for keywords in user input
        if re.search(pattern, user_input): 
            
            # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
            matched_intent=intent  
    
    # The fallback intent is selected by default
    key='fallback' 
    if matched_intent in responses:
        
        # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
        key = matched_intent 
    
    # The chatbot prints the response that matches the selected intent
    n = random.randint(0,3)
    print (responses[key][n]) 