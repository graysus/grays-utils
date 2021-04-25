import json
import asyncio
import discord

class PaginatorValueError(Exception):
	pass

class Paginator:
	def __init__(self,emb,*con):
		self.embjson = json.dumps(emb.to_dict())
		self.con = [repr(i)[1:-1] for i in con]
	def gen(self,i):
		h = {}
		h.update(
			json.loads(
				self.embjson
					.replace("{con}",self.con[i] if self.con[i].__len__() <= 2048 else self.con[i][:2045]+"...")
					.replace("{pagei}",str(i))
					.replace("{pagen}",str(i+1))
					.replace("{pages}",str(len(self.con)))
			)
		)

		return discord.Embed.from_dict(h)
	async def __call__(self,ch,c,*allowed_people,reac={"⏮":0,"⬅️":1,"➡️":2,"⏭":3,"❌":4},timeout=30,**kwargs):
		m = await ch.send(**kwargs,embed=self.gen(0))
		for i in reac:
			await m.add_reaction(i)
		await asyncio.sleep(0.5)
		pag = 0
		if True in [i not in range(0,5) for i in reac.values()]:
			raise PaginatorValueError("Reaction values must be between 0-4")
		while True:
			h,u = await c.wait_for("reaction_add",check=lambda h,u : h.message == m and u.id in allowed_people and h.emoji in reac)
			f = reac[h.emoji]
			if f == 0:
				pag = 0
			elif f == 1:
				pag -= 1
			elif f == 2:
				pag += 1
			elif f == 3:
				pag = len(self.con)-1
			elif f == 4:
				return m
			else:
				#Shouldn't happen but oh well, just in case 🤷‍♀️
				raise PaginatorValueError("Reaction value must be between 0-4")
			if pag >= len(self.con):
				pag = len(self.con)-1
			if pag < 0:
				pag = 0

			await m.remove_reaction(h.emoji,u)
			await m.edit(**kwargs,embed=self.gen(pag))

#await Paginator(discord.Embed(title="Page {pagen}/{pages}",description="{con}"),"Test 1\nMultiline Test","Test 2")(ctx)
