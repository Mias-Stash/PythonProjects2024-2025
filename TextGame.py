#import stuff
import time 
import random
#/////////////////////////////////////////////////////////////////////////////////////
    #decision loop 
    #!!! RE-USE THIS CODE FOR EVERY DECISION!!!
    #PlayerChoice= int()
    #while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        #PlayerChoice= int(input())
        #if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            #print("Invalid choice! Try again.")
        #else:
            #break
    #if PlayerChoice == 1:
        #print("1")
    #elif PlayerChoice == 2:
        #print("2")
    #else:
        #print("3")
#make sure to add return conditions as needed :) also if there's more than 3 options just add: and PlayerChoice != 4: etc.
#//////////////////////////////////////////////////////////////////////////////////
    #print('''Choose option 1-3:
    #1. ONE
    #2. TWO
    #3. THREE''')
#decision loop. 
    #PlayerChoice= int()
    #while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        #PlayerChoice= int(input())
        #if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            #print("Invalid choice! Try again.")
        #elif PlayerChoice == 3:
            ##insert chat dialogue
            #print('''THIS IS CHAT DIALOGUE''')
            #print()
            #time.sleep(2)
            #print('''Choose option 1-2:
            #1. ONE
            #2. TWO''')
            #while PlayerChoice != 1 and PlayerChoice != 2:
                #PlayerChoice= int(input())
                #if PlayerChoice == 3:
                    #print("Invalid choice! Try again.")
        #else:
            #break
    #if PlayerChoice == 1:
        #print("1")
        #return PlayerChoice
    #else:
        #print("2")
        #return PlayerChoice
#///////////////////////////////////////////////////////////////////////////////////
#define functions here
#intro crawl
def IntroCrawl():
    print('''The entry to the docks is bustling with activity. 
    Ships from all quadrants are gathered here for port, with many luxury vessels parked nearby the target- 
    Mrs. Bella’s Traveling Casino. 
    The massive liner towers overhead, twenty stories of debauchery, gambling, and poor decisions, 
    all spearheaded by one of the most bloodthirsty and ruthless matriarchs this side of The Twins.''')
    time.sleep(5)
    print()
    print('''You are Derek, a bounty hunter on good days and a thief for hire on most. 
    Your skill in this field is, unfortunately, unmatched. Dangerous jobs like this seem to push and pull you like the tides.
    Well, at least they pay very handsomely.''')
    print()
    print('''Gou Ya, your boss, approaches you from amidst a concealing crowd. 
    He hands you an envelope and waves you to step away from the bustle for a moment. 
    As you move, he speaks to you.''')
    print()
    time.sleep(5)
    print('''“Alright, you know as well as I do that this won’t be an easy snatch. 
    I’ll give you the rundown, but that’s all I can afford to do. ” 
    He rummages in his shirt pocket for a cigarette and lights it quickly, blowing acrid smoke in your direction.''')
    print('''“There’s a few routes you can take to get to the package, I recommend something a little out of the way, 
    but I know you wouldn’t follow an order without a pricetag, so do what ya’ will.” He shrugs, taking another puff. 
    “You’ll take the thumbdrive in that envelope, stick it into the computer in the back room with all the goods, 
    and it’ll unlock the safe I want you to get into.”''')
    print()
    time.sleep(5)
    print('''Choose option 1-3:
    1. "And after that?"
    2. "Got it. The thumbdrive."
    3. Call for advice?''')
    #decision loop 
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print('''Gou waves his hand dismissively, clearing the air a little from his smoke. “Ehh, take ship… Three I think. Yeah, three. 
My guys on board set it up to be ready to go once you need to dip.” He pats your shoulder. 
“Alright, get on that ship. Thing’s departing in ten minutes, and I needed you on it three minutes ago.”''')
        print()
    elif PlayerChoice == 2:
        print('''“Attaboy.” He pats your shoulder. “Alright, go get on that ship. Thing’s departing in ten minutes.”''')
        print()
    else:
        print('''The transceiver in your ear springs to life with a hissing static. On the other end you hear two familiar voices. 

        “Now what are you calling us about, man? Just go on the ship!” Pyrin shouts into the microphone. 

        “Hey, don’t get on his case already!” June cuts him off. “Look, if you need any help with anything give us a ping, we’ll see what we can do.” 

        “Don’t encourage the guy to bother us all day! I’ve got important-”

        “Alright, thats enough!” June cuts him off yet again and their transmission ends with a loud *KSSHT!*''')
        print()
        time.sleep(4)

