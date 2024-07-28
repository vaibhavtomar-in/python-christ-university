def addBook(bookDict, isbn, title, author, publisher, volume, year_of_publication):
    if(isbn not in bookDict.keys()):
        bookDict[isbn] = {"isbn" : isbn, "title" : title, "author" : author, "publisher" : publisher, "volume" : volume, "year_of_publication" : year_of_publication}
    else:
        print("book already exists")
    return bookDict
def deleteBook(bookDict, isbn):
    if(isbn in bookDict.keys()):
        del bookDict[isbn]
    else:
        print("isbn doesn't exist in the database")
def bookDetail(bookDict, isbn):
    if (isbn in bookDict.keys()):
        return [isbn, bookDict[isbn]["title"], bookDict[isbn]["author"], bookDict[isbn]["publisher"], bookDict[isbn]["volume"], bookDict[isbn]["year_of_publication"] ]
    else :
        print("isbn doesnt exist in the database")
def getByAuthor(bookDict, author):
    result = list()
    for i in bookDict:
        if (bookDict[i]["author"]==author):
            result.append([str(x) + " : " + str(bookDict[i][x]) for x in bookDict[i].keys()])
    if (result!=[]):
        return result
    else :
        print("author not present")
def getByTitle(bookDict, title):
    result = list()
    for i in bookDict:
        if (bookDict[i]["title"]==title):
            result.append([str(x) + " : " + str(bookDict[i][x]) for x in bookDict[i].keys()])
    if (result!=[]):
        return result
    else :
        print("title not present")
def checkAvailability(bookDict, isbn):
    print("book is available ") if isbn in bookDict else print("book is not available ") 
