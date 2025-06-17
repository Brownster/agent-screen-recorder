import time
import threading
import requests
from mss import mss

class ScreenRecorder:
    def __init__(self, upload_url: str, interval: float = 1.0):
        self.upload_url = upload_url
        self.interval = interval
        self.running = False
        self.thread = None
        self.sct = mss()

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._capture_loop)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _capture_loop(self):
        while self.running:
            screenshot = self.sct.shot(output='screenshot.png')
            with open(screenshot, 'rb') as img:
                requests.post(self.upload_url, files={'file': img})
            time.sleep(self.interval)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Simple Screen Recorder Agent')
    parser.add_argument('--upload', required=True, help='Upload URL for screenshots')
    args = parser.parse_args()

    recorder = ScreenRecorder(upload_url=args.upload)
    try:
        recorder.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        recorder.stop()
