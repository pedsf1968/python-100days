import random
STARTING_IMAGE_URL = "https://media1.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid=ecf05e47zkkbuhl2gi5prwkdxb5bhofnm3fmm4qiuks0f8ux&ep=v1_gifs_search&rid=200w.webp&ct=g"
LOW_IMAGE_URL = "https://media1.giphy.com/media/JPOaQ5e1ZmEmc/giphy.webp?cid=ecf05e47951wpo78is9odge38wxe67wgr4l4tv1telinhtn5&ep=v1_gifs_search&rid=giphy.webp&ct=g"
HIGH_IMAGE_URL = "https://giphy.com/gifs/viralhog-viral-hog-doggy-shows-perfect-balancing-performance-11JA9axStWivLUyhsB"
OK_IMAGE_URL = "https://media0.giphy.com/media/1xONIE9kieqf4VTX50/giphy.webp?cid=ecf05e47nrzy5ewoti6817zbzkfmfts16aljvmkaqpmzcacy&ep=v1_gifs_search&rid=giphy.webp&ct=g"
MAX_RANGE = 9


class Number:
    def __init__(self, max_range=MAX_RANGE):
        self.max_range = max_range
        self.value = random.randint(0, max_range)

    def reset_number(self, max_range=MAX_RANGE):
        self.max_range = max_range
        self.value = random.randint(0, max_range)
        text = f"Guess a number between 0 and {self.max_range}"
        color = "black"
        url = STARTING_IMAGE_URL

        return (f"<h1 style=\"color: {color}\">{text}</h1>"
                f"<img src={url}/>")

    def verify(self, number):
        if number < self.value:
            text = "Too low, try again!"
            color = "red"
            url = LOW_IMAGE_URL
        elif number > self.value:
            text = "Too high, try again!"
            color = "purple"
            url = HIGH_IMAGE_URL
        else:
            text = "You found me!"
            color = "green"
            url = OK_IMAGE_URL

        return f"<h1 style=\"color: {color}\">{text}</h1><img src={url}/>"
