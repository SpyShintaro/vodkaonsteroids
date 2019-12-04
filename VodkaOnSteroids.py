from random import *

# Deck Class
class Deck:
  def __init__(self, CardArray):
    self.Decksize = len(CardArray)
    self.Cardarray = CardArray
    print(" ")
    print("There are " + str(self.Decksize) + " cards in the deck")

# Troop Class
class Troop:
  def __init__(self, cardName, cardDescription, power, health):
    self.cardName = cardName
    self.cardDescription = cardDescription
    self.power = power
    self.health = health
    print(" ")
    print("The " + self.cardName)
    print(cardDescription)
    print("Power: " + str(power))
    print("HP: " + str(health))

# Spell Class
class Spell:
  def __init__(self, cardName, cardDescription):
    self.cardName = cardName
    self.cardDescription = cardDescription
    print(" ")
    print(cardName)
    print(cardDescription)

# Hand Class
class Hand:
  def __init__(self, Decklist, handList, playerType):
    self.Decklist = Decklist
    if playerType == "Player":
      print(" ")
      print("You drew:")
    for i in range(1, 6):
      cardChosen = choice(Decklist)
      hand.append(cardChosen)
      self.hand = hand
      Decklist.remove(cardChosen)
    if playerType == "Player":
      for i in hand:
        print(i.cardName)
  def discard(self, cardToDiscard):
    hand.remove(cardToDiscard)

class Field:
  def __init__(self, field):
    self.FieldSide = field

class Hell:
  def __init__(self, hell):
    self.Hell = hell
    for i in self.Hell:
      print(i.cardName)

def gameInitialize():
  print("In your deck you have:")


# Draw Function
def drawCard(CardArray, hand, field):
  cardToDraw = choice(CardArray)
  print(" ")
  print("You drew:")
  print(cardToDraw.cardName)
  hand.append(cardToDraw)
  CardArray.remove(cardToDraw)
  otherActions(CardArray, hand, playerField)

# Attack Function
def battle(attacker, defender, CardArray, handList, field):
  defender.health
  print(" ")
  print(attacker.cardName + " attacks " + defender.cardName)
  defender.health -= attacker.power
  if defender.health > 0:
    print(defender.cardName + " is now on " + str(defender.health) + " health")
  else:
    print(defender.cardName + " was killed")
  drawCard(CardArray, hand, field)

# Battle Initialiser Function
def gameplay(CardArray, handList, field):
  attacked = "false"
  print(" ")
  attacker = input("What would you like to attack with? ")
  for i in field:
    if attacker == i.cardName and i.__class__.__name__ == "Troop":
      attacked = "true"
      battle(i, bigBoiiPotat, CardArray, hand, field)
  if attacked == "false":
    print("Not a valid target")
    gameplay(CardArray, handList, field)

# Summon Function
def summon(CardArray, hand, field):
  summoned = "false"
  summonCard = input("What would you like to summon? ")
  for i in hand:
    if summonCard == i.cardName and i.__class__.__name__ == "Troop" and summoned == "false":
      summoned = "true"
      playerField.append(i)
      hand.remove(i)
    if summoned == "true":
      drawCard(CardArray, hand, field)
  else:
    print("Not a valid target")

# Actions Function
def otherActions(CardArray, hand, field):
  print(" ")
  action = input("What would you like to do? ")
  if action == "Attack":
    gameplay(CardArray, hand, field)

  if action == "Summon":
    summon(CardArray, hand, field)

  if action == "Ability":
    print("Ability")

  if action == "Hand":
    for i in hand:
      print(i.cardName)

  if action == "Field":
    for i in field:
      print(i.cardName)

  if action == "Draw":
    drawCard(CardArray, hand, field)

  else:
    otherActions(CardArray, hand, field)

# Initialise Game
gameInitialize()

hand = []
opponentHand = []

playerField = []
opponentField = []

