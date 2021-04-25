# grays-utils
**Discord.py library for these things (as of now)**
- Pagination

**To use the paginator:**

Sample code:

````python
embed = discord.Embed(title="Python code stuff",description="```py\n{con}\n```").set_footer(text="Sample {pagen} of {pages}")
"""

"""
code_samples = [
"""@client.command()\nasync def HelloWorld(ctx):\n\tawait ctx.send('I\\'m not World, I\\'m Dad!\\')""",
"""@client.command()\nasync def ping(ctx):\n\tawait ctx.send(f'Ping: {round(client.latency,2)}ms')"""
] 

#check this code out for usage 
pagi = graysutils.Paginator(embed,*code_samples) 
await pagi(ctx,c,ctx.author.id)
````
