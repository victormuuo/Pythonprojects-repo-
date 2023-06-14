print("Welcome to my computer quiz")

playing=input("Do you want to play? ")
 
if playing.lower()!="yes":
    quit()

print("Okay! Let's play 😚")
score=0

answer=input("What does IBM stand for? ")
if answer.lower()=="international business machines":
    print("Correct ✅")
    score+=1
else: 
    print("Incorrect ❌")
    
answer=input("What does JSON stand for? ")
if answer.lower()=="javascript object notation":
    print("Correct ✅")
    score+=1
else: 
    print("Incorrect ❌")

answer=input("What does TED stand for? ")
if answer.lower()=="technology, entertainment and design":
    print("Correct ✅")
    score+=1
else: 
    print("Incorrect ❌")

answer=input("What does VR stand for? ")
if answer.lower()=="virtual reality":
    print("Correct ✅")
    score+=1
else: 
    print("Incorrect ❌")

answer=input("What does MBA stand for? ")
if answer.lower()=="master of business administration":
    print("Correct ✅")
    score+=1
else: 
    print("Incorrect ❌")

answer=input("What does PDF stand for? ")
if answer.lower()=="portable document format":
    print("Correct ✅")
    score+=1
else: 
    print("Incorrect ❌")

answer=input("What does GIT stand for? ")
if answer.lower()=="global information tracker":
    print("Correct ✅")
    score+=1
else: 
    print("Incorrect ❌") 

print(f"You got {score} questions correct!")
print(f"You got {score/7*100} %")         