# Tower-Defence-Game-V1

### Project overview:

### Purpose
* To challenge players to strategically place, manage, and upgrade towers to defend against waves of increasingly difficult enemies that attempt to reach the end of a map.
* To learn how to implement and demonstrate OOP principles in code 
### Brief description:
* The game is based on the classic tower defence genre
* The goal is to defend against incoming waves of enemies by placing and upgrading towers that attack them while the enemies travel across the map. If enemies reach the end of the map, you lose lives. If you have no more lives left, then its game over.
### Key features:
* You can choose a variety of different maps
* There are a variety of different towers that you can place that all have unique stats as well as unqiue attributes
* There are different types of enemies that can spawn, each with different stats
* As waves continue, enemy stats scale as well as the amount of enemies and frequency of enemies per wave.
* Towers can be placed on valid tiles on the map and pre-existing towers can be selected and upgraded, increasing that tower objects stats

---
---

### Setup Instructions:
- requires at least python version 3.12.0
- must have pygame installed
- run the game from 'main.py' file

---
---

### Functional Requirements:

---

### Towers Requirements:
* Towers must be placeable on the grid by the player, only on valid tiles that are not occupied by obstacles, other towers or paths.
* Each tower type has unique base attributes, including damage, range, attack delay, cost, and potential unique attributes for specific tower types (e.g., splash damage, slow).
* Towers must be upgradable, with each level increasing their stats and requiring currency to upgrade.
* towers must create projectile objects that travel toward targeted enemies and apply damage or special effects upon collision.
* Towers must target closest enemy within its specific range

### Implementation:
* Towers are derived from a base tower class and customized in subclasses like Dart Tower, Cannon Tower, Boomerang Tower, each with unique base stats and unique attributes 
* Towers have an upgrade method which updates their stats based on a dictionary attribute containing stat values that correspond to tower levels
* Each subclass contains their own unique upgrade stats dictionary for unique stat values at different levels
* Towers have find_target() method that calculates the distance between them and enemies in order to find the closest enemy
* Towers create projectile objects that travel towards the location of the closest enemy, subtracting health from enemy if the rects for both objects collide
* Tower placement and valid placement is tracked by a 2d array that corresponds to specific maps, updating with tower placement
* Tower selection, upgrading and placement are managed by TowerEditGuiManager(manages upgrades),  GridManager(Manages placing towers on grids and selecting already placed towers) and GameGuiManager(Manages selecting towers to place)
* Tower methods and rendering is called within the gamestate class

---

### Enemies Requirements:
 * The game must spawn enemies with varying stats that can travel across the map along a path across varying maps
 *  Enemies can be targetted and damaged by towers and projectiles, dying if their health reaches 0
*  Enemies that make it across the whole map should take lives away from the player
### Implmentation:
* enemy spawning is managed by EnemyWaveManager object
* Different subclasses of enemies with varying stats (Speedy enemy variant has high speed, tanky enemy variant hass high health etc)
* PathfindingManager object calculates the path for enemies to travel for different maps, passing a list of direction corresponding to the unique path
* Enemies move across the map according to list of directions, based on their speed attribute
* If an enemy reaches the end of the path, lives corresponding to the enemies damage attribute is subtracted from the gamedata object lives attribute 

---

### Game State Requirements:
* The game must manage and track important player stats such as currency and lives throughout gameplay.
* The game must allow players to buy and upgrade towers using in-game currency, preventing purchases if insufficient funds.
* The game must spawn enemy waves that scale in difficulty over time (increasing numbers, speed, health, etc.).
* The game must detect when the player loses (runs out of lives)
* The current state of the game (e.g., playing, paused, menu) must be tracked and used to determine what logic to run and what to render.
### Implementation:
* Currency is tracked via the GameDataManager object. It includes methods for increasing money when enemies are defeated and subtracting it when towers are bought or upgraded.
* Before any tower is purchased or upgraded, a check is made to ensure the player has sufficient currency. If not, the action is denied.
* Lives are tracked in the GameDataManager. When enemies reach the end of the path, lives are reduced by an amount equal to the enemy’s damage attribute.
* The StateManager class manages the transition between different game states (e.g., from "mainmenu" to "playing", "pause", or "gameover") which each handle different aspects of the game
* If lives reach zero, the game transitions to the GameOverMenu screen using the StateManager.
* The EnemyWaveManager class handles spawning waves of enemies, and includes methods to scale amount of enemies spawned as well as frequency of enemies spawned based on wave count

---

### Grid-Based Map System Requirements:
* The game screen must be divided into a grid layout with evenly sized cells while reserving space for the side panel user interface buttons
* A range of different map scan be selected from the map select menu and must be loaded in the game accordingly
* Towers placed on the grid must be able to be selected individually
* When placing a tower, it must automatically snap to the center of the selected grid tile — not between tiles.
* The game must check whether the grid tile is valid before placing a tower. Towers cannot be placed on tiles that are already occupied
### Implementation:
* towers and objects rendered map on screen is represented by a corresponding 2D array
* 2D array contains different values for different things on the map. (0->vacant space, 1->path, 2->obstacle etc)
* Each unique map has a preset unique 2D array that is loaded in when map is chosen
* GridManager contains methods to convert screen coordinates to specific grid indexes that correspond to the 2D array to allow for selecting specific tiles while being able to click on any part of that specific tile
* GridManager checks whether the grid index for placing new tower is equal to 0 (vacant space) in order to verify valid placements
* New tower placements are updated on the 2D array by GridManager to prevent stacking of towers

---
---

### Credits and Acknowledgements
* Gameplay and tower types heavily infuenced by popular games from the tower defence genre such as Bloons Tower Defence 6
* Tower sprites are taken from Bloons Tower Defence 6
* Tower functionality heavily inspired by towers from BLoons Tower Defence 6
* ChatGPT used for adding commenting, some debugging and ideas for implementation/improvement of certain features

---
---

### Developer Retrospective:

### What went well:
* Development process rarely strayed away from original planning
* Changes from initial plan were either for minor QOL/improvement implementations or due to small bugs/oversights in original plan
* Pathfinding method for enemies was initially not planned out, however devlopment went pretty smoothly with very few bugs

### Challenges faced:
* 

### Lessons Learnt:
* Got a lot of new experience using dictionaries in code
* Learnt how to better implement OOP principles such as polymorphism and inheritance
* Got a better understanding of how to divide tasks amoungst different functions/classes and how to better arrange files within projects e.g -> splitting game functionality into different state classes.
* Learnt alot about classes and sublasses, mostly how subclasses can inherit attributes and methods as well as how certain methods can be overridden
---
---