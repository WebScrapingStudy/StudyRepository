import pyautogui as auto
import datetime
import config
import funtion

def main():
    # datetime obj create
    d = datetime.datetime

    # login
    if config.login_funtion:
        funtion.logout_detect()

    # init point parse
    view_btn = funtion.view_btn()
    num_btn = funtion.num_btn()
    apply_btn, text_area = funtion.apply_btn()
    close_btn = funtion.close_btn()

    # load course
    f = open('course.txt','r')
    courses = f.read().split()
    print(courses)
    f.close()

    while True:
        if config.login_funtion and d.now().minute % config.login_interval == 0:
            funtion.logout_detect()
            auto.click(view_btn, interval=0.3)
            auto.click(num_btn, interval=0.2)

        for course in courses:
            #auto.click(view_btn, interval=0.3)
            #auto.click(num_btn, interval=0.2)
            auto.click(text_area, interval=0.1)
            auto.typewrite(course, interval=0.05)
            auto.click(apply_btn, interval=0.8)
            auto.click(close_btn)
            now = d.now().strftime('%H:%M:%S')
            print(now+':Apply to '+course)

if __name__ == '__main__':
    main()

