from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from superqt import QLabeledSlider


class verticalSliders(QMainWindow):
    def __init__(self, sliders=None):
        super().__init__()
        overall_vbox = QVBoxLayout()
        widget = QWidget()

        # figure stuff
        self._fig = Figure()
        self._canvas = FigureCanvas(self._fig)
        self._canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._canvas.setFocusPolicy(Qt.ClickFocus)
        self._canvas.setFocus()
        self._canvas.setParent(widget)

        self.toolbar = NavigationToolbar(self._canvas, self)
        # self.toolbar.setOrientation(Qt.Orientation.Vertical)
        overall_vbox.addWidget(self.toolbar)
        overall_vbox.addWidget(self._canvas)

        # layout2.addWidget(self._canvas)
        self.sliders = []
        for s in sliders:
            # do interpreting of sliders a la mpl-interactions here
            # slider = QLabeledDoubleSlider(Qt.Orientation.Horizontal)
            slider = QLabeledSlider(Qt.Orientation.Horizontal)
            slider.setRange(s[0], s[1])
            overall_vbox.addWidget(slider)
            self.sliders.append(slider)
        # overall_vbox.addWidgets(self.sliders)
        # layout1.addLayout(layout2)

        widget.setLayout(overall_vbox)
        self.setCentralWidget(widget)

    def get_fig(self) -> Figure:
        return self._fig

    def get_canvas(self):
        return self._canvas

    def draw(self):
        self._canvas.draw()

    # def keyPressEvent(self, event):
    #     print('here? -sdfsd')
    #     super().keyPressEvent(event)
    # def eventFilter(self, object, event: QEvent):
    # TODO: use this always get keyevents in mpl events
    # print(event.type)
    # inspired by
    # https://github.com/matplotlib/matplotlib/blob/v3.5.1/lib/matplotlib/backends/backend_qt.py#L360
    # if event.type() == QEvent.KeyPress:
    #     key = event.key()
    #     try:
    #         self._key = SPECIAL_KEYS[key]
    #     except KeyError:
    #         if key > sys.maxunicode:
    #             return None

    #         self._key = chr(key).lower()
    # elif event.type() == QEvent.KeyRelease and not event.isAutoRepeat():
    #     self._key = None
    # elif event.type() == QEvent.Scroll:
    #     if event.keys() is None:
    #         event.setK
    #         QEvent()
    # return super().eventFilter(object, event)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     app.exec()
