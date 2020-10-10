car_started = False
while True:
    command = input('>')
    if command.lower() == 'start':   # Utilizando o metodo lower() para tornar o input case insensitive
        if car_started:              # Mesmo que if car_started == True:
            print('The car is already started!')
        else:
            print('Car started... Ready to go!')
            car_started = True
    elif command.lower() == 'stop':
        if not car_started:    # Mesmo que if car_started == False:
            print('The car is already stopped!')
        else:
            print('Car stopped')
            car_started = False
    elif command.lower() == 'quit':
        break
    elif command.lower() == 'help':
        print("""                 
start - to start the car
stop - to stop the car             
quit - to exit
        """)                   # String de multiplas linhas, utilizandos aspas triplas """ """, note que o espacamento normal do elif nao eh necessario, e se houver, ira aparecer espacado no output.
    else:
        print("What")