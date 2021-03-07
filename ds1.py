from pypresence import Presence
from time import time

RPC = Presence("818012004185800705")
btns = [
	{
		"label": "VK",
		"url": "https://vk.com/sherbyaakodanel"
	},
	{
		"label": "GITHUB",
		"url": "https://github.com/sherbyaakodanel"
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