import PySimpleGUI as sg

# PySimpleGUIのWindowTheme全リスト
# 無駄に長いリスト配列
# 各自好きなテーマに設定してよい。
# ただし見易さを考慮すること。
TL = ['Black']
# リストボックス用リスト変数
history = []
# サイズ用リスト変数
SizeLst = {
    'BTN': (6, 1),
    'PARM1': (16, 1),
    'PARM2': (16, 1),
    'ANSWER': (10, 1),
    'TXT01': (14, 1),
    'LSB': (35, 7)
}
# 処理ボタンレイアウト
PrcBtn = [[sg.Button('計算', size=SizeLst['BTN'], key='-GOGO-')],
          [sg.Button('消去', size=SizeLst['BTN'], key='-KESU-')],
          [sg.Button('保存', size=SizeLst['BTN'], key='-SAVE-', disabled=True)],
          [sg.Button('終了', size=SizeLst['BTN'], key='-OWARI-')]]
# 四則演算ラジオボタンレイアウト
keyName = {
    'ADD': '-ADD-',
    'SUB': '-SUB-',
    'MUL': '-MUL-',
    'DIV': '-DIV-'}
# 四則演算記号^^^vvv

CalcModeRadio = [[sg.Radio('加算', group_id='calcmode', key=keyName['ADD'], default=True)],
                 [sg.Radio('減算', group_id='calcmode', key=keyName['SUB'], default=False)],
                 [sg.Radio('乗算', group_id='calcmode', key=keyName['MUL'], default=False)],
                 [sg.Radio('除算', group_id='calcmode', key=keyName['DIV'], default=False)]]

# メインレイアウト
layout = [[sg.Text('項目１', size=SizeLst['TXT01']),
           sg.Text('項目２', size=SizeLst['TXT01']),
           sg.Text('結果', size=SizeLst['ANSWER'])],
          [sg.InputText(size=SizeLst['PARM1'], key='-INP01-'),
           sg.InputText(size=SizeLst['PARM2'], key='-INP02-'),
           sg.Text('', size=SizeLst['ANSWER'], key='-ANSWER-')],
          [sg.Text('履歴↓↓↓', size=SizeLst['TXT01'])],
          [sg.Listbox(history, size=SizeLst['LSB'], key='-LSB-'),
           sg.Frame('計算', CalcModeRadio),
           sg.Frame('処理', PrcBtn)]]


# 計算用関数
# 計算不能な文字など計算結果は０とする。
# try,except,else,finally構文を利用する（必要なものだけでよい）
# 引数は各自で考える事。
# 戻り値も各自で考える事。
# return parm1, parm2と記述すると戻り値が2個になる
# 受け取りは  ret01, ret02 = calcExecute() みたいな。。。
#        ⇒ ret01にparm01，ret02にparm02が代入される。。。。
def calcExecute(l, r, s):
    try:
        if s == '+':
            return int(l + r)
        elif s == '-':
            return int(l - r)
        elif s == '×':
            return int(l * r)
        elif s == '÷':
            return int(l / r)
    except:
        return "ERROR"


# 必要であればThemeの設定
sg.theme('Black')


def getOperator():
    if values['-ADD-'] == 1:
        return "+"
    elif values['-SUB-'] == 1:
        return "-"
    elif values['-MUL-'] == 1:
        return "×"
    elif values['-DIV-'] == 1:
        return "÷"


# Windowの作成　※クラス番号氏名を各自に書き換える
window = sg.Window('PythonGUICalculator', layout)

while True:
    # イベントとデータの読み込み
    event, values = window.read()
    # 終了ボタン、WindowCloseボタン押下？
    if event in ('-OWARI-', None):
        break
        # 計算ボタン押下？
    # 項目が２つ入力されているときだけ計算関数へ。
    # 項目が未入力か1つだけの場合は何もしない。
    # 計算は関数を作成して結果を受け取り処理すること。
    # 必ずcalcExecuteを作成し、利用すること！！！！
    if event == '-GOGO-':
        l = values['-INP01-'].replace(' ', '')
        r = values['-INP02-'].replace(' ', '')
        if l != "" and r != "":
            try:
                history.append(l + getOperator() + r + '=' + str(calcExecute(int(l), int(r), getOperator())))
            except:
                history.append(l + getOperator() + r + '=EERROR')
            finally:
                window['-LSB-'].update(history)

    # 消去ボタン押下？
    if event == '-KESU-':
        # InputText,ListBox,Text,履歴用リスト配列をクリアする
        history.remove(values['-INP01-'])  # 項目1
        history.remove(values['-INP02-'])  # 項目2
        history.remove(values['-ANSWER-'])  # 結果
        history.remove(values['-LSB-'])  # 履歴リストボックス
        window['-LSB-'].update(history)  # 画面更新？

window.close()
