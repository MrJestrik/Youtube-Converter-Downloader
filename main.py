from ui_main_window_updated import Ui_Form
from PySide6 import QtCore
from PySide6.QtCore import (Qt)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import *
from pytube import YouTube
from tkinter import Tk
from youtubesearchpython import VideosSearch
import sys, os, threading, time, ctypes

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.BG.setGraphicsEffect(self.shadow)

        self.show()

        self.ui.Close.clicked.connect(self.close_win)
        self.ui.download.clicked.connect(self.download)
        self.ui.search_video.clicked.connect(self.search_video)
        self.ui.copy_video_id.clicked.connect(self.copy_selected_video)

        self.old_results = None

    def copy_selected_video(self):
        num = 0
        for result in self.old_results['result']:
            if self.ui.results.currentText() == f"{result['title']} | {result['id']}":
                r = Tk()
                r.withdraw()
                r.clipboard_clear()
                r.clipboard_append(result['id'])
                r.update()  # now it stays on the clipboard after the window is closed
                r.destroy()
            num += 1

    def search_video(self):
        results = self.FindYoutubeVideos(self.ui.video_name.text(), self.ui.limit.text())
        self.old_results = results
        self.ui.results.clear()
        [self.ui.results.addItem(f"{i['title']} | {i['id']}") for i in results['result']]

    def YoutubeAudioDownload(self, video_id, output_path, ui):
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(video_url)
        stream = yt.streams.get_audio_only()

        t = self.thread_wait_and_change("smth", self)
        t.start()

        try:
            if output_path != None:
                stream.download(output_path=output_path)
                print(f"{stream.default_filename.replace('.mp4', '.mp3')} was downloaded successfully!")
            else:
                stream.download(output_path=output_path)
                print(f"{stream.default_filename.replace('.mp4', '.mp3')} was downloaded successfully!")
            t.raise_exception()
            t.join()
            self.ui.download.setEnabled(True)
            self.ui.download_prog.setValue(80)
            self.ui.download_stat.setText("Status: Almost there!")
            time.sleep(2)
            self.ui.download_prog.setValue(100)
            self.ui.download_stat.setText("Status: Successfully Downloaded!")
        except:
            print("Failed to download audio!")
            t.raise_exception()
            t.join()
            self.ui.download.setEnabled(True)
            self.ui.download_prog.setValue(100)
            self.ui.download_stat.setText("Status: Download Failed!")

        os.rename(stream.default_filename, stream.default_filename.replace(".mp4", ".mp3"))

    def YoutubeVideoDownload(self, video_id, output_path, ui):
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video = YouTube(video_url)
        video = video.streams.get_highest_resolution()

        t = self.thread_wait_and_change("smth", self)
        t.start()

        try:
            if output_path != None:
                video.download(output_path=output_path)
                print(f"{video.default_filename} was downloaded successfully!")
            else:
                video.download(output_path=output_path)
                print(f"{video.default_filename} was downloaded successfully!")
            t.raise_exception()
            t.join()
            self.ui.download_prog.setValue(80)
            self.ui.download_stat.setText("Status: Almost there!")
            time.sleep(2)
            self.ui.download.setEnabled(True)
            self.ui.download_prog.setValue(100)
            self.ui.download_stat.setText("Status: Successfully Downloaded!")
        except:
            print("Failed to download video!")
            t.raise_exception()
            t.join()
            self.ui.download.setEnabled(True)
            self.ui.download_prog.setValue(100)
            self.ui.download_stat.setText("Status: Download Failed!")

        ui.download.setDisabled(False)

    def FindYoutubeVideos(self, name, limit):
        videosSearch = VideosSearch(query=name, limit=int(limit))
        return videosSearch.result()

    def wait_and_change(self):
        time.sleep(3)
        self.ui.download_prog.setValue(10)
        self.ui.download_stat.setText("Status: Download Started...")
        time.sleep(3)
        self.ui.download_prog.setValue(20)
        self.ui.download_stat.setText("Status: Downloading Bytes...")
        time.sleep(3)
        self.ui.download_prog.setValue(50)
        self.ui.download_stat.setText("Status: Please Wait...")

    class thread_wait_and_change(threading.Thread):
        def __init__(self, name, self2):
            threading.Thread.__init__(self)
            self.name = name
            self.self2 = self2

        def run(self):
            try:
                self.self2.wait_and_change()
            finally:
                pass

        def get_id(self):

            # returns id of the respective thread
            if hasattr(self, '_thread_id'):
                return self._thread_id
            for id, thread in threading._active.items():
                if thread is self:
                    return id

        def raise_exception(self):
            thread_id = self.get_id()
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                             ctypes.py_object(SystemExit))
            if res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                print('Exception raise failure')

    def download(self):
        if os.path.isdir(self.ui.download_folder.text()):
            self.ui.download.setEnabled(False)
            if self.ui.video.isChecked():
                self.ui.download_prog.setValue(0)
                self.ui.download_stat.setText("Status: Starting Download...")
                threading.Thread(target=self.YoutubeVideoDownload, args=(self.ui.video_id.text(), self.ui.download_folder.text(), self.ui), daemon=True).start()
            else:
                threading.Thread(target=self.YoutubeAudioDownload, args=(self.ui.video_id.text(), self.ui.download_folder.text(), self.ui), daemon=True).start()
                threading.Thread(target=self.wait_and_change, daemon=True).start()
        else:
            self.ui.download.setEnabled(False)
            if self.ui.video.isChecked():
                self.ui.download_prog.setValue(0)
                self.ui.download_stat.setText("Status: Starting Download...")
                threading.Thread(target=self.YoutubeVideoDownload,
                                 args=(self.ui.video_id.text(), None, self.ui),
                                 daemon=True).start()
                threading.Thread(target=self.wait_and_change, daemon=True).start()
            else:
                threading.Thread(target=self.YoutubeAudioDownload,
                                 args=(self.ui.video_id.text(), None, self.ui),
                                 daemon=True).start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            event.accept()

    def close_win(self):
        self.close()
        sys.exit(0)

def main_window():
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())