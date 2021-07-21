import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Lets play stone paper scissor")   

    else:
        speak("Good Evening! Lets play stone paper scissor")  

         
        
if __name__ == "__main__":
    wishMe()
    from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie! don,t worry i definitely WIN next time")
        r = str("Tie! don,t worry i definitely WIN next time")
        speak(r)
    elif player == "Rock":
        if computer == "Paper":
            print(f"You lose! {computer}, covers {player} hahahahaaaaa")
            r=str(f"You lose! {computer}, covers {player} hahahahaaaaa")
            speak(r)
        else:
            print(f"You win! {player}, smashes {computer}, annnhhhhhhhhhh why this happen to me!!!!")
            r=str(f"You win! {player}, smashes {computer}, annnhhhhhhhhhh why this happen to me!!!!")
            speak(r)
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You lose!{computer}, cut {player} hahahahaaaaa")
            r=str(f"You lose!{computer}, cut {player} hahahahaaaaa")
            speak(r)
        else:
            print(f"You win! {player},covers {computer}, annnhhhhhhhhhh why this happen to me!!!!")
            r=str(f"You win! {player},covers {computer}, annnhhhhhhhhhh why this happen to me!!!!")
            speak(r)
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You lose...{computer}, smashes {player} hahahahaaaaa")
            r=str(f"You lose...{computer}, smashes {player} hahahahaaaaa")
            speak(r)
        else:
            print(f"You win! {player}, cut {computer} annnhhhhhhhhhh why this happen to me!!!!")
            r=str(f"You win! {player}, cut {computer} annnhhhhhhhhhh why this happen to me!!!!")
            speak(r)
    else:
        print("That's not a valid play. Check your spelling!")
        r=str("That's not a valid play. Check your spelling!")
        speak(r)
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

