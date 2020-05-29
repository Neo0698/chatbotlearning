# chatbotlearning
so what's a chatbot, a chatbot is simply a program that can understand what words are important in a phrase and know that for exemple if he sees "hello "and "how" and you" he need's to print("im find")
<p></p>
so how to do that
<p></p>
<h1>first step</h1>
the first step is to know what the user says what phrase to do that we will use the method <b>upper</b><p></p>
for exemple<p></p>
question=upper("what is our question:")<p>
print(question)<p>
<p></p>
normally question is equal to the text that you type on the keyboard
<p></p>
know we need to tell to the computer when the user ask this question answer this question
<p>to do that their is to methode</p>
the first one<p>
if(question=="hello how are you"):<p>
    print("hello, im find thank you")
 <p></p>
 but their ise a better methode that it's with the fonction .find()
 <p>
  so for exemple with this code<p></p>
  question=upper("what is our question:")<p>
  hellof=question.find("hello")<p>
  print(hellof)<p>
  <p></p>
  you can see that when you put a phrase that have hello in it you can see a number that it's not -1 and when there is no hello there is a number =-1 know we will use that for our chatbot
  <p></p>
  <h1>this is the code</h1>
  <p></p>
question=upper("what is our question:")<p>
print(question)<p>
hellof=str(question.lower()).find("hello")<p>
howf=str(question.lower()).find("how")<p>
youf=str(question.lower()).find("you")<p>
if(hellof is not -1 and howf is not -1 and youf is not -1):<p>
    print("hello, im find and you")
 <p></p>
 know you know the fonctions<p>
  -find<p>
  -lower<p>
  -upper<p>
