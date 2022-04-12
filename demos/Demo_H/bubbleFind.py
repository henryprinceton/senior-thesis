import numpy as np
import cv2

box_template = cv2.imread('./assets/box_sanders.jpg', 0)
bubble_template = cv2.imread('./assets/ballot_bubble_empty.jpg', 0)

box_h, box_w = box_template.shape
bubble_h, bubble_w = bubble_template.shape

method = cv2.TM_CCOEFF
# cv2.TM_CCOEFF
# cv2.TM_CCOEFF_NORMED
# cv2.TM_CCORR
# cv2.TM_CCORR_NORMED
# cv2.TM_SQDIFF
# cv2.TM_SQDIFF_NORMED

img_match = cv2.imread('./assets/ballot.jpg', 0)
img_display = cv2.imread('./assets/ballot.jpg')

img_h, img_w = img_match.shape

# find where box template is within original image
box_result = cv2.matchTemplate(img_match, box_template, method)
box_min_val, box_max_val, box_min_loc, box_max_loc = cv2.minMaxLoc(box_result)
box_location = box_max_loc

# find where bubble template is within box template
bubble_result = cv2.matchTemplate(box_template, bubble_template, method)
bubble_min_val, bubble_max_val, bubble_min_loc, bubble_max_loc = cv2.minMaxLoc(bubble_result)
bubble_location = bubble_max_loc

# find top_left and bottom_right of rectangle on original image

box_right = box_location[0] + box_w
box_bottom = box_location[1] + box_h

bubble_right = bubble_location[0] + bubble_w
bubble_bottom = bubble_location[1] + bubble_h

final_right = box_right - (box_w - bubble_right)
final_bottom = box_bottom - (box_h - bubble_bottom)
final_top = final_bottom - bubble_h
final_left = final_right - bubble_w
final_top_left = (final_left, final_top)
final_bottom_right = (final_right, final_bottom)
cv2.rectangle(img_display, final_top_left, final_bottom_right, (0, 0, 255), 5)
cv2.imshow("bubble detection", img_display)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print("image dimensions: " + str((img_w, img_h)))
# print("box location: " + str(box_location))
# print("bubble location: " + str(bubble_location))
# print("final location: " + str(final_bottom_right))

# code structure and opencv fundamentals were taken from the following tutorial series:
# https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn