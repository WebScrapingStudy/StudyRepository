import pyautogui as auto
import config

def logout_detect():
    """
    로그인창에 있는지 검사를 한후 로그인을 시도합니다.
    :return: None
    """
    login_btn = auto.locateOnScreen('btn/login.png')
    if login_btn is not None:
        login_center = auto.center(login_btn)
        id_point = login_btn[0] - login_btn[2] * 3, login_btn[1]  + 10
        auto.click(id_point)
        auto.typewrite(config.id + '\t', interval=0.2)
        auto.typewrite(config.pw, interval=0.2)
        auto.click(login_center, interval=config.login_delay)
        print('login as :'+config.id)

def view_btn():
    """
    수강신청 버튼 좌표를 반환합니다.
    :return: pyautogui.Point
    """
    view_btn = auto.locateOnScreen('btn/view.png')
    if view_btn is not None:
        view_btn = auto.center(view_btn)
        auto.click(view_btn, interval=config.view_delay)
    else:
        print('view btn error')
    return view_btn

def num_btn():
    """
    학수번호 버튼 좌표를 반환합니다.
    :return: pyautogui.Point
    """
    num_btn = auto.locateOnScreen('btn/number.png')
    if num_btn is not None:
        num_btn = auto.center(num_btn)
        auto.click(num_btn, interval=1)
    else:
        print('num btn error')
    return num_btn

def apply_btn():
    """
    빠른수강 버튼 좌표와 학수번호 입력창 좌표를 반환합니다.
    :return: pyautogui.Point, tuple(x,y)
    """
    apply_box = auto.locateOnScreen('btn/apply.png')
    if apply_box is not None:
        apply_btn = auto.center(apply_box)
        text_area = apply_box[0] - apply_box[2] * 2, apply_btn[1]
        auto.click(apply_btn, interval=1)
    else:
        print('apply btn error')
    return apply_btn, text_area

def close_btn():
    """
    빠른수강 버튼을 눌렀을때 나타나는 팝업창의 닫기버튼의 좌표를 반환합니다.
    :return: pyautogui.Point
    """
    close_btn = auto.locateOnScreen('btn/close.png')
    if close_btn is not None:
        close_btn = auto.center(close_btn)
        auto.click(close_btn, interval=1)
    else:
        print('close btn error')
    return close_btn