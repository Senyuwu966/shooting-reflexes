import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Nhấp vào Hình Tròn")

# Định nghĩa màu sắc
GREY = (128, 128, 128)  # Màu xám
BLACK = (0, 0, 0)       # Màu đen
WHITE = (255, 255, 255) # Màu trắng

# Khởi tạo biến
counter = 0
radius = 50
random_screen = (random.randint(radius, 800 - radius), random.randint(radius, 500 - radius))

# Tạo font để hiển thị văn bản
font = pygame.font.Font(None, 36)  # None để sử dụng font mặc định, 36 là kích thước font

def draw():
    screen.fill(GREY)
    pygame.draw.circle(screen, BLACK, random_screen, radius)
    
    # Hiển thị bộ đếm trên màn hình
    counter_text = font.render(f"{counter}", True, WHITE)
    screen.blit(counter_text, (10, 10))  # Vẽ văn bản ở góc trên bên trái

# Vòng lặp chính của trò chơi
running = True
draw()  # Vẽ hình tròn ban đầu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Nút chuột trái
                mouse_pos = pygame.mouse.get_pos()
                # Kiểm tra xem cú nhấp chuột có nằm trong hình tròn không
                distance_sq = (mouse_pos[0] - random_screen[0])**2 + (mouse_pos[1] - random_screen[1])**2
                if distance_sq <= radius**2:
                    counter += 1
                    # Tạo một vị trí ngẫu nhiên mới cho hình tròn
                    random_screen = (random.randint(radius, 800 - radius), random.randint(radius, 500 - radius))
                # Nếu nhấp bên ngoài, không làm gì cả

    # Vẽ lại hình tròn và bộ đếm
    draw()
    pygame.display.update()

# Thoát Pygame
pygame.quit()