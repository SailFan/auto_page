import time
from selenium.webdriver.common.action_chains import ActionChains
import logging
#浏览器页面类，主要用来浏览器页面的控制，包括获取
class PageUtil():
    def __init__(self, page=None,browser_type = "firefox"):
        if page:
            self.driver = page.driver
        else:
            super(PageUtil, self).__init__(browser_type=browser_type)

    #获取当前窗口事件句柄

    @property
    def current_window(self):
        return self.driver.current_window_handle

    #获取标题

    @property
    def title(self):
        return self.driver.title;

    #获取当前地址
    @property
    def current_url(self):
        return self.driver.current_url

    #获取浏览器驱动
    @property
    def get_driver(self):
        return self.driver

    #睡眠一段时间
    def wait(self, seconds=3):
        time.sleep(seconds)

    #执行js代码
    def exectu(self, js, *args):
        self.driver.execute_script(js, *args)

    #移动到指定的元素
    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    # 寻找指定元素
    def find_element(self, *args):
        return self.driver.find_element(*args)

    # 寻找指定的一批元素
    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    #切换窗口
    def switch_to_windows(self, partial_url, partial_title):
        """切换窗口
                    如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
                    如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logging.warning("只有1个window!")
            # logger.warning("只有1个window!")
        elif len(all_windows) ==2:
            other_window = all_windows[all_windows.index(self.current_window)]
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logging.debug(self.driver.current_url, self.driver.title)

    #切换frame页面
    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    #切换alter
    def switch_to_alert(self):
        return self.driver.switch_to.alert