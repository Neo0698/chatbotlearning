# chatbotlearning
so what's a chatbot, a chatbot is simply a program that can understand what words are important in a phrase and know that for exemple if he sees "hello "and "how" and you" he need's to print("im find")
<p></p>
so how to do that
<p>in this document you will have how to use the fonction that will be used in the final code, the final code and some link to better understand</p>

<h1>first step</h1>
the first step is to know what the user says what does he type, for that we use the method  <b>input</b><p></p>
for exemple<p></p>
question=input("what is our question:")<p>
print(question)<p>
<p></p>
normally question is equal to the text that you type on the keyboard
<p></p>
know we need to tell to the computer when the user ask this question answer this answer
<p>to do that their is to option but the last one is better</p>
the first one<p>

```
if(question=="hello how are you"):
         print("hello, im find thank you")
```

 <p></p>
 but their ise a better methode that it's with the fonction .find()
 <p>
  so for exemple with this code<p></p>
  question=upper("what is our question:")<p>
  hellof=question.find("hello")<p>
  print(hellof)<p>
  <p></p>
  you can see that when you put a phrase that have hello in it you can see a number that it's not -1 and when there is not hello in hit there is a number equel to -1 know we will use that for our chatbot
  <p></p>
  <h1>this is the code final</h1>
  <p></p>
```
question=input("what is our question:")#know what the user type
print(question)#print what the user type
hellof=str(question.lower()).find("hello")#find hello with the variable question in tiny
howf=str(question.lower()).find("how")#find how with the variable question in tiny
youf=str(question.lower()).find("you")find you with the variable question in tiny
if(hellof is not -1 and howf is not -1 and youf is not -1):#find if the variable hellof and howf and youf is not -1
    print("hello, im find and you")# when hellof and howf and youf is not -1 print the answer
```
 <p></p>
 ```
 know you know the fonctions<p>
  -find<p>
  -lower<p>
  -input<p>
```
some sources to help you on stack overflow<p></p>
     <a href="https://stackoverflow.com/questions/3345202/getting-user-input">https://stackoverflow.com/questions/3345202/getting-user-input</a>
     <a href="https://stackoverflow.com/questions/674764/examples-for-string-find-in-python">https://stackoverflow.com/questions/674764/examples-for-string-find-in-python</a>
