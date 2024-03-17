# html generator code
with open("htmlpage.html", "w") as generate:
    generate.write("<html>\n<body style='padding: 1cm;'>\n<p>\nBread, the simple yet essential staple of countless diets around the world, has a remarkable history dating back millennia. This humble foodstuff, made from basic ingredients like flour, water, yeast, and salt, has sustained civilizations, offering sustenance and nourishment through the ages. From the crusty baguettes of France to the soft, fluffy naan of India, bread takes on a multitude of forms, textures, and flavors, reflecting the diverse cultures that have perfected its creation.\n<br/>In ancient Egypt, bread held such significance that it was often used as currency and even offered as a form of payment to workers who built the great pyramids. The skill of breadmaking was highly revered, with bakers passing down their secret recipes from generation to generation. The process of breadmaking itself is a fascinating blend of science and art, as yeast microorganisms ferment the dough, producing carbon dioxide gas that causes it to rise. The result is the airy, porous texture that bread lovers crave. The aroma of freshly baked bread wafting through the air is enough to make anyone's mouth water.\n<br/>Throughout history, bread has played a central role in religious rituals and symbolism. In Christianity, the sacrament of the Eucharist involves the consumption of bread as a representation of the body of Christ. The act of breaking bread together has also been a universal symbol of communion and unity among people of different backgrounds and beliefs. It is a testament to bread's unifying power, transcending cultural and religious boundaries.\n<br/>In recent years, the art of breadmaking has experienced a resurgence, with artisanal bakeries and home bakers experimenting with unique ingredients and techniques to create bread that goes beyond the ordinary. Sourdough bread, with its tangy flavor and chewy crust, has become a trendy choice for many. People are also exploring gluten-free and alternative grain options, ensuring that bread remains a beloved part of our diets, regardless of dietary restrictions.\n<br/>In conclusion, bread is far more than just a simple food. It is a symbol of history, culture, and sustenance. Whether it's a freshly baked bagel, a warm slice of garlic bread, or a traditional pita, bread is a testament to the creativity and innovation of humanity throughout the ages. So, let us celebrate this versatile and beloved food that has been kneaded, risen, and baked to perfection for thousands of years. In our modern world, where trends come and go, bread remains a timeless and comforting staple on our tables, a source of nourishment, and a symbol of togetherness.\n</p>\n</body>\n</html>")



# main code
def switch(ch, text, portion_to_format):
    if ch == 1:
        formatted_text = text.replace(portion_to_format, "<mark>"+portion_to_format+"</mark>")
        return formatted_text
    elif ch == 2:
        formatted_text = text.replace(portion_to_format, "<b>"+portion_to_format+"</b>")
        return formatted_text
    elif ch == 3:
        formatted_text = text.replace(portion_to_format, "<u>"+portion_to_format+"</u>")
        return formatted_text
    elif ch == 4:
        formatted_text = text.replace(portion_to_format, "<mark><b><u>"+portion_to_format+"</u></b></mark>")
        return formatted_text
    # elif ch == 5:
    #     formatted_text = text.replace("<mark>","")
    #     formatted_text = text.replace("</mark>","")
    #     return formatted_text
    # elif ch == 6:
    #     formatted_text = text.replace("<b>","")
    #     formatted_text = text.replace("</b>","")
    #     return formatted_text
    # elif ch == 7:
    #     formatted_text = text.replace("<u>","")
    #     formatted_text = text.replace("</u>","")
    #     return formatted_text
    # elif ch == 8:
    #     formatted_text = text.replace("<mark>","")
    #     formatted_text = text.replace("</mark>","")
    #     formatted_text = text.replace("<b>","")
    #     formatted_text = text.replace("</b>","")
    #     formatted_text = text.replace("<u>","")
    #     formatted_text = text.replace("</u>","")
    #     return formatted_text
    else:
        print("Invalid choice")

print("*********Menu*********")
print("What do you want to do?")
print("1  :  Highlight specified text")
print("2  :  Make specified text bold")
print("3  :  Underline specified text")
print("4  :  Apply all formatting on specified text")
# print("5  :  Remove highlights on any text")
# print("6  :  Remove boldness of any text")
# print("7  :  Remove underlines below any text")
# print("8  :  Remove all formatting")
choice = int(input("Enter you choice : "))


with open("htmlpage.html" , "r") as page:
    s = page.read()

with open("htmlpage.html" , "w") as page:
    page.write(switch(choice, s, input("State the text within this file that you want to format? ")))