#ship entrance
def FoyerIntro():
    print('''The entrance hall is massive, towering nearly higher than you can crane your head up to see. Brass band jazz flits in to your ears from a distant place on the top floor of the foyer. 
Rich couples, groups, and singles mingle and gamble on the first few floors. 
You feel a bit out of place with your street clothes.''')
    time.sleep(2)
    print('''A particular masked couple passes you by, one leaning over to say; “You shouldn’t be here.”''')
    time.sleep(2)
    print('''How rude!''')
    print()
    time.sleep(1)
    print('''Choose option 1-2:
    1. Continue
    2. Call for advice''')
    #decision loop
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2:
            print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print("You push forward...")
        time.sleep(2)
    else:
        print('''KSSHT! 

“Go and punch him!” Pyrin yells into your ear.

“No, no, no!” June shouts over him. “Focus on the package! I’m not going to encourage you to get into a stupid scrap for no reason!”

“He’d be fine! Right, Derek?”

    They don’t seem to be very focused…''')
        time.sleep(2)
        print('''You push forward...''')

#route branching
def FoyerDecision():
    print('''You make it past the main entrance onto the casino floor. People are hunched in front of slot machines and over small-bets tables. 
The first floor has always been a bit lackluster, but you aren’t here to do sightseeing.
It’s time to decide your route, will you…''')
    print()
    time.sleep(3)
    print('''Choose option 1-3:
    1. Go overt! No one suspects what's hidden in plain sight!
    2. Go sneaky, better safe than sorry!
    3. Call for advice''')
    #decision loop. 
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            #insert chat dialogue
            print('''KSSHT!

“Hmm…” June trails in and out.

“Guns blazing, dude!” Pyrin says. 

“No, no, Pyrin. I think maybe going in quieter is the best option here.”

“You’re never any fun, you know that?” He pouts. 

“I’m just trying to look out for him!” She cries. 

“Well *I* think he’s got this handled. Derek! Follow your heart or something, man!”
                  
    How inspiring...''')
            print()
            time.sleep(3)
            print('''Choose option 1-2:
            1. Go overt! No one suspects what's hidden in plain sight!
            2. Go sneaky, better safe than sorry!''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print("Overt it is!")
        return PlayerChoice
    else:
        print("Sneaky it is!")
        return PlayerChoice
#--------------------------------------------
#OVERT route functions
def SecurityGuards():
    print('''Two burly men stand in front of the back exit of the casino floor. 
You eye them as you pace between machines, trying not to look suspicious…''')
    print('''Choose option 1-3:
    1. Talk it out!
    2. Knock em’ out!
    3. Ask for advice''')
#decision loop
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            print('''“Wh- what are you calling us for?!” June exclaims. “Just- just get out of there!”

“PUNCH EM’!!!” Pyrin shouts.''')
            print()
            time.sleep(2)
            print('''Choose option 1-2:
            1. Talk it out!
            2. Knock em’ out!''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print('''You approach the two guards with a smile and a wave. 
They look down at you in annoyance. 
Before you can try to smooth talk through them, the one on the left speaks up…''')
        time.sleep(2)
        print('''“Hey, wait… I recognize you! You’re the Green Blur!” He slaps the chest of the other guard. 
“Jim, help me wrangle this guy before he tries to do any funny business!”
Maybe the social route wasn’t the best idea…''')
        #CALL GAMEOVER FUNCTION
        return 1

    else:
        print('''On instinct, you charge towards them and land a punch square on the jaw of one of the guards!''') 
        time.sleep(1)
        print('''He stumbles backward, then falls down, knocked out! What a lucky punch!
              The other guard scrambles to reach for his radio…''')
        time.sleep(2)
        print('''But you bat it away and punch him in the same spot!''')
        time.sleep(1)
        print('''He falls down the same way as his coworker, and you dart past them!''')
        return 2

def Hallway():
    print('''You blaze past the guards, hopefully they didn’t set off any alarms as you made your way… away. 
In front of you, the path forks!''')
    print('''Choose option 1-3:
    1. Go left!
    2. Go right!
    3. Ask for advice''')
#decision loop. 
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            #insert chat dialogue
            print('''KSSHT!

“Uhh, left.” Pyrin says

“No, right!” June replies. 

“I think left is luckier.”

“Well you’re *wrong.*” 

“*I’m* wrong?!”

“Yeah! You-”

They don’t seem to be of much help… Better get a move on!''')
            print()
            time.sleep(3)
            print('''Choose option 1-2:
            1. Go left!
            2. Go right!''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print("Veering left, you push forward…")
        return 1
    else:
        print("Right! Right is always right! You veer thataway and…")
        time.sleep(2)
        print('''Are met with a hallway full of guards. Looks like word of intruders passes around pretty quickly on this ship…
Seems you won’t be making it out of a scrape this big!''')
        #CALL GAMEOVER FUNCTION
        return 2


def MotionDetectors():
    print('''Further down the hallway, you see the tell-tale sign of high-security. Red lasers in seemingly random patterns slice across the hallway in front of you. 
To your left there seems to be a control panel.
You don’t know how much time you have… ''')
    print('''Choose option 1-3:
    1. Hack the system!
    2. Duck and roll!
    3. Ask for advice''')
#decision loop.
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            #insert chat dialogue
            print('''KSSHT!

“KAL tech slicer systems?” Pyrin groans into the transceiver. “Just plug into the wall controls over there and I’ll have it down in thirty seconds.”

“Well aren’t you handy!” June chimes.

“*I* helped develop these. There’s a backdoor I put into their- whatever. Derek, just plug me in.”''')
            print()
            time.sleep(3)
            print('''Choose option 1-2:
            1. Hack the system!
            2. Duck and roll!''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print("You unplug your transceiver from your ear and plug it into a port on the wall controller to your left. Pyrin’s voice rings from its small speaker.")
        time.sleep(2)
        print('''“Alright, sending the shut-off… now.”''')
        time.sleep(2)
        print("The lasers power down, then you unplug from the controller, and forge onwards into the back room.")
        return 1
    else:
        print('''Good idea! You’re in pretty good shape. 
You walk back a few paces and shake out any inhibitions, then charge forward!''')
        time.sleep(2)
        print('''Unfortunately, the spaces between the lasers were a bit smaller than you initially thought- oh, and did I mention they weren’t motion detectors…? ''')
        time.sleep(2)
        print("It seems they cut quite cleanly, though!")
        #CALL GAMEOVER FUNCTION
        return 2


#--------------------------------------------
#SNEAKY route functions

def TheCloset():
    print('''You decide to go more covert. After scanning the area a bit while meandering around the slot machines, you watch a janitor exit a closet on the far left wall. 
You mosey your way over to the closet, 
pretending to gauge the luck of each slot machine you walk past to not attract suspicion.''')
    time.sleep(2)
    print('''You look left and right, then quickly open the door to and duck inside the closet.
Inside, there is various cleaning supplies, and a vent in the back. It looks small enough to squeeze through?''')
    print('''Choose option 1-3:
    1. Wait for the floor to close, then find a route through the casino
    2. Go unseen through the vent
    3. Ask for advice''')
#decision loop.
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            #insert chat dialogue
            print('''KSSHT!

“Oh, definitely hide in the closet!” June chimes. “You’ll be out of sight, we might even be able to hack the cameras from here!”

“What?!” Pyrin pipes up. “There’s no way I’d be able to do that!”

“I thought you were a genius!”

“Well I *am*, but that’s not related to this!” He cries. “Mrs. Bella has top of the line security, I’d need *days* to access her systems!”

“Well-” June sounds annoyed, “it might be best to use the closet anyway, stay out of sight, y’know?”

Pyrin sighs. “Yeah, be real sneaky about it.”''')
            print()
            time.sleep(4)
            print('''Choose option 1-2:
            1. Wait for the floor to close, then find a route through the casino
            2. Go unseen through the vent''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print("Of course! What’s more sneaky than a nighttime thief slinking through a heavily guarded casino?!")
        time.sleep(1)
        print("That’s what I *would* say, if you weren’t hiding in a janitor’s closet.")
        time.sleep(2)
        print("The janitor comes back to get a mop after about five minutes.")
        time.sleep(2)
        print("And you’re carted off by security thirty seconds after that.")
        #CALL GAMEOVER FUNCTION
        return 1

    else:
        print('''Maybe pushing forward is your best option here. You check the corners of the vent and find standard screws holding it in place.
A little strange, considering the security elsewhere on the ship, but you brush it off.''')
        time.sleep(2)
        print("You take out your multi-tool and unscrew the vent cover as quietly and quickly as you can. ")
        time.sleep(1)
        print("You shimmy inside, and continue on…")
        return 2

def Vents():
    print('''Getting into the vent was a bit of a tight squeeze, but in the ducts there’s a little more room to breathe. 
    Granted, you’re stuck in a belly crawl, but it’s better than that closet. You push forward…''')
    time.sleep(2)
    print('''You come to a split path in the ducts. To your left, it plunges downward further than you can really see. To your right, the duct slopes upward, 
there is a faint glow. You feel a breeze from both directions.
You…''')
    print('''Choose option 1-3:
    1. Go down
    2. Go up
    3. Ask for advice''')
#decision loop. 
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            #insert chat dialogue
            print('''KSSHT!

“Follow the light!” June says. 

“Never know what might be waiting for you in the dark, though!” Pyrin interjects.

“You’re looking for a *computer*.” She says, annoyed. “Why would you go somewhere darker?”''')
            time.sleep(2)
            print()
            print('''“Well,” Pyrin trails off, “I keep my screen rooms dark… Or maybe the screens are turned off… You never know…” He sounds a little defeated. 

“Like I said, the light. Go there.”''')
            print()
            time.sleep(2)
            print('''Choose option 1-2:
            1. Go down
            2. Go up''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print("You decide to go left and down. What’s a little plunge into the unknown?")
        time.sleep(2)
        print("You fall down…")
        time.sleep(3)
        print("And down…")
        time.sleep(4)
        print("And down…")
        time.sleep(4)
        print("Right out the air chute…")
        #CALL GAMEOVER FUNCTION
        return 1

    else:
        print("You follow your gut and decide to go right and up.")
        return 2


def BackRoom():
    print('''After clambering through more ducts than you thought was really necessary, 
          you hear the sound of people talking. Based on your map, you should be nearing the back room…''')
    time.sleep(2)
    print('''Ahead, you see a faint glow against the right wall, as you approach, the sound of people talking gets louder. 
You adjust your crawl to be quieter with each inch. A vent leading into the back room on your left side comes into your view. 
Peeking through the grating, you see two guards chatting to each other. 
          
“You see the footage of the crazy guy on the main floor earlier?” One says

“No, you’re on your phone too much.” Says the other. “Did Eddie send you that one?”

“No, no, Mrs. Bella herself sent it to all employees. Apparently we need to be on the lookout for this guy.” The first guard clarifies. “You should check your phone more, man.”

The other guard leans over the look at the first’s phone. “Looks scrawny.”

The first guard laughs. “We could take him no problem.”''')
    time.sleep(4)
    print("What a bruise to your ego! You’ve been working out for years! You should…")
    print('''Choose option 1-3:
    1. Distract the guards
    2. Attack the guards!
    3. Ask for advice''')
#decision loop. 
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            #insert chat dialogue
            print('''KSSHT!

“If you don’t punch someone today I’m gonna throw all of your stuff out the airlock.” Pyrin sounds annoyed. 

“Are you stupid?!” June cuts him off. “Derek, get their attention elsewhere. 
Those vents lead through the whole ship- I’m sure you can find a distraction in a nearby room.”''')
            print()
            time.sleep(3)
            print('''Choose option 1-2:
            1. Distract the guards
            2. Attack the guards!''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print('''Better safe than sorry… 
You shimmy further into the vents into a room further down the hall. 
Thinking quickly, you unscrew the vent cover leading in and toss it into the room, then shimmy back from whence you came.''') 
        time.sleep(2)
        print("The guards are gone! Now’s your chance!")
        return 1

    else:
        print("You leap out of the vent and onto one of the guards! You struggle against him…")
        time.sleep(2)
        print("As valiantly as you fought, you forgot that these guys were armed…")
        #CALL GAMEOVER FUNCTION
        return 2


#--------------------------------------------
#routes converge here
def RouteConverge():
    print('''You’ve made it into the back room. It’s dingy and dim, but the walls are lined with red velvet. 
On the far side, a computer sits unattended, and to its left are an array of safes. 
You take out the thumb drive Gou gave you earlier, and insert it into the computer...''')
    time.sleep(2)
    print("You feel sweat run down your neck…")
    time.sleep(2)
    print('''The screen flashes, and a light on the thumb drive glows an inviting shade of green. 
A safe numbered 13 unlatches and pops open, inside is a small wrapped package. 
You pick it out and close the door slowly. It feels a bit heavy for its size, but you stuff it into your pocket.''')
    time.sleep(2)
    print('''*KSSHT!* June’s voice breaks your victorious silence. “You got the package? Good! 
That computer should have a ten second grace period before it sets off the alarm. Get out of there!”''')
    time.sleep(2)
    print('''You burst through the door into the hallway, from here you can try to escape by…''')
    print('''Choose option 1-3:
    1. Going back the way you came! You don’t know what’s ahead!
    2. Go deeper! There should be escape ships somewhere here!
    3. Ask for advice''')
#decision loop. 
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 3:
            #insert chat dialogue
            print('''KSSHT!

“Keep going, man!” Pyrin eggs you on. 

“We don’t have a map, Derek!” June says exasperatedly. “Follow your intuition!”''')
            print()
            time.sleep(2)
            print('''Choose option 1-2:
            1. Going back the way you came! You don’t know what’s ahead!
            2. Go deeper! There should be escape ships somewhere here!''')
            while PlayerChoice != 1 and PlayerChoice != 2:
                PlayerChoice= int(input())
                if PlayerChoice == 3:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print('''Maybe turning around *would* be best.
You look behind yourself and note how clear the coast is, on account of everything you’ve already done.''')
        time.sleep(1)
        print("Surely there hasn’t been enough time for Mrs. Bella’s guards to filter back into the spaces you left behind, right?")
        time.sleep(2)
        print("Sorry to tell you, but…")
        time.sleep(2)
        print("Wrong!")
        #CALL GAMEOVER FUNCTION
        return 1

    else:
        print("You decide to push onwards, to hell with the odds!")
        time.sleep(2)
        print("You run past room after room, and the alarm June warned you of starts to blare!")
        time.sleep(2)
        print('''“ATTENTION ALL GUARDS!” A shrill voice shrieks over intercom speakers on the walls. 
“AN INTRUDER HAS BEEN SPOTTED ON FLOOR THREE!” It’s the voice of Mrs. Bella herself! Why does she have this much free time?
“ALL ACTIVE UNITE MOBILIZE!”''') 
        print("You cross your fingers and take a right down a dark hallway…")
        return 2


#final stretch functions. four possible options this time
def EndGame(): 
    print('''You finally reach the docks. Its a massive room and there are more vessels than you can count, 
but you remember Gou telling you to take…''')
    print('''Choose option 1-3:
    1. Ship 1! It looks fast!
    2. Ship 2! It looks lucky!
    3. Ship 3! It looks sturdy!
    4. Ask for advice''')
#decision loop. trying to get it to "delete" the fourth option, then ask again, if the player selects it
    PlayerChoice= int()
    while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3 and PlayerChoice != 4:
        PlayerChoice= int(input())
        if PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3 and PlayerChoice != 4:
            print("Invalid choice! Try again.")
        elif PlayerChoice == 4:
            #insert chat dialogue
            print('''KSSHT!

Pyrin’s voice rings loud and annoyed in your ear. 

“I knew i should’ve sent one of my own ships there! Ugh!”

“*Your* ships all have stupid faces spray painted onto them! We’re trying to be subtle here! You’d be spotted from a light year away in that thing!” 

“*My* ships are fast and well-made enough to warrant decor! Derek! I can send one for you right now!”

Now doesn’t seem like a good time… The alarm blares louder in your ear now, and a voice shrieks over the intercom.''')
            time.sleep(3)
            print('''“FLOOR SEVEN! INTRUDER LOCATED ON THE ESCAPE DOCKS! ALL UNITS MOBILIZE!” 

“Was that Mrs. Bella?!” June panics into the speaker. 

“Go for ship two!” Pyrin shouts over her. “Wait, no, ship three!”

“No, no! Ship one! You’ve gotta get out of there!”''')
            time.sleep(3)
            print("They don’t seem to be of much help… Better choose fast!")
            print()
            time.sleep(2)
            print('''Choose option 1-3:
            1. Ship 1! It looks fast!
            2. Ship 2! It looks lucky!
            3. Ship 3! It looks sturdy!''')
            while PlayerChoice != 1 and PlayerChoice != 2 and PlayerChoice != 3:
                PlayerChoice= int(input())
                if PlayerChoice == 4:
                    print("Invalid choice! Try again.")
        else:
            break
    if PlayerChoice == 1:
        print('''Better go fast! This ship looks sleek and glossy. You run towards it and realize…''')
        time.sleep(2)
        print('''You can’t find the entrance. Just then, Mrs. Bella’s guards burst into the docks and… 
Well, I suppose the rest is up to your imagination…''')
        #CALL GAMEOVER FUNCTION
        return 1

    elif PlayerChoice == 2:
        print("Ship two it is! A pair of fuzzy dice swing in the mirror of the cockpit. Maybe luck will be on your side for once today?")
        time.sleep(2)
        print('''You enter the ship and find your way into the cockpit, but it looks like this ship was made to be piloted by someone with *way* more than two arms. 
    A big red button blinks in front of you in the middle of the dashboard…''')
        time.sleep(2)
        print('''Choose option 1-2:
            1. Push it...?
            2. Don't even think about it!''')
        PlayerChoice == 0
        PlayerChoice = int(input())
        if PlayerChoice == 1:
            print('''You cross your fingers, close your eyes, and slam your hand on the button!''')
            time.sleep(1)
            print('''A cheery voice rings through the ship in a language you don’t know, something rattles, and then…''')
            time.sleep(2)
            print('''KABOOM!''')
            #CALL GAMEOVER FUNCTION
            return 1

        else:
            print('''Your hand hovers over the big red button as it blinks. You decide to think better of it, but what now?! The guards- oh. ''')
            time.sleep(2)
            print('''Well, it seems you have company, and a *lot* of explaining to do.''')
            #CALL GAMEOVER FUNCTION
            return 2


    else:
        print('''Ship three… Ship three- Ship three! That was it! You run towards it, and its loading dock opens to greet you. 
You’ve never felt more grateful to enter the back end of a hauler! ''')
        time.sleep(2)
        print("The dock closes behind you before any of the guards on your trail filter in, and just as you hear them shouting, the ship rumbles to life!")
        time.sleep(2)
        print("You get thrown around a bit, but you feel the thrusters kick in, and with a start, you’ve made it out!")
        return 3


def TheEnd():
    print('''Package safely tucked away, you run to the front of the ship. Autopilot got you out of the docks, but the way back to safety is up to you-
Luckily, you’re known for your sense of direction!''')
    time.sleep(2)
    print('''You duck and weave the unwieldy ship between debris and trailer ships, moving erratically to get Mrs. Bella’s fleet off of your tail…''')
    time.sleep(2)
    print('''After white-knuckling the steering wheel for what felt like hours, you finally feel safe enough to engage warp…''')
    time.sleep(2)
    print('''You’re back at the loading docks, where Gou Ya, your ship, Pyrin, and June are waiting!''')
    time.sleep(2)
    print('''Congratulations, you win!''')

def GameOver():
    print("Do you want to play again? (Type Yes or No)")
    return input().lower().startswith("y")

def RandomGameOverText():
    gameovertxt=['''Ms. Bella’s shrieking voice cuts over the speakers…

“Next time, maybe you should plan ahead a little better!”
~~~~~~~~~~
GAME OVER
''', '''Well, I’m sure you’ll have plenty of time to figure out what to do next… erm… if you’re not dead, that is. 
~~~~~~~~~~
GAME OVER
''','''“slippery little guy, not anymore!.” A guard says as you’re carried off towards the airlock…
~~~~~~~~~~
GAME OVER
''', '''KSSHT!

“Derek?”

“Derek!”

“DEREK…!!!”

~~~~~~~~~~
GAME OVER
''']
    chosentext= random.choice(gameovertxt)
    time.sleep(4)
    print()
    print(chosentext)
    
#main
def main(): 
    #declaring variables
    PlayAgain= str()
    PlayAgain= True
    RestartGame= False
    RouteChoice= int()
    #game loop
    while PlayAgain == True:
        #playagain loop
        while RestartGame == False:
            IntroCrawl()
            FoyerIntro()
            #path branches
            RouteChoice= FoyerDecision()
            if RouteChoice == 1:
                SecurityCheck=SecurityGuards()
                if SecurityCheck== 1:
                    RandomGameOverText()
                    break
                HallwayCheck=Hallway()
                if HallwayCheck== 2:
                    RandomGameOverText()
                    break
                MotionCheck=MotionDetectors()
                if MotionCheck== 2:
                    RandomGameOverText()
                    break 
            else:
                ClosetCheck=TheCloset()
                if ClosetCheck== 1:
                    RandomGameOverText()
                    break
                VentCheck=Vents()
                if VentCheck== 1:
                    RandomGameOverText()
                    break
                BackCheck=BackRoom()
                if BackCheck==2:
                    RandomGameOverText()
                    break
            #paths converge
            ConvergeCheck=RouteConverge()
            if ConvergeCheck==1:
                RandomGameOverText()
                break
            End1=EndGame()
            if End1== 1 and End1== 2:
                RandomGameOverText()
                break
            TheEnd()
        #play again?
        PlayAgain= GameOver()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#call main here
main()
print("Thank you for playing!")