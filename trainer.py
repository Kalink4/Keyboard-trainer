from pygame_functions import*
import pygame,random,keyboard,sys
level=1
time=50
letters_list=["а","п","р","о"] 
pygame.init()
screenSize(900, 400)
setBackgroundColour([255, 239, 213])# бежевая заливка экрана
# ***Создание спрайтов для анимации***
kusq=makeSprite('img/dino1.png')
addSpriteImage(kusq,'img/dino2.png')
transformSprite(kusq,0,0.35)
moveSprite(kusq, 50, 100)
changeSpriteImage(kusq,1)
showSprite(kusq)
# *** Создание текстовых лейблов***
label=makeLabel('',45, 370, 195, fontColour=[25, 25, 112], font='segoe ui', background='clear')
exit_label=makeLabel('Нажмите Esc,<br>чтобы выйти', 20, 720, 10, fontColour=[160, 82, 45], font='segoe print', background='clear')
score_label=makeLabel('Точность: ', 30, 30, 50, fontColour=[160, 82, 45], font='segoe ui', background='clear')
percent_label=makeLabel('', 30, 30, 90, fontColour=[25, 25, 112], font='segoe ui', background='clear')
next_lvl_label=makeLabel('Нажмите ENTER, чтобы продолжить', 40, 140, 300, fontColour=[255, 69, 0], font='segoe ui', background="clear")
level_label=makeLabel('Уровень:', 20, 30, 10, fontColour=[160, 82, 45], font='segoe print', background='clear')
level_num_label=makeLabel('', 20, 30, 30, fontColour=[25, 25, 112], font='segoe print', background='clear')
speed_label=makeLabel('Средняя скорость: ', 30, 30, 130, fontColour=[160, 82, 45], font='segoe ui', background='clear')
speed_num_label=makeLabel('', 30, 30, 170, fontColour=[25, 25, 112], font='segoe ui', background='clear')
# ***Показать лейблы в начале уровня***
showLabel(exit_label)
showLabel(level_label)
showLabel(level_num_label)
# ***Вывод результатов уровня***
def level_end():
	global score
	score=score*2
	#скрыть предыдущие изображения
	hideLabel(label)
	hideLabel(level_label)
	hideLabel(level_num_label)
	hideSprite(kusq)
	#показать изобр-я со счетом
	showLabel(score_label)
	changeLabel(percent_label,str(score)+"%")
	changeLabel(speed_num_label,str(level_speed)+" сим/мин")
	showLabel(percent_label)
	if level<6:
		showLabel(next_lvl_label)
	showLabel(speed_label)
	showLabel(speed_num_label)

	# ***отлавливать клавиши, чтобы либо выйти, либо перейти на следующий уровень***
	while 1:
		if keyboard.read_key()=='enter':
			break
		elif keyboard.read_key()=="esc":
			sys.exit(0)
	#скрыть изобр-я со счетом
	hideLabel(score_label)
	hideLabel(next_lvl_label)
	hideLabel(percent_label)
	hideLabel(speed_label)
	hideLabel(speed_num_label)
	pygame.time.delay(time)

# ***Создание строки для следующего уровня***
def create_level(lvl_num:int): 
	global letters_list
	if level==1:
		new_letters=["-"]
	if level==2:
		new_letters=["к","е","н","г"]
	elif level==3:
		new_letters=["с","м","и","т","ь"]
	elif level==4:
		new_letters=["ы","в","л","д"]
	elif level==5:
		new_letters=["ц","у","ш","щ","я","ч"]
	elif level==6:
		new_letters=["ф","й","з","б","ю","ё","х","ъ"]
	letters_list.extend(new_letters)

def level_run(): 
	global score
	global level_speed
	start_time=pygame.time.get_ticks()
	showSprite(kusq)
	showLabel(level_label)
	changeLabel(level_num_label, str(level))
	showLabel(level_num_label)
	score=0
	letters=[random.choice(letters_list) for i in range(50)] # заполнение списка случайными буквами
	start=0
	end=15
	while start<50:
		pygame.time.delay(time)
		type_letters=''.join(letters[start:end]) #преобразовать список в строку
		changeLabel(label, type_letters)
		showLabel(label)
		start=start+1
		if end<50:
			end=end+1
		current_key=type_letters[0] #первая буква из сформироваанного массива
		key=keyboard.read_key()
		if key=="esc":
			sys.exit(0)
		# ***Анимация и увеличение счета***
		if key == current_key or (key=="space" and current_key=="-"):
			score=score+1
			changeSpriteImage(kusq,0)
			showSprite(kusq)
			pygame.time.delay(time)
			changeSpriteImage(kusq,1)
			showSprite(kusq)
		else:
			pygame.time.delay(time)
	end_time=pygame.time.get_ticks()
	level_time=(end_time-start_time)/60000 #время в минутах, затраченное на уровень
	level_speed=int(50/level_time)# количество символов в минуту

while level<7:
	create_level(level)
	level_run()
	level_end()
	level=level+1
pygame.time.delay(time)