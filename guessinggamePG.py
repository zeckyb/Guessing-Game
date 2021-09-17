import random
num=random.randint(1,15)
user=input("whats ur name?")
insult_list=["wow ur bad at this",\
    "come on! you can get the number!!! HERES A HINT: you haven’t guessed it yet","nope, keep going",\
        "jeez," +(user)+ " we're gonna have to come up with more insults just 4 u",(user) + " are u even trying??",\
    "Thou hast no more brain than i have in mine elbows\n” -shakespeare", (user) + " wow, you really are bad at this"]

guess=None

while guess != num:
   guess=input("guess a number 1-15:")
   guess=int(guess)
   if int(guess) < 1 or int(guess) > 15:
       print("i said 1-15 bozo")
       continue
   if guess == num:
        print("wrong")
        break
   if guess != num: 
    print(random.choice(insult_list))
   
   
  