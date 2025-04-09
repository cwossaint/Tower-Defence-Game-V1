from entities.enemy.speedy_enemy_class import Speedy_Enemy
from entities.enemy.basic_enemy_class import Basic_Enemy
from entities.enemy.tanky_enemy_class import Tanky_Enemy
from entities.enemy.boss_enemy_class import Boss_Enemy

def test_enemy_speed():
    obj1 = Speedy_Enemy(0,0, [], None, 0)
    assert obj1.health == 15
    assert obj1.damage == 10
    assert obj1.speed == 10

    obj2 = Tanky_Enemy(0,0, [], None, 0)
    assert obj2.health == 50
    assert obj2.damage == 20
    assert obj2.speed == 3

    obj3 = Basic_Enemy(0,0, [], None, 0)
    assert obj3.health == 20
    assert obj3.damage == 10
    assert obj3.speed == 5

    obj4 = Boss_Enemy(0,0, [], None, 0)
    assert obj4.health == 50
    assert obj4.damage == 20
    assert obj4.speed == 3