from tasks.base.ui import UI
from tasks.login.assets.assets_login_agreement import *
from tasks.login.assets.assets_login_popup import Game_Main_Announcement, Game_In_Advertise, Daily_Bonus


class GameInPopup(UI):
    def handle_game_popup(self):
        """
        Returns:
            bool: If clicked
        """
        # CN user agreement popup
        if self.appear_then_click(Game_Main_Announcement, interval=3):
            return True
        if self.appear_then_click(Game_In_Advertise, interval=3):
            return True
        if self.appear_then_click(Daily_Bonus, interval=3):
            return True

        return False
    def is_game_popup(self):
        """
        Returns:
            bool: If clicked
        """
        # CN user agreement popup
        if self.appear(Game_Main_Announcement, interval=3):
            return False
        if self.appear(Game_In_Advertise, interval=3):
            return False
        if self.appear(Daily_Bonus, interval=3):
            return False

        return True

