from entities.button.menu_button import MenuButton
from entities.button.tower_select_button import TowerSelectButton
from entities.button.wave_start_button import WaveStartButton

#button dimensions

GAMEBUTTONHEIGHT = 80
GAMEBUTTONWIDTH = 175
GAMEBUTTONSPACING = 18

MENUBUTTONHEIGHT = 125
MENUBUTTONWIDTH = 250
MENUBUTTONSPACING = 20
MENUTEXTSPACE = 75


#button object data -> DISPLAY TEXT, OUTPUT, BUTTON CLASS

GAMEGUIPANELBUTTONDATA = [
        ("Pause", "pause", MenuButton),
        ("Glue: $25", "glue", TowerSelectButton),
        ("Boomerang: $25", "boomerang", TowerSelectButton),
        ("Dart: $25", "dart", TowerSelectButton),
        ("Cannon: $70", "cannon", TowerSelectButton),
        ("Gatling: $110", "gatling", TowerSelectButton),
        ("Start Next Wave", "start", WaveStartButton),
        ] 

TOWEREDITGUIBUTTONDATA = [
        ("Back", "back", MenuButton),
        ("Remove Tower", "remove", MenuButton),
        ("Upgrade Tower", "upgrade", MenuButton)
        ] 

MAINMENUBUTTONDATA = [
    ("Play", "mapselect"),
    ("Options", "options"),
    ("Quit Game", "quit")
]

PAUSEMENUBUTTONDATA = [
    ("Resume", "playing"),
    ("Back to Main Menu", "mainmenu")
]

GAMEOVERMENUDATA = [
    ("Back to Main Menu", "mainmenu")
]

OPTIONSMENUDATA = [
    ("Back to Main Menu", "mainmenu"),
    ("Quit game", "quit")
]

MAPSELECTMENUBUTTONDATA = [
    ("Map 1", "map1"),
    ("Map 2", "map2"), 
    ("Map 3", "map3"),
    ("Back to Main Menu", "mainmenu")
]

