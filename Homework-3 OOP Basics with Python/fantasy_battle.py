# fantasy_battle.py - Basit Savaş Oyunu OOP Örneği

from abc import ABC, abstractmethod
import random

#Soyutlama - Abstraction
class Character(ABC):
    def __init__(self, name, health, strength):
        #Encapsulation
        self._name = name
        self._health = health
        self._max_health = health
        self._strength = strength
        self._is_alive = True
    
    @property
    def name(self):
        return self._name
        
    @property
    def is_alive(self):
        return self._is_alive
    
    def take_damage(self, damage):
        self._health -= damage
        print(f"{self._name} {damage} hasar aldı! Kalan can: {self._health}")
        if self._health <= 0:
            self._health = 0
            self._is_alive = False
            print(f"{self._name} öldü!")
    
    def heal(self, amount):
        if self._is_alive:
            self._health = min(self._max_health, self._health + amount)
            print(f"{self._name} {amount} can yeniledi. Yeni can: {self._health}")
    
    #Abstract methods
    @abstractmethod
    def attack(self, target):
        pass
    
    @abstractmethod
    def special_ability(self):
        pass
    
    def __str__(self):
        status = "Hayatta" if self._is_alive else "Ölü"
        return f"{self._name} [{status}] - HP: {self._health}/{self._max_health}, Güç: {self._strength}"

#Inheritance
class Warrior(Character):
    def __init__(self, name, health=150, strength=15):
        # Parent constructor çağrısı
        super().__init__(name, health, strength)
        self._rage = 0
    
    #Method Overriding
    def attack(self, target):
        if not self._is_alive:
            return
        
        damage = self._strength + random.randint(1, 10)
        print(f"{self._name} kılıcıyla {target.name}'a saldırıyor!")
        target.take_damage(damage)
        self._rage += 15
    
    def special_ability(self):
        if not self._is_alive or self._rage < 50:
            print(f"Öfke yetersiz: {self._rage}/50")
            return False
        
        print(f"{self._name} ÖFKE PATLAMASI kullanıyor!")
        self._rage = 0
        return True

class Archer(Character):
    def __init__(self, name, health=100, strength=12):
        super().__init__(name, health, strength)
        self._arrows = 10
    
    def attack(self, target):
        if not self._is_alive or self._arrows <= 0:
            if self._arrows <= 0:
                print(f"{self._name}'in oku kalmadı!")
            return
        
        self._arrows -= 1
        damage = self._strength + random.randint(3, 8)
        print(f"{self._name} yayıyla {target.name}'a saldırıyor! Kalan ok: {self._arrows}")
        target.take_damage(damage)
    
    def special_ability(self):
        if not self._is_alive:
            return False
        
        self._arrows += 5
        print(f"{self._name} 5 ok topladı. Toplam ok: {self._arrows}")
        return True

class Mage(Character):
    def __init__(self, name, health=80, strength=10):
        super().__init__(name, health, strength)
        self._mana = 100
        self._max_mana = 100
    
    def attack(self, target):
        if not self._is_alive or self._mana < 10:
            if self._mana < 10:
                print(f"{self._name}'in manası yetersiz!")
            return
        
        self._mana -= 10
        damage = self._strength + random.randint(5, 15)
        print(f"{self._name} ateş topu fırlatıyor! Kalan mana: {self._mana}")
        target.take_damage(damage)
    
    def special_ability(self):
        if not self._is_alive or self._mana < 30:
            if self._mana < 30:
                print(f"Mana yetersiz: {self._mana}/30")
            return False
        
        self._mana -= 30
        print(f"{self._name} meditasyon yapıyor ve iyileşiyor!")
        self.heal(30)
        return True

# Ana oyun işleyişi
def simple_game():
    print("=== FANTASY BATTLE ===")
    
    # Karakterleri oluştur
    player = Warrior("Kahraman Savaşçı")
    enemies = [
        Archer("Goblin Okçu"),
        Mage("Kötü Büyücü")
    ]
    
    print("\nKarakterler:")
    print(player)
    for enemy in enemies:
        print(enemy)
    
    # Basit oyun döngüsü
    turn = 1
    while player.is_alive and any(enemy.is_alive for enemy in enemies):
        print(f"\n=== TUR {turn} ===")
        
        # Oyuncu sırası
        if player.is_alive:
            print("\nSıra sizde!")
            print("1. Saldır")
            print("2. Özel yetenek kullan")
            
            alive_enemies = [e for e in enemies if e.is_alive]
            if not alive_enemies:
                break
                
            choice = input("Seçiminiz (1-2): ")
            
            if choice == '1':
                # Basitleştirilmiş hedef seçimi
                target = alive_enemies[0]
                player.attack(target)
            elif choice == '2':
                if player.special_ability():
                    # Tüm düşmanlara saldır
                    for enemy in alive_enemies:
                        damage = player._strength * 2
                        print(f"{player.name} {enemy.name}'a güçlü saldırı yapıyor!")
                        enemy.take_damage(damage)
        
        # Düşman sırası
        for enemy in enemies:
            if enemy.is_alive and player.is_alive:
                # Basit AI
                if random.choice([True, False]):
                    enemy.attack(player)
                else:
                    enemy.special_ability()
        
        turn += 1
    
    # Oyun sonu
    print("\n=== OYUN SONU ===")
    if player.is_alive:
        print("Tebrikler, kazandınız!")
    else:
        print("Kaybettiniz!")

if __name__ == "__main__":
    simple_game()