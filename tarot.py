import random

def display_intro():
    print("||||||||||Tarot||||||||||")
    print("||||||||||Cards||||||||||")


tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 
         4:	"The Emperor", 5:	"The Hierophant", 
         6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 
         9:	"The Hermit", 10:	"Wheel of Fortune",  
         11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 
         14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 
         17:	"The Star", 18:	"The Moon", 19:	"The Sun", 
         20:	"Judgement", 21:	"The World", 22: "The Fool"
        }
tarot_meanings = {1:	"The magician represents freedom. A magician seeks to bring forth the divine gold within her or himself", 
         2:	"The high priestess represents the need to prioritize your intuition, rathern than intellectual mind", 
         3:	"The empress represents femininity, fertility, creativity, and nurtering. Above all, it is a signal to be kind to oneself", 
         4:	"The emperor represents authority, regulation, and organization. Act rationally in times of crisis.", 
         5:	"The hierophant represents conventionalism and a wanting for traditionalism over innovation", 
         6:	"The lovers represents harmony, attractiveness, and perfection within relationships, which are usually close and intimate.", 
         7:	"The chariot represents overcoming challenges and gaining victory through control of one's surroundings. Strength and willpower are critical in overcoming the obstacles in your path.", 
         8:	"Strength represents resilience and willpower in times of immense struggle. Compassion, even at one's own expense, can be interpreted as well", 
         9:	"The Hermit represents a lonely wanderer, seeking knowledge from within-the inner voice. They must disconnect from society to achieve their goals.", 
         10: "Wheel of fortune represents the cycle of good and bad times that we all experience, even if out of our control",  
         11: "Justice represents the judgments of life, from oneself and others. Justice signals that judgments will be made fairly.", 
         12: "The hanged man represents a need to suspend certain action. Postponing decisions may be best to furthur reflect", 
         13: "Death represents the ending of one phase if your life and the begining of the next. Place the past behind you to focus yourself on what's ahead", 
         14: "Temperance represents one with clear vision ahead, calmness in times of distress, and the ability to work in harmony with your community, coworkers, and your loved ones", 
         15: "The devil represents feelings of emptiness and a lack of fulfullment in your life.", 
         16: "The tower represents change in it's strongest and most chaotic sense.", 
         17: "The star represents hope, renewed power, and the strength to carry on in life.", 
         18: "The moon represents a dark path that you are unsure of. The light of the moon.", 
         19: "The sun represents success, abundance and radiance. Joy, happiness, and good times are coming to you.", 
         20: "Judgement represents reflection and clear evaluation of ourselves and our actions.", 
         21: "The world represents great unity and wholeness. Inner and outter worlds become one.", 
         22: "The fool represents innocence, beginings, and optimism. Anything can happen and life is waiting to be explored."
         }

#card = random.choice(list(tarot.keys()))

def card_grab(card):
    print(tarot.get(card))

def meaning_grab(card):
    print(tarot_meanings.get(card))



def draw_cards():
    drawn_cards = []
    input("Press enter to draw your past card: ")
    past_card = random.choice(list(tarot.keys()))
    drawn_cards.append(past_card)
    card_grab(past_card)
    meaning_grab(past_card)

    input("\nPress enter to draw your present card: ")
    present_card = random.choice([card for card in tarot.keys() if card not in drawn_cards])
    drawn_cards.append(present_card)
    card_grab(present_card)
    meaning_grab(present_card)

    input("\nPress enter to draw your future card: ")
    future_card = random.choice([card for card in tarot.keys() if card not in drawn_cards])
    drawn_cards.append(future_card)
    card_grab(future_card)
    meaning_grab(future_card)

display_intro()
while True:
    draw_cards()
    another_reading = input("\nWould you like another reading? (yes/no): ").strip().lower()
    if another_reading != "yes":
        print("Goodbye and goodluck")
        break

#offer another reading