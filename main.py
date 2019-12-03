from src.lyrtim import LyricsToImages
import src.manualVocalSeparation as mVS

LTI = LyricsToImages()
# #LTI.getLyrics("NLE Choppa")
LTI.getImages()
# #LTI.getAudio()
lyrics = LTI.compileVideo()
mVS.playback("/home/johk/Projects/LyricsToImages/songs/_-3W0e7aI0gAg.mkv", lyrics)