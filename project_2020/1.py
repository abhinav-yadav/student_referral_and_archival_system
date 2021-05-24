import filetype

def main():
    kind = filetype.guess('media/files/1.jpg')
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

class a():
    def pig(self):
        a=main()
        return a

c=a()
print(c.pig())
