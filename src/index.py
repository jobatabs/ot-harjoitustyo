from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title('DoseCalculator')
    window.geometry("300x150")
    window.resizable(False, False)
    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == '__main__':
    main()
