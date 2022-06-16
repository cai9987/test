from time import sleep

from 修改密码.base.base import Base
from 修改密码 import page


class PageLogin(Base):
    def page_input_old_password(self, input_old_password):
        self.base_input(page.input_old_password, input_old_password)

    def page_input_new_password(self, input_new_password):
        self.base_input(page.input_new_password, input_new_password)

    def page_again_input_new_password(self, again_input_new_password):
        self.base_input(page.again_input_new_password, again_input_new_password)

    def page_ok_btn(self):
        self.base_click(page.password_btn)

    def page_clear(self):
        self.base_click(page.password_clear)

    def page_input_new_password_err_text(self):
        return self.base_get_text(page.input_new_password_err_text)

    def page_again_input_new_password_err_text(self):
        return self.base_get_text(page.again_input_new_password_err_text)

    def page_up_err_text(self):
        return self.base_get_text(page.up_err_text)

    def page_get_image(self):
        self.base_get_image()

    def page_password(self, input_old_password, input_new_password, again_input_new_password):
        self.page_input_old_password(input_old_password)
        self.page_input_new_password(input_new_password)
        self.page_again_input_new_password(again_input_new_password)
        sleep(3)
        self.page_ok_btn()
