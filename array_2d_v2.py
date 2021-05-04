from PIL import Image, ImageFont, ImageDraw 


# STATIC

title_font = ImageFont.truetype('PlayfairDisplay-Italic-VariableFont_wght.ttf', 20)

#photo ONLY - STATIC
LEFT_RIGHT=15
DOWN_UP=35 
step=18

title_text = [
    [35,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0],
    [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10],
]




def once(array,nameOfFile):
    print(array)
    currentStep=0

    my_image = Image.open("src.jpg")
    image_editable = ImageDraw.Draw(my_image)


    while(currentStep<len(array)):

        # space between each font 
        next = step*currentStep

        image_editable.text((LEFT_RIGHT,DOWN_UP+next), str(array[currentStep]), (0, 0, 0), font=title_font)

        # while loop update
        currentStep=currentStep+1

    my_image.save(f"./iterations/result{nameOfFile}.jpg")

iteration=0
while(iteration<len(title_text)):
    once(title_text[iteration],iteration)
    print(iteration)
    iteration=iteration+1
