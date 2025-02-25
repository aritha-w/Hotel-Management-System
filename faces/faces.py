def main():
    ex=input()
    convert(ex)


def convert(to):
    to=to.replace(":)","🙂").replace(":(","🙁")
    print(to)

main()
