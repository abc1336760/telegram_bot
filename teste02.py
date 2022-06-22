import pyperclip
import telebot as tbot

chatid = '-621832928'
chatid_02 = '-587755138'

try:
    api_key = '5453037027:AAG9ZzMWq4GQM7qZfP3dTknWCflpUt_pgtU'
    bot = tbot.TeleBot(api_key)
except:
    print('error')
def envia():
    copia = input('Copie oque voce quer que seja mandado para os grupos e Digite [S] para enviar:  ')
    u = copia.upper()
    if u == 'S':
        cola = pyperclip.paste()
        bot.send_message(chatid, cola)
        bot.send_message(chatid_02, cola)
        print('Enviado!')
        msg = input('Deseja mandar mais alguma mensagem? digite [S] para sim e [N] para sair do programa: ')
        msgu = msg.upper()
        if msgu == 'S':
            envia()
        elif msgu == 'N':
            exit()
    else:
        print('digite um valor valido')
        envia()


envia()

bot.polling()
