import pygame, sys, time, random

# check error game

check_error = pygame.init()
if check_error[1] > 0:
	print('[!] {check_error} error game')
else:
	print('[+] Game berhasil di install')


# nama
nama = input("Siapa namamu:")

#===== Window game =====

size_x = 720
size_y = 480

# Judul game
pygame.display.set_caption('Ular python riski drian pratama')
screen = pygame.display.set_mode((size_x, size_y))

# Game variabel color
black = pygame.Color(0, 0 ,0)
coklat = pygame.Color(0,100,255)
white  = pygame.Color(255,255,255,255)
green  = pygame.Color(255, 0, 255)

# snake

snake_pos = [100, 50]

snake_tubuh = [[100,50],[90,50],[80,50]]

change_to = "RIGHT"
direction = "RIGHT"

# food
food_pos = [random.randrange(1, size_x // 10) * 10 , random.randrange(1, size_y // 10) * 10] 
food_spawn = True

# skor
score = 0


pygame.mixer.init()
eating = pygame.mixer.Sound('nyam.mp3')


#kelur game
def keluar():
	print('you lose' + nama)

# game over
def game_over():
	my_font = pygame.font.SysFont('times new roman', 90)
	game_over_surface = my_font.render('Mengulang', True, white)
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (size_x/2, size_y/4)
	screen.fill(black)
	screen.blit(game_over_surface, game_over_rect)
	# show score
	pygame.display.flip()
	time.sleep(3)
	keluar()


#show score 
def show_score():
	score_font = pygame.font.SysFont('consolas', 20)
	score_surface = score_font.render('Poin mu: ' + str(score), True, black)
	score_rect = score_surface.get_rect()
	score_rect.midtop = (72, 15)

	screen.blit(score_surface, score_rect)
	pygame.display.flip()
def nama_gw():
	score_font = pygame.font.SysFont('consolas', 20)
	score_surface = score_font.render(nama, True, black)
	score_rect = score_surface.get_rect()
	score_rect.midtop = (250, 15)

	screen.blit(score_surface, score_rect)
	pygame.display.flip()

#change bg to white
screen.fill(white)

# running
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				change_to = "RIGHT"
			if event.key == pygame.K_LEFT:
				change_to = "LEFT"
			if event.key == pygame.K_UP:
				change_to = "UP"
			if event.key == pygame.K_DOWN:
				change_to = "DOWN"
	# update screen to white again
	
	# create snake
	for pos in snake_tubuh:
		pygame.draw.ellipse(screen, green, pygame.Rect(pos[0], pos[1],10,10))
	snake_tubuh.insert(0, snake_pos[:])
	 

	# snake run

	# fix sure move
	if change_to == "RIGHT" and direction != "LEFT":
		direction = "RIGHT"
	if change_to == "LEFT" and direction != "RIGHT":
		direction = "LEFT"
	if change_to == "UP" and direction != "DOWN":
		direction = "UP"
	if change_to == "DOWN" and direction != "UP":
		direction = "DOWN"

		#================
	if direction == "RIGHT":
		snake_pos[0] += 10
	if direction == "LEFT":
		snake_pos[0] -= 10
	if direction == "UP":
		snake_pos[1] -= 10
	if direction == "DOWN":
		snake_pos[1] += 10

	# snake over window
	if snake_pos[0] > size_x:
		snake_pos[0] = 0
	if snake_pos[0] < 0:
		snake_pos[0] = size_x
	if snake_pos[1] > size_y:
		snake_pos[1] = 0
	if snake_pos[1] < 0:
		snake_pos[1] = size_y

	# draw food
	pygame.draw.ellipse(screen, coklat, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

	# snake eating food

	if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
		food_spawn = False
		score += 1
		eating.play()
	else:
		snake_tubuh.pop()

	# logic food spawn
	if not food_spawn:
		food_pos = [random.randrange(1, size_x // 10) * 10 , random.randrange(1, size_y // 10) * 10] 
	food_spawn = True
	#show score
	show_score()

	#game over
	for block in snake_tubuh:
		if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
			game_over()

	nama_gw()

	# level
	pygame.time.Clock().tick(10)

	# update screen 

	pygame.display.update()