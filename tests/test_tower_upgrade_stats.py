import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entities.tower.boomerang_tower_class import Boomerang
from entities.tower.dart_tower_class import Dart
from entities.tower.cannon_tower_class import Cannon
from entities.tower.gatling_tower_class import Gatling
from entities.tower.glue_tower_class import Glue

@pytest.mark.parametrize("TowerClass, level1_expected, level2_expected", [
    (
        Boomerang, 
        {"damage": 7, "range": 250, "attack delay": 50, "pierce": 5, "cost": 25},
        {"damage": 12, "range": 300, "attack delay": 45, "pierce": 7, "cost": 50},
    ),
    (
        Cannon,
        {"damage": 80, "range": 175, "attack delay": 100, "cost": 70, "splash damage": 35, "splash range": 125},
        {"damage": 95, "range": 200, "attack delay": 95, "cost": 75, "splash damage": 45, "splash range": 150},
    ),
    (
        Dart,
        {"damage": 15, "range": 150, "attack delay": 25, "cost": 25},
        {"damage": 18, "range": 175, "attack delay": 23, "cost": 35},
    ),
    (
        Gatling,
        {"damage": 3, "range": 250, "attack delay": 5, "cost": 110},
        {"damage": 3.5, "range": 325, "attack delay": 4.5, "cost": 80},
    ),
    (
        Glue,
        {"slow": 0.5, "range": 150, "attack delay": 70, "slow duration": 180, "splash range": 80, "cost": 25},
        {"slow": 0.6, "range": 175, "attack delay": 60, "slow duration": 250, "splash range": 100, "cost": 65},
    ),
])
def test_tower_stats_upgrade(TowerClass, level1_expected, level2_expected):

    tower = TowerClass(0, 0)  
    stats = tower.upgrade_stats[tower.level]
    

    for key, val in level1_expected.items():
        assert stats[key] == val


    tower.upgrade()
    stats = tower.upgrade_stats[tower.level]

    for key, val in level2_expected.items():
        assert stats[key] == val
