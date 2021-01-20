# Импорт pygame

import pygame
import time
import sys
import random
# Импорт клавиш
from pygame.locals import(K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, K_RETURN, MOUSEBUTTONDOWN)

# Инициализация музыки
pygame.mixer.init()
pygame.mixer.music.load('D:\Projects\.vscode\Music\Worakls - Pain Forest1.wav')
sound_hit = pygame.mixer.Sound('D:\Projects\.vscode\Music\kboom.wav')

# Инициализация шрифтов
pygame.font.init()
Starfont = pygame.font.Font('D:\Projects\.vscode\Fonts\SF Distant Galaxy Alternate.ttf', 38)


class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 0, 0)
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()
    

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()
                
    def getText(self):
        return self.text
    

text_input_box = TextInputBox(-1, 432, 300, Starfont)
group = pygame.sprite.Group(text_input_box)


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
    if (x1 > x2 - size_x) and (x1 < x2 + size_x) and (y1 > y2 - size_y) and (y1 < y2 + size_y):
        return True
    else:
        return False

def you_win():
    while True:
        screen.fill([131, 35, 35])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
        textWin = Starfont.render('You win', 1, [255, 0, 0])
        screen.blit(textWin, [150, 150])
        window.blit(score, [0, 0])
        window.blit(screen, [0, 40])
        pygame.display.flip()


def loser():
        while True:
            screen.fill([131, 35, 35])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True
        textLose = Starfont.render('You lost', 1, [255, 0, 0])
        screen.blit(textLose, [150, 150])
        window.blit(score, [0, 0])
        window.blit(screen, [0, 40])
        pygame.display.flip()

