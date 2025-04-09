import pytest
from entities.tower.boomerang_tower_class import Tower, Boomerang
from entities.tower.dart_tower_class import Dart
from entities.tower.glue_tower_class import Glue
from entities.tower.cannon_tower_class import Cannon
from entities.enemy.basic_enemy_class import Basic_Enemy

def test_find_target():
    tower_obj = Tower(0,0)
    Basic_Enemy.all_enemies = []

    enemy_obj1 = Basic_Enemy(750, 750)
    enemy_obj2 = Basic_Enemy(450, 600)
    enemy_obj3 = Basic_Enemy(650, 400)


    tower_obj.find_target()
    assert tower_obj.target == None

    enemy_obj4 = Basic_Enemy(150, 50)
    enemy_obj5 = Basic_Enemy(40, 50)
    enemy_obj6 = Basic_Enemy(60, 70)

    tower_obj.find_target()
    assert tower_obj.target == enemy_obj5

def test_dart_attributes():
    obj = Dart(0,0)
    assert obj.range == 200
    assert obj.damage == 1
    assert obj.attack_delay == 4

def test_cannon_attributes():
    obj = Cannon(0,0)
    assert obj.range == 150
    assert obj.damage == 10
    assert obj.attack_delay == 40

def test_glue_attributes():
    obj = Glue(0,0)
    assert obj.range == 150
    assert obj.damage == 2
    assert obj.attack_delay == 10

def test_boomerang_attributes():
    obj = Boomerang(0,0)
    assert obj.range == 200
    assert obj.damage == 4
    assert obj.attack_delay == 20