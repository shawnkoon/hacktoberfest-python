from shutil import get_terminal_size
from time import sleep
score=0
dic={
    "Humpty":"Dumpty",
    "King":"Queen",
    "Cinderella": "Prince Charming",
    "Cat": "Mouse",
    "Tom": "Jerry",
    "Rock": "Roll",
    "Bow": "Arrow",
    "Lock": "Key",
    "Surf": "Turf",
    "Pancakes": "Syrup",
    "Fork": "Knife",
    "Milk": "Cookies",
    "Rhythm": "Blues",
    "Mickey": "Minnie",
    "Salt": "Pepper",
    "Copy": "Paste",
    "Games": "Fun",
    "Python": "More Fun",
    "Errors": "Debug",
}
print("Hey! Let's play a game :)")
print("So here are the rules!")
print("Try to remember as many pairs as you can, you have got 20 seconds to memorise! "
      "Let's see how much you score ;)")
for key,value in dic.items():
    print(key+":"+value,end=" || ",flush=True)
    sleep(1)
sleep(1)
print("\n" * get_terminal_size().lines, end='')
print("Let's test your Memory now!")
sleep(1)
for key in dic.keys():
    ans=input(key+": ").title()
    if ans==dic[key]:
        score+=1
        print("Correct!")
    else:
        print("Wrong! The correct answer is",dic[key])
print("Great! Your Final score is",score,"/",len(dic))