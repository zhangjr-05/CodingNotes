import sys
import time
import pygame
import settings

pygame.init()

highest_points = 0

# 主窗口
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
pygame.display.set_caption('星球大战')

# 战斗机
fighter = pygame.image.load(r'D:\mypython\Game\game_library\星球大战\fighter.png')
fighter = pygame.transform.scale(fighter, (70, 70))   # 调整图片大小
fighter_rect = fighter.get_rect()
fighter_rect.midbottom = screen_rect.midbottom

# 子弹
bullets = pygame.sprite.Group()


# 文字
txt_font = pygame.font.SysFont(None, 24)
txt_image = txt_font.render(f'Highest Points: {highest_points}', True, settings.red, settings.night_blue)
txt_rect = txt_image.get_rect()




# 开关
moving_left = False
moving_right = False


# 循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True

            if event.key == pygame.K_SPACE:
                if len(bullets) < 5:
                    new_bullet = pygame.sprite.Sprite()
                    new_bullet.rect = pygame.Rect(0, 0, 5, 15)
                    new_bullet.rect.midbottom = fighter_rect.midtop
                    bullets.add(new_bullet)

            

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False

    if moving_left and fighter_rect.left > 0:
        fighter_rect.x -= 1
    if moving_right and fighter_rect.right < 800:
        fighter_rect.x += 1
    

    # 绘制图像
    
    screen.fill(settings.night_blue)    # 分别代表红绿蓝的强度
    screen.blit(txt_image, txt_rect)
    screen.blit(fighter, fighter_rect)

    for bullet in bullets:
        pygame.draw.rect(screen, settings.yellow, bullet)
        bullet.rect.y -= 1
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    

    pygame.display.flip()

    time.sleep(0.001)

