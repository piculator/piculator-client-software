from typing import List, Callable
import app


class Function:
    def __init__(self, name: str, desc: str, icon_path: str, login_required: bool, keywords: List[str], fun: Callable,
                 guest_fallback: Callable):
        self.name = name
        self.desc = desc
        self.icon_path = icon_path
        self.login_required = login_required
        self.keywords = keywords
        self.fun = fun
        self.guest_fallback = guest_fallback

    def search(self, txt):
        return self.name.find(txt) != -1 or self.desc.find(txt) != -1 or txt in self.keywords

    def execute(self):
        if self.login_required and app.login_manager.is_guest:
            self.guest_fallback()
        else:
            self.fun()

    def generate_tile(self):
        pass
