import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from entities.enemy.basic_enemy_class import Basic_Enemy
from entities.enemy.speedy_enemy_class import Speedy_Enemy
from entities.enemy.boss_enemy_class import Boss_Enemy
from entities.enemy.tanky_enemy_class import Tanky_Enemy

@pytest.mark.parametrize("enemy_class, expected_stats", [
    (Basic_Enemy, {"health": 20, "damage": 10, "speed": 5}),
    (Speedy_Enemy, {"health": 15, "damage": 10, "speed": 10}),
    (Boss_Enemy,  {"health": 500, "damage": 100, "speed": 1}),
    (Tanky_Enemy,  {"health": 50, "damage": 20, "speed": 3}),
])
def test_enemy_stats(enemy_class, expected_stats):
    dummy_direction_list = ["left", "right"]
    dummy_wave = 0
    dummy_game_data = None
    enemy = enemy_class(0, 0, dummy_direction_list, dummy_game_data, dummy_wave)
    assert enemy.health == expected_stats["health"]
    assert enemy.speed == expected_stats["speed"]
    assert enemy.damage == expected_stats["damage"]
