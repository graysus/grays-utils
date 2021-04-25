# grays-utils
**Discord.py library for these things (as of now)**
- Pagination

**To use the paginator:**

Sample code: ```py
embed = discord.Embed(title="Python code stuff",description="{con}")
  .set_footer("Sample {pagen} of {pages}")

code_samples = [
"""
@client.command()
async def HelloWorld(ctx):
  await ctx.send("I'm not World, I'm Dad!")
""",
"""
@client.command()
async def ping(ctx):
  await ctx.send(f"Ping: {round(client.latency,2)}ms")
"""
]

#check this code out for usage
pagi = graysutils.Paginator(embed,*code_samples)
await pagi(ctx,client,ctx.author.id)
```
