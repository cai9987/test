from time import sleep

from 发布任务.base.base import Base
from 发布任务 import page


class PageLogin(Base):
    def page_task_btn(self):
        self.base_click(page.task_btn)

    def page_input_task_title(self, title):
        self.base_input(page.task_title, title)

    def page_task_date_click(self):
        self.base_click(page.task_date_click)

    def page_task_date(self):
        self.base_click(page.task_date)

    def page_input_task_money_min(self, min_money):
        self.base_input(page.task_money_min, min_money)

    def page_input_task_money_max(self, max_money):
        self.base_input(page.task_money_max, max_money)

    def page_input_task_want_day(self, want_day):
        self.base_input(page.task_want_day, want_day)

    def page_input_task_people_sum(self, people_sum):
        self.base_input(page.task_people_sum, people_sum)

    def page_input_task_describe(self, describe):
        self.base_input(page.task_describe, describe)

    def page_task_save_btn(self):
        self.base_click(page.task_save_btn)

    def page_titLe_err_text(self):
        return self.base_get_text(page.task_titLe_err_text)

    def page_field_err_text(self):
        return self.base_get_text(page.task_field_err_text)

    def page_err_text(self):
        # title_err_text = self.page_titLe_err_text()
        # field_err_text = self.page_field_err_text()
        a = (self.page_titLe_err_text(), self.page_field_err_text())
        res = list(filter(None, a))
        return res

    # def page_err_text(self):
    #     if self.page_titLe_err_text() is None:
    #         if self.page_field_err_text() is None:
    #             print("正常运行")
    #         else:
    #             msg = self.page_field_err_text()
    #             return msg
    #     else:
    #         msg = self.page_field_err_text()
    #         return msg
    #
    # def page_err_up_text(self):
    #     return self.base_get_text(page.login_err_up_text)
    #
    # def page_login_if_quit(self):
    #     return self.base_if_success(page.login_link)

    def page_get_image(self):
        self.base_get_image()

    def page_task(self, title, min_money, max_money, want_day, people_sum, describe):
        self.page_input_task_title(title)
        self.page_task_date_click()
        self.page_task_date()
        self.page_input_task_money_min(min_money)
        self.page_input_task_money_max(max_money)
        self.page_input_task_want_day(want_day)
        self.page_input_task_people_sum(people_sum)
        self.page_input_task_describe(describe)
        sleep(5)
        self.page_task_save_btn()
        sleep(1)
