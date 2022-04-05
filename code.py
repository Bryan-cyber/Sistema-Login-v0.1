import sqlite3

db = sqlite3.connect('dados.db')
cursor = db.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (login text,senha integer)")
db.commit()
#cursor.execute("INSERT INTO cadastro VALUES ('Teste2', '123')")
#cursor.execute("SELECT * FROM cadastro")


from PySimpleGUI import PySimpleGUI as sg
import pyautogui
import openpyxl


seu_login = "Nada"
sua_senha = "0"



def cadastro():
    sg.theme('Reddit')
    ly = [

        [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))], 
        [sg.Text('Senha'), sg.Input(key='senha', size=(21,1), password_char='*')], 
        [sg.Button('Cadastrar')],
        [sg.Button('Efetuar Login')],
    #[sg.Output(size=(20,10))],
    ]
    return sg.Window('Cadastrar', ly, finalize=True)

def janela_login():
    sg.theme('Reddit')
    ly2 = [
        [sg.Text('Usuário'), sg.Input(key='usuario_login', size=(20,1))], 
        [sg.Text('Senha'), sg.Input(key='usuario_senha', size=(21,1), password_char='*')], 
        [sg.Button('Login')],
    ]
    return sg.Window('Efetuar Login', ly2, finalize=True)

def consulta_logins(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

janela1, janela2 = cadastro(), None


def logins_cadastrados():
    lg = cursor.execute("SELECT * FROM cadastro")
    for r in lg:
        return r[0]


while True: 
    window, botao, valores = sg.read_all_windows() 
    if window == janela1 and botao == sg.WINDOW_CLOSED: 
        pyautogui.alert("Programa encerrado")
        break  
    if window == janela2 and botao == sg.WINDOW_CLOSED: 
        pyautogui.alert("Programa encerrado")
        break
    if window == janela1 and botao == "Efetuar Login":
        janela2 = janela_login() 
        janela1.hide()
    if window == janela1 and botao == "Cadastrar":
        if valores['usuario'] == "":
            pyautogui.alert("Você não pode cadastrar sem escrever seu usuário")
        elif valores['usuario'] == logins_cadastrados():
            pyautogui.alert("Você não pode cadastrar um login já existente")
        elif valores['senha'] == "":
            pyautogui.alert("Você não pode cadastrar sem escrever sua senha") 
        elif len(valores['usuario']) <5:
              pyautogui.alert("Você deve utilizar até 5 caracteres em seu usuário")
        elif len(valores['senha']) <8:
              pyautogui.alert("Você deve utilizar até 8 caracteres em sua senha")
        elif valores['usuario'] == valores['senha']:
              pyautogui.alert("Você deve utilizar um usuario diferente de sua senha")
        else:
            adicionando = cursor.execute("INSERT INTO cadastro VALUES ('"+valores['usuario']+"', '"+valores['senha']+"')")
            pyautogui.alert("Cadastro efetuado. Efetue o login para ter acesso total")
            seu_login = valores['usuario']
            sua_senha = valores['senha']
            db.commit()
    if window == janela2 and botao == "Login":
        tabela = cursor.execute("SELECT * FROM cadastro WHERE login = '{}'".format(valores['usuario_login']))
        senha_db = cursor.fetchall()
        if str(senha_db[0][1]) == valores['usuario_senha']:
            pyautogui.alert("Login efetuado com sucesso")
        else:
            pyautogui.alert("Senha inválida")








