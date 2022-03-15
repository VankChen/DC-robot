@bot.event
async def on_member_join(member):
    channel=bot.get_channel(953135766974894120)
    await channel.send(f"{member}歡迎加入邊緣垃圾群")

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(953135766974894120)
    await channel.send(f"{member}沒差啊我才不稀罕要滾就滾")