def load_menu():
    # наюор пунктов меню список []
    elements_menu = [   
        #[x, y, название, цвет обычный, цвет при наведении, id]
        [300, 200, 'Play', [255, 0, 0], [0, 255, 0], 0],
        [300, 270, 'Quit', [255, 0, 0], [0, 255, 0], 1]
    ]
    pygame.mouse.set_visible(True)

    element = -1
    done = False
    while not done:
        screen.fill([0, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if element == 0:
                    done = True
                elif element == 1:
                    pygame.quit()
                    sys.exit()
            # Получение позиции курсора мыши
            pointer = pygame.mouse.get_pos()
             # Совпали ли координаты курсора и кнопки
            for el in elements_menu:
                if pointer[0] > el[0] and pointer[0] < el[0] + 100 and pointer[1] < el[1] + 10 and pointer[1] > el[1]:
                    element = el[5]

            
            for el in elements_menu:
                if element == el[5]:
                    screen.blit(Starfont.render(el[2], 1, el[4]), [el[0], el[1] - 40])
                else:
                    # изменение цвета
                    screen.blit(Starfont.render(el[2], 1, el[3]), [el[0], el[1] - 40])

            window.blit(score, [0, 0])
            window.blit(screen, [0, 0])
            pygame.display.flip()


# Объявляем экран, окно
window = pygame.display.set_mode([720, 480])
screen = pygame.Surface([720, 480])
score = pygame.Surface([720, 40])

# Объявление действующих объектов 
tank = Sprite(200, 300, "D:\Projects\.vscode\img\Tank1.png")
zombie = Sprite(600, 100, "D:\Projects\.vscode\img\Zombie.png")

zombie.step = 1

# название вкладки
pygame.display.set_caption("Платформер ЛОЛ 0_0")

# 3 платформы
platform1 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')
platform2 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')
platform3 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')
platform4 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')
platform5 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')
platform6 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')
platform7 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')
platform8 = Sprite(random.randint(0, 500), random.randint(60, 460), 'D:\Projects\.vscode\img\KEK.png')

# Пуля
weapon = Sprite(-100, -100, 'D:\Projects\.vscode\img\Gun1.png')

# Бенз
# fuel1 = Sprite(140, 330, 'D:\Projects\.vscode\img\kanistra.png')
# fuel2 = Sprite(265, 330, 'D:\Projects\.vscode\img\kanistra.png')
# fuel3 = Sprite(390, 330, 'D:\Projects\.vscode\img\kanistra.png')

right_free, left_free, up_free, down_free = True, True, True, True
right_freeZ, left_freeZ, up_freeZ, down_freeZ = False, True, False, True

weapon.push = False

Tank_Space = [right_free, left_free, up_free, down_free]
key_right_press, key_left_press, key_up_press, key_down_press = False, False, False, False
Zombie_Space = [right_freeZ, left_freeZ, up_freeZ, down_freeZ]

score1 = 0
i = 20
t = 1
input_active = True
inp_text = False
ot = TextInputBox(0, 0, 0, Starfont)

# будет запущенно пока не закроем окно
running = True
if running:
    load_menu() # pygame.mixer.music.play(-1)
while running:
    event_list = pygame.event.get()
    # Щелкнули ли мы закрыть окно?
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == text_input:
                    entered_text = text
                    
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_RETURN:
                inp_text = True
            if event.key == K_ESCAPE:
                load_menu()
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
    if Zombie_Space[3]:
        zombie.y = zombie.y + zombie.step
        if zombie.y > 420:
            Zombie_Space[3] = False
            Zombie_Space[2] = True
    elif Zombie_Space[2]:
        zombie.y = zombie.y - zombie.step
        if zombie.y < 0:
            Zombie_Space[3] = True
            Zombie_Space[2] = False
    

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
        if score1 > 0:
            zombie.step -= zombie.step * 0.1 * score1
        else:
            pass
        score1 = 0
        while i > 0:
            tank.x = tank.x - i
            i -= 1
        else:
            i = 20

    platform1.x = platform1.x - 1
    platform2.x = platform2.x - 1
    platform3.x = platform3.x - 1
    platform4.x = platform4.x - 1
    platform5.x = platform5.x - 1
    platform6.x = platform6.x - 1
    platform7.x = platform7.x - 1
    platform8.x = platform8.x - 1

    if platform1.x < -100:
        platform1.x = 800
        platform1.y = random.randint(60, 460)
    
    if platform2.x < -100:
        platform2.x = 800
        platform2.y = random.randint(60, 460)

    if platform3.x < -100:
        platform3.x = 800
        platform3.y = random.randint(60, 460)
    
    if platform4.x < -100:
        platform4.x = 800
        platform4.y = random.randint(60, 460)
    
    if platform5.x < -100:
        platform5.x = 800
        platform5.y = random.randint(60, 460)

    if platform6.x < -100:
        platform6.x = 800
        platform6.y = random.randint(60, 460)
    
    if platform7.x < -100:
        platform7.x = 800
        platform7.y = random.randint(60, 460)
    
    if platform8.x < -100:
        platform8.x = 800
        platform8.y = random.randint(60, 460)

    if Intersect(tank.x, platform1.x, tank.y, platform1.y, 100, 20):
        tank.y = tank.y - 50

    if Intersect(tank.x, platform2.x, tank.y, platform2.y, 100, 20):
        tank.y = tank.y - 50

    if Intersect(tank.x, platform3.x, tank.y, platform3.y, 100, 20):
        tank.y = tank.y - 50

    if Intersect(tank.x, platform4.x, tank.y, platform4.y, 100, 20):
        tank.y = tank.y - 50

    if Intersect(tank.x, platform5.x, tank.y, platform5.y, 100, 20):
        tank.y = tank.y - 50

    if Intersect(tank.x, platform6.x, tank.y, platform6.y, 100, 20):
        tank.y = tank.y - 50

    if Intersect(tank.x, platform7.x, tank.y, platform7.y, 100, 20):
        tank.y = tank.y - 50

    if Intersect(tank.x, platform8.x, tank.y, platform8.y, 100, 20):
        tank.y = tank.y - 50



    if score1 == 10:
        you_win()

    while t == 1:
        first = int(random.randint(1, 12)) 
        second = int(random.randint(1, 12))
        znak = int(random.randint(1, 4)) # 1 = +, 2 = -, 3 = *, 4 = /
        print(first, second, znak)
        if znak == 1:
            SUMM = first + second
            C = '+'
        elif znak == 2:
            SUMM = first - second
            if SUMM < 0:
                continue
            C = '-'
        elif znak == 3:
            SUMM = first * second
            C = 'x'
        elif znak == 4:
            if first % second != 0:
                continue
            else:
                SUMM = first / second
                C = '/'
        t -= 1
        

    text_C = Starfont.render(C, 1, [255, 255, 255])
    screen.blit(text_C, [zombie.x + 20, zombie.y - 40])
    text_F = Starfont.render(str(first), 1, [255, 255, 255])
    screen.blit(text_F, [zombie.x - 20, zombie.y - 40])
    text_S = Starfont.render(str(second), 1, [255, 255, 255])
    screen.blit(text_S, [zombie.x + 50, zombie.y - 40])

    if inp_text == True:
        ot = TextInputBox.getText()
        if int(ot) == SUMM:
            score1 += 1
            t = 1
            inp_text = False
        else:
            t = 1
            print('Упс, неверный ответ')
            inp_text = False
            if score1 == 0:
                pass
            else:
                score1 -= 1



        
    
    tank.render()
    zombie.render() 
    weapon.render()
    platform1.render()
    platform2.render()
    platform3.render()
    platform4.render()
    platform5.render()
    platform6.render()
    platform7.render()
    platform8.render()

        # отображение текста
    text = Starfont.render('Score:', 1, [255, 0, 0])
    score.blit(text, [0, 0])
    text_score1 = Starfont.render(str(score1), 1, [255, 255, 255])
    score.blit(text_score1, [150, 0])

    
    
    # отображение

    window.blit(screen, [0, 0])
    window.blit(score, [0, 0])
    group.update(event_list)
    group.draw(window)


    # для того, чтобы все обновления стали видимыми
    pygame.display.flip()
    pygame.time.delay(3)
else:
    pygame.quit()
pygame.quit()