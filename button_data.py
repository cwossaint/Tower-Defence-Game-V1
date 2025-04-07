from entities.button.menu_button import MenuButton
from entities.button.tower_select_button import TowerSelectButton
from entities.button.wave_start_button import WaveStartButton

GAMEBUTTONHEIGHT = 80
GAMEBUTTONWIDTH = 175
GAMEBUTTONSPACING = 18

GAMEGUIPANELBUTTONDATA = [
        ("Pause", "pause", MenuButton),
        ("Glue", "glue", TowerSelectButton),
        ("Boomerang", "boomerang", TowerSelectButton),
        ("Dart", "dart", TowerSelectButton),
        ("Cannon", "cannon", TowerSelectButton),
        ("Gatling", "gatling", TowerSelectButton),
        ("Start Next Wave", "start", WaveStartButton),
        ] 

TOWEREDITGUIBUTTONDATA = [
        ("Back", "back", MenuButton),
        ("Remove Tower", "remove", MenuButton),
        ("Upgrade Tower", "upgrade", MenuButton)
        ] 

MENUBUTTONHEIGHT = 125
MENUBUTTONWIDTH = 250
MENUBUTTONSPACING = 20
MENUTEXTSPACE = 75

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

