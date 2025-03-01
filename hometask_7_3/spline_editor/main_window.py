from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox
from PyQt5.QtGui import QKeySequence

from spline_view import SplineView
from control_panel import ControlPanel

class MainWindow(QMainWindow):
     def __init__(self, parent = None):
        super().__init__(parent)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        about_menu = menubar.addMenu('About')
        
        save_action = file_menu.addAction('Save')
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.on_save_triggered)

        open_action = file_menu.addAction('Open')
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.on_open_triggered)

        close_action = file_menu.addAction('Close')
        close_action.setShortcut("Alt+F4")
        close_action.triggered.connect(self.close)
        
        undo_action = edit_menu.addAction('Undo')
        undo_action.setShortcut(QKeySequence.Undo) #dont working only with Ctrl+Z - non standart shortcuts working well
        undo_action.triggered.connect(self.on_undo_triggered)

        redo_action = edit_menu.addAction("Redo")
        redo_action.setShortcut('Shift+Ctrl+Z') #dont working only with Ctrl+Z - non standart shortcuts working well
        redo_action.triggered.connect(self.on_redo_triggered)

        about_action = about_menu.addAction("About")
        about_action.setShortcut("F1")
        about_action.triggered.connect(self.on_about_triggered)

        spline_view = SplineView()
        self.setCentralWidget(spline_view)

        control_panel = ControlPanel(spline_view.maximumWidth(), spline_view.maximumHeight())
        self.statusBar().addWidget(control_panel)

        control_panel.state_changed.connect(spline_view.set_current_knot)
        spline_view.current_knot_changed.connect(control_panel.set_state)
        # spline_view.undo_action_triggered.connect(spline_view.set_previous_spline)

     def on_save_triggered(self):
         pass

     def on_open_triggered(self):
         pass

     def on_undo_triggered(self):
        #  self.spline = SplineView()
        #  self.spline.set_previous_spline()
         print('activated undo')

     def on_redo_triggered(self):
         print('activated redo')

     def on_about_triggered(self):
            widget = QMessageBox(self)
            widget.information(self, 'Information', 'Spline editor v1.0\nAuthor: rom101rom\nThis is desktop simple line editor for drawing lines with approximation')