# Card Declarations
# Troops
furret = Troop("Furret", "Doubles power when combined with Floor Fighter", 15, 20)
spedDealer = Troop("Sped Dealer", "Is the dealer of Sped", 0, 10)
bigBoiiPotat = Troop("Big Boii Potat", "The big Boii", 0, 30)
xCalibur = Troop("X CALIBUR", "[Insert Description Here]", 15, 2)
spleensTheCat = Troop("Spleens the Cat", "[Insert Description Here]", 12, 11)
tonsilsTheCat = Troop("Tonsils the Cat", "[Insert Description Here]", 5, 16)
spleensTonsilsCat = Troop("Spleens/Tonsils the Baby Cat", "[Insert Description Here]", 15, 3)
tonk = Troop("Tonk", "[Insert Description Here]", 3, 8)
bigBoiiTonk = Troop("Chonk Tonk", "[Insert Description Here]", 4, 11)
wavyBoiiTonk = Troop("Wavy Boii Tonk", "[Insert Description Here]", 6, 12)
tonkTonk = Troop("Tonk Tonk", "[Insert Description Here]", 6, 16)
sanic = Troop("Sanic", "[Insert Description Here]", 5, 9)
jetStreamRider = Troop("Jet Stream Rider", "[Insert Description Here]", 4, 9)
jetStreamRiderBot = Troop("Jet Stream Rider Bot", "[Insert Description Here]", 6, 7)
zombie = Troop("Zombie", "[Insert Description Here]", 2, 1,)
kamikazeKitten = Troop("Kamikaze Kitten", "[Insert Description Here]", 10, 1)

# Spells
floorTentacles = Spell("Floor Tentacles", "When this card is played, it can drag 3 troops to Hell")
supaVirus = Spell("Supa Virus", "When this card is played it can lower one troop's HP by 2 each turn")
laserPointer = Spell("Laser Pointer", "Defuses Kamikaze Kitten either when it goes off or when it’s on the field. Becomes an X CALIBUR when combined with a Big Boi Battery")
chernobyl = Spell("Chernobyl", "Completely wipes the entire board. User can summon one troop but then their turn is over")
trashCompactor = Spell("Trash Compactor", "Turns one card on the field into a Trash Token")

CardArray = [furret, spedDealer, spedDealer, bigBoiiPotat, bigBoiiPotat, xCalibur, xCalibur, xCalibur, spleensTheCat, spleensTheCat, tonsilsTheCat, tonsilsTheCat, spleensTonsilsCat, spleensTonsilsCat, tonk, tonk, tonk, tonk, tonk, tonk, tonk, tonk, bigBoiiTonk, bigBoiiTonk, bigBoiiTonk, bigBoiiTonk, wavyBoiiTonk, wavyBoiiTonk, wavyBoiiTonk, tonkTonk, tonkTonk, sanic, sanic, sanic, jetStreamRider, jetStreamRider, jetStreamRider, jetStreamRider, jetStreamRiderBot, jetStreamRiderBot, jetStreamRiderBot, zombie, zombie, zombie, kamikazeKitten, kamikazeKitten, floorTentacles, supaVirus, supaVirus, supaVirus, laserPointer, laserPointer, laserPointer, laserPointer, chernobyl, chernobyl, trashCompactor, trashCompactor, trashCompactor]

opponentCardArray = [furret, spedDealer, spedDealer, bigBoiiPotat, bigBoiiPotat, xCalibur, xCalibur, xCalibur, spleensTheCat, spleensTheCat, tonsilsTheCat, tonsilsTheCat, spleensTonsilsCat, spleensTonsilsCat, tonk, tonk, tonk, tonk, tonk, tonk, tonk, tonk, bigBoiiTonk, bigBoiiTonk, bigBoiiTonk, bigBoiiTonk, wavyBoiiTonk, wavyBoiiTonk, wavyBoiiTonk, tonkTonk, tonkTonk, sanic, sanic, sanic, jetStreamRider, jetStreamRider, jetStreamRider, jetStreamRider, jetStreamRiderBot, jetStreamRiderBot, jetStreamRiderBot, zombie, zombie, zombie, kamikazeKitten, kamikazeKitten, floorTentacles, supaVirus, supaVirus, supaVirus, laserPointer, laserPointer, laserPointer, laserPointer, chernobyl, chernobyl, trashCompactor, trashCompactor, trashCompactor]

playerHell = [furret]
opponentHell = [furret]

deck = Deck(CardArray)

pField = Field(playerField)

pHand = Hand(CardArray, hand, "Player")

otherActions(CardArray, hand, pField)

#battle(tonk, bigBoiiPotat)