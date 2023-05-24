import pyautogui
import time
from pynput.keyboard import Key, Controller
import os
def locateOnScreenshot(imagearray, minSearchTime=0, **kwargs):
				
				
	imCount = len(arr)
	"""TODO - rewrite this
	minSearchTime - amount of time in seconds to repeat taking
	screenshots and trying to locate a match.  The default of 0 performs
	a single search.
	"""
	count = 0
	start = time.time()
	screenshotIm = pyautogui.screenshot(region=(1000,920,180,30)) # the locateAll() function must handle cropping to return accurate coordinates, so don't pass a region here.
	screenshotIm.save(r"Ailments\\Burns\\currentScreen.png")
	for image in imagearray:
		#print(image)
		#print(image)
		while True:
			try:
				#start = time.time()
				retVal = pyautogui.locate(image, screenshotIm, **kwargs, step = 1)
				#print("Time taken to check image",(time.time() - start)*1000)
				try:
					screenshotIm.fp.close()
				except AttributeError:
					# Screenshots on Windows won't have an fp since they came from
					# ImageGrab, not a file. Screenshots on Linux will have fp set
					# to None since the file has been unlinked
					pass
				if retVal:

					#print(image)
					#print(image)
					return retVal
				elif  time.time() - start > minSearchTime and count >= imCount-1:
					return retVal

				else:
					count +=1
					break
			except pyautogui.ImageNotFoundException:
				if time.time() - start > minSearchTime:
					if USE_IMAGE_NOT_FOUND_EXCEPTION:
						raise
					else:
						return None
keyboard = Controller()
arr = []
cwd = os.getcwd()
in_directory = cwd+"\\Ailments"
for filename in os.listdir(in_directory):
	if filename.endswith(".png"):
		arr.append(in_directory+"\\"+filename)
imCount = len(arr)
print(arr)

while True:
	#time.sleep(1)

	# start_time = time.time()
	# s = locateOnScreenshot(arr, confidence=0.9	)
	# if(s != None):
	# 	print(s)
	# print(time.time()-start_time)
	print(pyautogui.position())
