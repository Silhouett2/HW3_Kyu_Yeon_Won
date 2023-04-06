text3 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"

text = input("문자열을 입력하세요 \n")
def reverse_words (text):    
    spl_textlist = text.split(' ')
    for i in range(len(spl_textlist)):
        spllist = list(spl_textlist[i])
        spllist.reverse()
        print("".join(spllist), end = ' ')

text2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
reverse_words (text)

def main():

    print("")

 

if __name__ == '__main__':

 

    main()

