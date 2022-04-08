    # Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
 
## CARD
## Barva, rank, hodnota 
import random 
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
suits = ("Hearts", "Diamonds", "Spades", "Clubs")

class Card: 
 
    def __init__(self, suit, rank):
         self.suit = suit
         self.rank = rank
         self.value = values[rank]
         
    def __str__(self):
        return self.rank + " of " + self.suit
  

  
  ## Deck
  
class Deck(): 
   
    def __init__(self):
       self.all_cards = []
       
       for suit in suits: 
           for rank in ranks:
               created_card = Card(suit,rank)
               self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

  #Player
  
class Player():
    
    def __init__(self,name,chip):
        
        self.name = name
        self.all_player_cards = []
        self.chip = chip
        self.aces = 0
        self.value = 0
    
    def hit_first(self,card):
        self.all_player_cards.append(card)
        if card.rank == "Ace":
            self.aces += 1
            
            
    def enough(self):
        pass
        
    def __str__(self):
        return f" Player {self.name} has {self.chip} chips"
        
    def countup(self):
        self.value = 0
        for i in self.all_player_cards:
            self.value += i.value
        for num in range(self.aces):
            if self.value >= 22:
                self.value -= 10
        
     

## Game starts - player gets 2 cards, computer gets 2, 1 facing down one facing up
## Player says how much he wants to bet // control if bet < player.chips
## Computer plays after player, either go over or under if player is busted
## Player either earns or loses the chips
## Is Players chips > 0? New round 

name = input("Enter your name: ")
chips = int(input("How much chips do you want? "))
new_player = Player(name,chips)
computer_player = Player("Computer",1)

def game_start(): 
    
    new_player.hit_first(new_deck.deal_one())
    new_player.hit_first(new_deck.deal_one())
    new_player.countup()
    
    computer_player.hit_first(new_deck.deal_one())
    computer_player.hit_first(new_deck.deal_one())
    computer_player.countup()
    
    print(f"Player has {new_player.all_player_cards[0]} and {new_player.all_player_cards[1]} the value of the hand is: {new_player.value} Player has {new_player.aces} of Aces")
    

    print(f"Computer has {computer_player.all_player_cards[0]}")
    

    
def player_bust():
    new_player.value > 21
    pass
def computer_bust():
    pass
def hand_dump():
    new_player.all_player_cards.clear()
    computer_player.all_player_cards.clear()
    
def player_wins():
    new_player.chip = new_player.chip + round_bet
def computer_wins():
    new_player.chip = new_player.chip - round_bet




while True:
## Game is on     
    new_deck = Deck()
    new_deck.shuffle()
    hand_dump()
    if new_player.chip > 0:
        game_start()
    else:
        print("Game over ya looser")
        break
    
    
    betting_in_progress = True
    while betting_in_progress == True:
    ##Correct bet    
        round_bet = int(input("How much you want to bet? "))
        if round_bet <= new_player.chip:
            betting_in_progress = False 
        else:
            print(f"Enter number smaller than your bank, your bank is {new_player.chip}")

## hit or stand 
    hit_or_stand = ""
    
    while hit_or_stand != "S":
        hit_or_stand = input("Type H for hit or S for stand: ")
        if hit_or_stand == "H":
            new_player.hit_first(new_deck.deal_one())
            new_player.countup()
            print(F" Another card is {new_player.all_player_cards[-1]} and value of your hand is: {new_player.value}")
        elif hit_or_stand == "S":
            print(f"You stand on value: {new_player.value}")
        else:
            pass
        
        if new_player.value > 21:
            print(f"Bust! Your value is: {new_player.value}")
            break
    print(f"Second card is {computer_player.all_player_cards[-1]} and his value is {computer_player.value}")
    
    
    while new_player.value < 22 and computer_player.value < new_player.value:
        
        computer_player.hit_first(new_deck.deal_one())
        computer_player.countup()
        print(f"New card is: {computer_player.all_player_cards[-1]} Dealers value is: {computer_player.value}")
        
        if computer_player.value > 21:
            print("Bust")
            break
        elif computer_player.value <= new_player.value:
            break
        else:
            continue
    
        
    if new_player.value > 21:
        computer_wins()
    elif computer_player.value > 21:
        player_wins()
    elif computer_player.value > new_player.value:
        computer_wins()
    else:
        player_wins()
        
    print(f"Round over, player has {new_player.chip} chips")
    
    want_more = input("Do you want some more Y/N")
    if want_more == "Y":
        continue
    else:
        break
    
        
    
            
    
    
    
  



