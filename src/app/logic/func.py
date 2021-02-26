from typing import List, Callable, Union
from app.ui.controls.tile_factory import make_tile


class Function:
    def __init__(self, name: str, desc: str, icon_path: str, login_required: bool, keywords: List[str], fun: Callable,
                 guest_fallback: Union[Callable, None] = None):
        self.name = name
        self.desc = desc
        self.icon_path = icon_path
        self.login_required = login_required
        self.keywords = keywords
        self.fun = fun
        self.guest_fallback = guest_fallback
        self.column = self.row = None
        self.tile = None

    def search(self, txt: str):
        txt = txt.lower()
        if self.name.lower().find(txt) != -1 or self.desc.lower().find(txt) != -1:
            return True
        else:
            for k in self.keywords:
                if txt in k.lower():
                    return True
            return False

    def execute(self):
        from app import myapp
        if self.login_required and myapp.login_manager.is_guest:
            self.guest_fallback()
        else:
            self.fun()

    def generate_tile(self):
        self.tile = make_tile(self.icon_path, self.name, self.desc, self.execute)
