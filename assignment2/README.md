Clone the repo
```
git clone https://github.com/ddyt0113/assignment
```

Update the repo
```
git pull
```

Install requirements
```
cd assignment2
pip install -r requirements.txt
```

Overview
```
The Aircraft Game is a simple Python-based game created using Pygame. 
Players must locate and "hit" aircraft on a grid by clicking on the cells. 
The objective is to find all the aircraft nose.
```
chessboard
```
The board consists of 10*10 grey squares.
```
aircraft
```
The shape of the aircraft is shown below, the nose is red and the rest is blue.
    x         <- aircraft nose
x x x x x     <- wing
    x         <- body
  x x x       <- tail
  
Aircrafts are randomly generated on the chessboard.
```

How to play
```
1. Run the game
2. Enter the number of aircraft you want to play with (must be between 1 and 3).
3. Click on the grid cells to find the aircraft. Try to deduce the position of the nose from the structure of the aircraft.
4. Each successful hit on an aircraft will increase your score by 1.
5. You win the game when you successfully find all the aircraft nose.
```
Try to complete the game with the least number of clicks.
Have fun! XD