from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def arvuta_click(self, event=None):
        pikkus = self.view.num_pikkus.get().strip()
        laius = self.view.num_laius.get().strip()
        r1 = self.model.get_area(pikkus, laius)
        r2 = self.model.get_perimeter(pikkus, laius)
        self.view.text_box.config(state='normal')
        self.view.text_box.delete(1.0, 'end')
        self.view.text_box.insert('insert', str(r1) + '\n' + str(r2))
        self.view.text_box.see('end')
        self.view.text_box.config(state='disabled')
        self.clear_text()

    def clear_text(self):
        self.view.num_laius.delete(0, 'end')
        self.view.num_pikkus.delete(0, 'end')
