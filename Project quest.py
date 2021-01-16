# Импорт pygame
import pygame
import time
import sys
# Импорт клавиш
from pygame.locals import(K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE)

# Инициализация музыки
pygame.mixer.init()
pygame.mixer.music.load('D:\Projects\.vscode\Music\Worakls - Pain Forest1.wav')
sound_hit = pygame.mixer.Sound('D:\Projects\.vscode\Music\kboom.wav')

# Инициализация шрифтов
pygame.font.init()
Starfont = pygame.font.Font('D:\Projects\.vscode\Fonts\SF Distant Galaxy Alternate.ttf', 38)

# Класс Sprite () метод render
class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)

    def render(self):
        screen.blit(self.image, (self.x, self.y))

# Функция столкновения объектов Interspect

def Intersect(x1, x2, y1, y2, size_x, size_y):
    if (x1 > x2 + size_x) and (x1 < x2 - size_x) and (y1 > y2 + size_y) and (y1 < y2 - size_y):
        return True
    else:
        return False

# Объявляем экран, окно
window = pygame.display.set_mode([720, 480])
screen = pygame.Surface([720, 480])
score = pygame.Surface([720, 40])

# Объявление действующих объектов 
tank = Sprite(200, 300, "D:\Projects\.vscode\img\Tank1.png")
zombie = Sprite(200, 100, "D:\Projects\.vscode\img\Zombie.png")

zombie.step = 1

# название вкладки
pygame.display.set_caption("Платформер ЛОЛ 0_0")

# 3 платформы
platform1 = Sprite(125, 400, 'D:\Projects\.vscode\img\KEK.png')
platform2 = Sprite(250, 400, 'D:\Projects\.vscode\img\KEK.png')
platform3 = Sprite(375, 400, 'D:\Projects\.vscode\img\KEK.png')

# Пуля
weapon = Sprite(-100, -100, 'D:\Projects\.vscode\img\Gun1.png')

# Бенз
# fuel1 = Sprite(140, 330, 'D:\Projects\.vscode\img\kanistra.png')
# fuel2 = Sprite(265, 330, 'D:\Projects\.vscode\img\kanistra.png')
# fuel3 = Sprite(390, 330, 'D:\Projects\.vscode\img\kanistra.png')

right_free, left_free, up_free, down_free = True, True, True, True
right_freeZ, left_freeZ, up_freeZ, down_freeZ = True, False, False, False

weapon.push = False

Tank_Space = [right_free, left_free, up_free, down_free]
key_right_press, key_left_press, key_up_press, key_down_press = False, False, False, False
Zombie_Space = [right_freeZ, left_freeZ, up_freeZ, down_freeZ]

score1 = 0


# будет запущенно пока не закроем окно
running = True
# if running:
    # pygame.mixer.music.play(-1)
while running:
    # Щелкнули ли мы закрыть окно?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                key_left_press = True
            elif event.key == K_RIGHT:
                key_right_press = True
            elif event.key == K_UP:
                key_up_press = True
            elif event.key == K_DOWN:
                key_down_press = True
            elif event.key == K_SPACE:
                if weapon.push == False:
                    weapon.x = tank.x + 15
                    weapon.y = tank.y
                    weapon.push = True
        
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                key_left_press = False
            elif event.key == K_RIGHT:
                key_right_press = False
            elif event.key == K_UP:
                key_up_press = False
            elif event.key == K_DOWN:
                key_down_press = False


    # Фон
    screen.fill([0, 255, 255])
    score.fill([0, 0, 0])

    # Движение пули
    if weapon.push == True:
        weapon.x = weapon.x + 1
    else:
        weapon.x = -100
        weapon.y = -100
    if weapon.x > 720:
        weapon.push = False

    # Движение Зомби
    if Zombie_Space[0]:
        zombie.x = zombie.x + zombie.step
        if zombie.x > 660:
            Zombie_Space[0] = False
            Zombie_Space[1] = True
    elif Zombie_Space[1]:
        zombie.x = zombie.x - zombie.step
        if zombie.x < 0:
            Zombie_Space[0] = True
            Zombie_Space[1] = False
    

    # движение танка
    if Tank_Space[0] and key_right_press:
        tank.x = tank.x + 1
        Tank_Space[1] = True
        if tank.x > 660:
            Tank_Space[0] = False

    elif Tank_Space[1] and key_left_press:
        tank.x = tank.x - 1
        Tank_Space[0] = True
        if tank.x < 0:
            Tank_Space[1] = False

    elif Tank_Space[2] and key_up_press:
        tank.y = tank.y - 1
        Tank_Space[3] = True
        if tank.y < 0:
            Tank_Space[2] = False

    elif Tank_Space[3] and key_down_press:
        tank.y = tank.y + 1
        Tank_Space[2] = True
        if tank.y > 420:
            Tank_Space[3] = False

    # Столкновение пули с врагом( = Смэрть (Не сразу))
    if Intersect(weapon.x, zombie.x, weapon.y, zombie.y, 60, 60):
        sound_hit.play()
        weapon.push = False
        zombie.step += 0.1
        score1 += 1
        print(score1)

    if Intersect(tank.x, zombie.x, tank.y, zombie.y, 60, 60):
        zombie.step -= zombie.step * 0.1 * score1
        score1 = 0
        while i > 0:
            tank.y = tank.y + i
            i -= 1
        else:
            i = 20

    if Intersect(tank.x, platform1.x, tank.y, platform1.y, 60, 60):
        Tank_Space[3] = False
        #if tank.y > 420:
        #    Tank_Space[3] = False
        #else:
        #    Tank_Space[3] = True

    if Intersect(tank.x, platform2.x, tank.y, platform2.y, 10, 50):
        Tank_Space[3] = False
        #if tank.y > 420:
        #    Tank_Space[3] = False
        #else:
        #    Tank_Space[3] = True

    if Intersect(tank.x, platform3.x, tank.y, platform3.y, 10, 50):
        Tank_Space[3] = False
        #if tank.y > 420:
        #    Tank_Space[3] = False
        #else:
        #    Tank_Space[3] = True
        
    
    tank.render()
    zombie.render() 
    weapon.render()
    platform1.render()
    platform2.render()
    platform3.render()

        # отображение текста
    text = Starfont.render('Score:', 1, [255, 0, 0])
    score.blit(text, [0, 0])
    text_score1 = Starfont.render(str(score1), 1, [255, 255, 255])
    score.blit(text_score1, [150, 0])

    
    
    # отображение

    window.blit(screen, [0, 0])
    window.blit(score, [0, 0])



    # для того, чтобы все обновления стали видимыми
    pygame.display.flip()
    pygame.time.delay(3)
else:
    pygame.quit()
pygame.quit()