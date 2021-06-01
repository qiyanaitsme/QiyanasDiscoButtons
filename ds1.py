print("Бот готов к работе, Шерби.") #не удаляй
print("Автор Шерби.") #не удаляй
print("ВК - vk.com/sherbyaakodanel.") #не удаляй

from pypresence import Presence #установи библиотеку pypresence - pip install pypresence
from time import time 

#Чтобы сделать название приложения, нужно зайди в https://discord.com/developers/applications, создать приложение, назвать его и добавить картинки.
RPC = Presence("818012004185800705") #clinetid discord
btns = [
    {
        "label": "GITHUB",
        "url": "https://github.com/sherbyaakodanel" #ссылка
    },
    {
        "label": "VK",
        "url": "https://vk.com/sherbyaakodanel"
    }
]

RPC.connect()
RPC.update(
	state="Хочу завоевать мир!",
	details="Шерби сделает это!",
	start=time(),
	buttons=btns,
	large_image="bigim",
	small_image="smallim",
	large_text="Мур мур",
	small_text="Люблю тебя!"
)

input()
