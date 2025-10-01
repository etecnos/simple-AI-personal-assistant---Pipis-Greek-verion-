import pygame

def run_window(image_path):
    pygame.init()


    window_size = (800, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("AI Assistant")


    image = pygame.image.load(image_path)
    scaled_image = pygame.transform.scale(image, window_size)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(scaled_image, (0, 0))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
