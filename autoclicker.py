import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = float(input("请输入延迟时间（建议为1）："))  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[运行中]")
    elif key == pause_key:
        pause = True
        print("[暂停]")
    elif key == exit_key:
        running = False
        print("[退出]")


def display_controls():
    print("// 连点器 by iSayChris")
    print("// - 设置： ")
    print("\t 每" + str(delay) + '秒' + '点1次\n')
    print("// - 控制：")
    print("\t F1 = 开始")
    print("\t F2 = 暂停")
    print("\t ESC = 退出")
    print("-----------------------------------------------------")
    print('按下F1以开始...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
