import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from entities.tower.dart_tower_class import Dart
from entities.enemy.base_enemy_class import Enemy

def test_tower_target_closest():

    Enemy.all_enemies = []

    towerobj = Dart(0, 450) # range = 150

    enemyobj1 = Enemy(0, 550, [], None, 0, 0, 0, 0)
    enemyobj2 = Enemy(50, 220, [], None, 0, 0, 0, 0)
    enemyobj3 = Enemy(0, 600, [], None, 0, 0, 0, 0)

    towerobj.find_target()
    assert towerobj.target == enemyobj1


def test_tower_target_in_range():

    Enemy.all_enemies = []

    towerobj = Dart(0, 450) # range = 150

    enemyobj1 = Enemy(600, 550, [], None, 0, 0, 0, 0)
    enemyobj2 = Enemy(50, 220, [], None, 0, 0, 0, 0)
    enemyobj3 = Enemy(500, 600, [], None, 0, 0, 0, 0)

    towerobj.find_target()
    assert towerobj.target == None
