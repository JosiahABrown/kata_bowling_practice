# Kata Bowling Practice

## Task
You have <1hr to complete a program that, when given a valid sequence of rolls for one line American Ten-Pin bowling, produces the total score for the game. Use a test driven development (TDD) mindset. Create a separate test file for the program. 

**The program will not**:
- Check for valid rolls
- Check for correct number of rolls and frames
- Provide scores for intermediate frames


#### How the scoring works
- Each game, or "line" of bowling, includes 10 turns ("frames") for the bowler
- In each frame, the bowler gets two tries to knock down all the pins 
- If in two frames, the bowler fails to knock them all down, his score for that frame is the total number of pins knocked down in his two tries. 
- If he knocks them all down in two tries, thats called a "spare" and his score for the frame is ten plus the number of pins knocked down on his next turn (throw)
- If on his first try in the frame he knocks down all the pins, this is called a "strike". HIs turn is over and his score for the frame is 10 plus the simple total of the pins knocked down in his next two rolls.
- If he gets a spare or strike on his last (tenth) frame, the bowler gets to throw one or two more bonus balls. These bonus throws are taken as part of the same turn. IF the bonus throws knock down all the pins, the process does not repeat. The bonus throws ree only used to calculate the score of the file frame.
- The game score is the total of all frame scores. 


**When Scoring**:
- "X" == Strike
- "/" == Spare
- "-" == Miss