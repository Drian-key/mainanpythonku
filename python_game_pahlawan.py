




player1 = {"name":"gopal", "power":200}
player2 = {"name":"yaya", "power":350}


def train(player):
	player['power'] += 100

def atk(atkers, defend):
	if(atkers['power'] > defend['power']):
		print("kamu menang", atkers['name'])
	else:
		print("kamu kalah", atkers['name'])

train(player2)
train(player2)
atk(player2, player1)