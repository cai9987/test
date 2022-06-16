from time import sleep

from 报名任务.base.base import Base
from 报名任务 import page


class PageLogin(Base):
    def page_task_sign(self):
        self.base_click(page.task_sign)

    def page_task_want_time(self, task_want_time):
        self.base_input(page.task_want_time, task_want_time)

    def page_task_want_money(self, task_want_money):
        self.base_input(page.task_want_money, task_want_money)

    def page_task_dir(self,task_dir):
        self.base_input(page.task_dir, task_dir)

    def page_task_ok_btn(self):
        self.base_click(page.task_ok_btn)

    def page_time_err_text(self):
        return self.base_get_text(page.time_err_text)

    def page_money_err_text(self):
        return self.base_get_text(page.money_err_text)

    def page_get_image(self):
        self.base_get_image()

    def page_task_ok(self, task_want_time, task_want_money, task_dir):
        self.page_task_sign()
        self.page_task_want_time(task_want_time)
        self.page_task_want_money(task_want_money)
        self.page_task_dir(task_dir)
        sleep(3)
        self.page_task_ok_btn()
