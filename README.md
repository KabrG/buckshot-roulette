# buckshot-roulette
Buckshot Roulette Game + Computer AI (Classical)

A terminal implementation of the popular Steam game "Buckshot Roulette" by Mike Klubnika. The purpose of the project is to implement an AI that would make the best move given all the information provided. 

## AI Implementation
The programmer is responsible for designing a ```make_move()``` function that will be continously called until the AI's turn has passed. ```make_move()``` takes two classes as parameters: ```Action``` and ```GameInfo```. 

### GameInfo
```GameInfo``` is used to obtain relevent game state information. Below is a short description of each attribute accessible to the programmer. 

| Attribute       | Description |
|-----------------|-----------------|
| ```shell_list: list```  | Percieved shell list for the current round, where 0, 1, 2 represnts dud, live, and unknown shells respectively.| 
| ```shell_index: int``` | Index represents current shell chambered in the shotgun. For example, if `shell_index` is 0, the first shell in shell_list will be fired next. | 
| ```num_live: int``` ```num_dud: int``` | The number of live and dud rounds announced at the beginning of the round.| 
| ```my_health: int``` ```opponent_health: int``` | Health of both players respectively.| 
| ```my_items: list``` ```opponent_items: list``` | Item list of both players respectively.| 
| ```my_damage: int``` ```opponent_damage: int``` | The amount of damage player or their opponent can deal in the next shot. Note, ```opponent_damage``` will always be visibly 1.| 
| ```max_health: int```| Max health either player can reach this game. This is important when consuming cigarettes as you can not exceed ```max_health```.| 
| ```turn: bool```|Returns if it is player's turn (always give ```True``` since ```make_move()``` is called only on your turn).| 
| ```my_cuffed: bool``` ```opponent_cuffed: bool``` | Returns the status of players being cuffed. ```my_cuffed``` will always appear ```False```.| 
| ```cuff_ban: bool```|Returns if the player is alloed to place cuffs on their opponent. This is used to prevent consecutive cuffing..| 


### Action
```Action``` is used to perform a move (such as shooting or using a powerup). Below is the list methods that can be used.
* ```shoot_self()```
* ```shoot_opponent()```
* ```use_cigarette()```
* ```use_pills()```
* ```use_beer()```
* ```use_cell_phone()```
* ```use_handsaw()```
* ```use_magnifying_glass()```
* ```use_inverter()```
* ```use_cuffs()```
* ```use_injection(steal_item)```, where ```steal_item``` is a string of the item to steal

For example, calling ```action.use_handsaw()``` followed by ```action.shoot_opponent()``` will deal 2 damage if the shell is loaded. 

**It is the programmer's responsibility to ensure that the actions methods are called correctly**. For example they may not call ```use_cell_phone()``` unless they have a cell phone in their inventory. 

### All Item Names
The list of all avaliable items: ["cigarette", "cell_phone", "magnifying_glass", "cuffs", "inverter", "injection", "beer", "handsaw", "pills"] 

## Extra
If you'd like to run the game with a simple command in the terminal, use an alias. For example,
```
alias buckshot='<ABSOLUTE_PATH_TO_REPO>/.venv/bin/python3.11 <ABSOLUTE_PATH_TO_REPO>/game.py'
```
lets you run the program by typing `buckshot` in terminal. Add this line into `~/.bashrc`.

