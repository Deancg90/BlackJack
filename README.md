Date: 27/03/2024

This is the first solo project, where I have written the entire project from scratch with little to no resources. 
This has been by far a great learning experience, and a great project to do to get me out of 'tutorial hell'. 
It took me around a day and a half of writing to get it into a working game.

In this project, I have learnt about:

1. Global variables, which can be used by everyone, both inside and outside the function,
I used this as after doing some basic research on how to access these variables in the to
then calculate who has won in the game, this needed to be done in the BlackJack() function.

2. The choice() method returns a randomly selected element, this was needed to have the cards chosen
to be truely random.isinstance() function, this returns True if the specified object is of the specified type.
In this case, it was to check if the card chosen is a face_card_value(str) or a card_list(int). And then i was
able to iterate and sum through both of these types of cards. This was nessaccery as i had to store the face
card values in a dictionary, it took me a while to figure this out and get the function to work. But was worth
it in the end as I haven't used dictionaries since learning about them a few months back.

Overall it was a fun project and a great learning experience. I look forward to making it better and building on 
the knowledge i have gained from writing this game. I gained alot more experience in writing functions and lots 
of if, elif and else loops, along with while loops. The future plans for this project is to add a currency system, 
also get around using global variables, as I have had advice on against using these, unless absolutely necessary.


Update: 28/03/2024

The user will now be prompted if they want to play again. I changed the BlackJack() function, to a while loop. With an input asking if the user would like to play again, this is then checked at the bottom with an if statement.

I have also added the currency feature, this was done with a simple if, elif statement within the BlackJack() function. This checks all the different scenarios and updates the players wallet accordinly. 


Update: 02/04/2024

1. Fixed a couple bugs in the code which was causing the bets to calculate incorrectly. I also added a couple more elif statements which handelled if the user busts but the computer gets under 21, resulting in the user losing the bet. 


Update: 03/04/2024

1. Added the Time library, this then slows down the computer responding to each action which is taking place. I noticed it got hard to read when it was the computers turn, so slowed down each action to 2seconds.
   time.sleep(2) was added to the dealer() function and blackjack() function above the if/elif statements.

2. Fixed a bug which stopped the user being able to bet a different amount when a round ends.

I've made the decision to stop updating this project now, its in a stable and functional state. 
My plans are to start a new project now (:
