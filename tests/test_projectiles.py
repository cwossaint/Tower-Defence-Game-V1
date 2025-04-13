import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pygame
from entities.tower.dart_tower_class import Dart
from entities.tower.boomerang_tower_class import Boomerang
from entities.tower.cannon_tower_class import Cannon
from entities.tower.gatling_tower_class import Gatling
from entities.tower.glue_tower_class import Glue
from entities.projectile.base_projectile_class import Projectile
from entities.projectile.boomerang_projectile_class import Boomerang_Projectile
from entities.projectile.cannon_projectile_class import Cannon_Projectile
from entities.projectile.basic_projectile_class import Basic_Projectile
from entities.projectile.glue_projectile_class import Glue_Projectile

class DummyEnemy:
    def __init__(self, x=100, y=100, width=40, height=40):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)

@pytest.fixture(autouse=True)
def reset_projectiles():
    
    Projectile.all_projectiles.clear()
    pygame.init()  
    yield
    pygame.quit()

def test_dart_tower_fires_projectile():
    tower = Dart(50, 50)
    tower.target = DummyEnemy()
    tower.attack_timer = tower.attack_delay
    tower.fire_projectile()
    
    projectile = Projectile.all_projectiles[-1]
    assert isinstance(projectile, Basic_Projectile)
    assert projectile.damage == tower.damage
    assert projectile.speed == 20  
    assert projectile.size == 20  

def test_boomerang_tower_fires_projectile():
    tower = Boomerang(50, 50)
    tower.target = DummyEnemy()
    tower.attack_timer = tower.attack_delay
    tower.fire_projectile()

    projectile = Projectile.all_projectiles[-1]
    assert isinstance(projectile, Boomerang_Projectile)
    assert projectile.damage == tower.damage
    assert projectile.pierce == tower.pierce

def test_cannon_tower_fires_projectile():
    tower = Cannon(50, 50)
    tower.target = DummyEnemy()
    tower.attack_timer = tower.attack_delay
    tower.fire_projectile()

    projectile = Projectile.all_projectiles[-1]
    assert isinstance(projectile, Cannon_Projectile)
    assert projectile.damage == tower.damage
    assert projectile.splash_damage == tower.splash_damage
    assert projectile.splash_range == tower.splash_range

def test_gatling_tower_fires_projectile():
    tower = Gatling(50, 50)
    tower.target = DummyEnemy()
    tower.attack_timer = tower.attack_delay
    tower.fire_projectile()

    projectile = Projectile.all_projectiles[-1]
    assert isinstance(projectile, Basic_Projectile)
    assert projectile.damage == tower.damage
    assert projectile.speed == 20

def test_glue_tower_fires_projectile():
    tower = Glue(50, 50)
    tower.target = DummyEnemy()
    tower.attack_timer = tower.attack_delay
    tower.fire_projectile()

    projectile = Projectile.all_projectiles[-1]
    assert isinstance(projectile, Glue_Projectile)
    assert projectile.slow == tower.slow
    assert projectile.slow_duration == tower.slow_duration
    assert projectile.splash_range == tower.splash_range
