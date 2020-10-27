#!/usr/bin/python3

#########################################################
# Nama file: AudioPlayer1.py
#########################################################

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

class MainForm(QWidget):  
   def __init__(self):
      super().__init__()      
      self.player = QMediaPlayer(self)      
      self.setupUi()
      
   def setupUi(self):
      self.resize(250, 150)
      self.move(300, 300)
      self.setWindowTitle('Audio Player')
      
      self.label1 = QLabel('Progress')
      self.progressSlider = QSlider(Qt.Horizontal)
      self.label2 = QLabel('Volume')
      self.volumeSlider = QSlider(Qt.Horizontal)
      self.volumeSlider.setValue(100)
      
      grid = QGridLayout()
      grid.addWidget(self.label1, 0, 0)
      grid.addWidget(self.progressSlider, 0, 1)
      grid.addWidget(self.label2, 1, 0)
      grid.addWidget(self.volumeSlider, 1, 1)           
      
      self.openButton = QPushButton('Open')
      self.playButton = QPushButton('Play')
      self.playButton.setEnabled(False)
      self.pauseButton = QPushButton('Pause')
      self.pauseButton.setEnabled(False)
      self.stopButton = QPushButton('Stop')
      self.stopButton.setEnabled(False)
      
      hbox = QHBoxLayout()
      hbox.addWidget(self.openButton)
      hbox.addWidget(self.playButton)
      hbox.addWidget(self.pauseButton)
      hbox.addWidget(self.stopButton)      
      hbox.addStretch()
                  
      layout = QVBoxLayout()
      layout.addLayout(grid)
      layout.addLayout(hbox)
      self.setLayout(layout)
      
      self.openButton.clicked.connect(self.openButtonClick)
      self.playButton.clicked.connect(self.playButtonClick)
      self.pauseButton.clicked.connect(self.pauseButtonClick)
      self.stopButton.clicked.connect(self.stopButtonClick)
      
      self.progressSlider.sliderMoved.connect(self.progressSliderMoved)
      self.volumeSlider.sliderMoved.connect(self.volumeSliderMoved)
      
      self.player.positionChanged.connect(self.playerPositionChanged)
      self.player.durationChanged.connect(self.playerDurationChanged)
   
   def setPlayingMode(self, mode):
      if mode:
         self.playButton.setEnabled(False)
         self.pauseButton.setEnabled(True)
         self.stopButton.setEnabled(True)
      else:
         self.playButton.setEnabled(True)
         self.pauseButton.setEnabled(False)
         self.stopButton.setEnabled(False)
   
   def openButtonClick(self):      
      import os
      fileName = QFileDialog.getOpenFileName(
        self, 
        'Open', 
        os.curdir, 
        'MP3 Files (*.mp3)', '*.mp3')
      if len(fileName[0]) > 0:
         self.player.setMedia(
           QMediaContent(QUrl.fromLocalFile(fileName[0])))
         if self.player.state() == QMediaPlayer.PlayingState:
            self.player.stop()         
         self.setPlayingMode(False)
      
   def playButtonClick(self):
      self.player.play()
      self.setPlayingMode(True)      

   def pauseButtonClick(self):
      self.player.pause()
      self.setPlayingMode(False)

   def stopButtonClick(self):
      self.player.stop()
      self.setPlayingMode(False)

   def progressSliderMoved(self):
      self.player.setPosition(self.progressSlider.value())

   def volumeSliderMoved(self):
      self.player.setVolume(self.volumeSlider.value())

   def playerPositionChanged(self, position):
      self.progressSlider.setValue(position)

   def playerDurationChanged(self, position):
      self.progressSlider.setMaximum(position)

if __name__ == '__main__':
   a = QApplication(sys.argv)

   form = MainForm()
   form.show()
   
   a.exec_()
