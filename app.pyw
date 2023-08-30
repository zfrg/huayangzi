import os
import sys
import time
import tkinter
import tkinter.simpledialog
import webbrowser as wb
import threading


def install_lib(lib_name):
    os.system("\"" + sys.executable + "\" -m pip install --default-timeout=1688 " + lib_name)


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
    except Exception:
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

threads = []
text = ''
final_text = ''
font_type = 1


def on_quit_clicked():
    icon.stop()
    sys.exit()


def change_type(n=None):
    global font_type
    if n:
        font_type = n
    icon.notify('花漾字生成器', '设置成功！')


def new():
    global text, final_text, font_type
    tk = tkinter.Tk()
    tk.withdraw()
    text = tkinter.simpledialog.askstring('花漾字生成器', '文字')
    final_text = ''
    if text:
        if font_type == 1:
            for i in range(len(text)):
                final_text = final_text + text[i] + "҈"
        elif font_type == 2:
            for i in range(len(text)):
                final_text = final_text + text[i] + "҉"
        elif font_type == 3:
            for i in range(len(text)):
                final_text = final_text + text[i] + "=͟͟͞"
        elif font_type == 4:
            final_text = "ℒℴѵℯ·"
            for i in range(len(text)):
                final_text = final_text + text[i] + "·"
            final_text = final_text + "ꦿ໊ོ"
        pyperclip.copy(final_text)
        icon.notify('复制成功！', '花漾字生成器')
    tk.destroy()


image = Image.open("Icon.ico")

submenu = pystray.Menu(pystray.MenuItem('花҈漾҈字҈', lambda: change_type(1)),
                       pystray.MenuItem('花҉漾҉字҉', lambda: change_type(2)),
                       pystray.MenuItem('花=͟͟͞͞ 漾=͟͟͞͞ 字=͟͟͞͞ ', lambda: change_type(3)),
                       pystray.MenuItem('ℒℴѵℯ·花·漾·字·ꦿ໊ོ ', lambda: change_type(4)),)

menu = pystray.Menu(
    pystray.MenuItem('快速生成', lambda: threading.Thread(target=new, name='new').start(), default=True),
    pystray.MenuItem('字体样式', submenu),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem('退出', on_quit_clicked), )

icon = pystray.Icon("name", image, "花漾字生成器", menu)
icon.run()
