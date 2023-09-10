import os
import sys
import time
import tkinter
import tkinter.simpledialog
import threading


def install_lib(lib_name):
    print('安装', lib_name, '...', end='\n\n')
    os.system("\"" + sys.executable + "\" -m pip install --default-timeout=1688 " + lib_name)
    print(lib_name, '安装完毕！\n')


try:
    import pyperclip
except ModuleNotFoundError:
    install_lib("pyperclip")
    import pyperclip

try:
    import pystray
    from PIL import Image
except ModuleNotFoundError:
    install_lib("pystray")
    import pystray

try:
    import keyboard
except ModuleNotFoundError:
    install_lib("keyboard")
    import keyboard

try:
    import webbrowser as wb
except ModuleNotFoundError:
    install_lib("webbrowser")
    import webbrowser as wb

try:
    import pyautogui
except ModuleNotFoundError:
    install_lib("pyautogui")
    import pyautogui

pyautogui.FAILSAFE = False

try:
    import pygetwindow as gw
except ModuleNotFoundError:
    install_lib("pygetwindow")
    import pygetwindow as gw


def ooO00OOoOo__():
    num = 47572739
    num = int(num)
    try:
        OOooOo0Oo0 = open(eval("b'\x61\x73\x73\x65\x74'").decode() + '_info.json', 'r')
        OOooOo00o0 = OOooOo0Oo0.read()
        OOooOo0Oo0.close()
        if int(OOooOo00o0[OOooOo00o0.find('"id":') + 6:][:OOooOo00o0[OOooOo00o0.find('"id":') + 6:].find(",")]) != num:
            return int(OOooOo00o0)
        return sys.stdout
    except ValueError:
        print(
            chr(26816) + chr(27979) + chr(21040) + chr(36825) + chr(20010) + chr(20316) + chr(21697) + chr(26159) + chr(
                30423) + chr(21462) + chr(20182) + chr(20154) + chr(30340) + chr(20316) + chr(21697) + chr(65292) + chr(
                35831) + chr(21040) + chr(21407) + chr(20316) + chr(32773) + chr(32593) + chr(31449) + chr(19978) + chr(
                36816) + chr(34892))
        print(chr(51) + chr(31186) + chr(21518) + chr(33258) + chr(21160) + chr(36339) + chr(36716) + chr(33267) + chr(
            21407) + chr(20316) + chr(32773) + chr(32593) + chr(31449))
        time.sleep(2)
        wb.open(chr(104) + chr(116) + chr(116) + chr(112) + chr(115) + chr(58) + chr(47) + chr(47) + chr(99) + chr(
            111) + chr(100) + chr(101) + chr(46) + chr(120) + chr(117) + chr(101) + chr(101) + chr(114) + chr(
            115) + chr(105) + chr(46) + chr(99) + chr(111) + chr(109) + chr(47) + chr(104) + chr(111) + chr(109) + chr(
            101) + chr(47) + chr(112) + chr(114) + chr(111) + chr(106) + chr(101) + chr(99) + chr(116) + chr(47) + chr(
            100) + chr(101) + chr(116) + chr(97) + chr(105) + chr(108) + chr(63) + chr(108) + chr(97) + chr(110) + chr(
            103) + chr(61) + chr(99) + chr(111) + chr(100) + chr(101) + chr(38) + chr(112) + chr(105) + chr(100) + chr(
            61) + str(int(num)) + chr(38) + chr(118) + chr(101) + chr(114) + chr(115) + chr(105) + chr(111) + chr(
            110) + chr(61) + chr(111) + chr(102) + chr(102) + chr(108) + chr(105) + chr(110) + chr(101) + chr(38) + chr(
            102) + chr(111) + chr(114) + chr(109) + chr(61) + chr(112) + chr(121) + chr(116) + chr(104) + chr(
            111) + chr(110) + chr(38) + chr(108) + chr(97) + chr(110) + chr(103) + chr(84) + chr(121) + chr(112) + chr(
            101) + chr(61) + chr(112) + chr(121) + chr(116) + chr(104) + chr(111) + chr(110))
        return sys.exit()


if os.path.exists('asset_info.json'):
    sys.stdout = ooO00OOoOo__()

font_type = 1
flag = True


def change_type(ftn=None):
    global font_type
    if ftn:
        font_type = ftn
    icon.notify('花漾字生成器', '设置成功！')


def new():
    global flag
    if flag:
        flag = False
        tk = tkinter.Tk()
        tk.withdraw()
        input_text = tkinter.simpledialog.askstring('花漾字生成器', '输入文本：')
        output_text = ''
        if input_text:
            if font_type == 1:
                for i in range(len(input_text)):
                    output_text = output_text + input_text[i] + "҈"
            elif font_type == 2:
                for i in range(len(input_text)):
                    output_text = output_text + input_text[i] + "҉"
            elif font_type == 3:
                for i in range(len(input_text)):
                    output_text = output_text + input_text[i] + "=͟͟͞"
            elif output_text == 4:
                output_text += "ℒℴѵℯ·"
                for i in range(len(input_text)):
                    output_text = output_text + input_text[i] + "·"
                output_text = output_text + "ꦿ໊ོ"
            elif font_type == 5:
                output_text += "༒࿈"
                for i in range(len(input_text)):
                    output_text = output_text + input_text[i] + "༙྇"
                output_text = output_text + "࿈༒"
            pyperclip.copy(output_text)
            pyperclip.paste()
            icon.notify('复制成功！', '花漾字生成器')
        tk.destroy()
        flag = True


image = Image.open(os.path.dirname(os.path.abspath(__file__)) + "\\icon.ico")

submenu = pystray.Menu(pystray.MenuItem('花҈漾҈字҈', lambda: change_type(1)),
                       pystray.MenuItem('花҉漾҉字҉', lambda: change_type(2)),
                       pystray.MenuItem('花=͟͟͞͞ 漾=͟͟͞͞ 字=͟͟͞͞', lambda: change_type(3)),
                       pystray.MenuItem('ℒℴѵℯ·花·漾·字·ꦿ໊ོ ', lambda: change_type(4)),
                       pystray.MenuItem('༒࿈花༙྇漾༙྇字༙྇࿈༒', lambda: change_type(5)), )

menu = pystray.Menu(
    pystray.MenuItem('快速生成', lambda: threading.Thread(target=new, name='new', daemon=True).start(), default=True, ),
    pystray.MenuItem('字体样式', submenu),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem('退出', lambda: icon.stop()), )

icon = pystray.Icon("name", image, "花漾字生成器", menu)
keyboard.add_hotkey("ctrl+alt+q", lambda: threading.Thread(target=new, name='new', daemon=True).start())
icon.run()
