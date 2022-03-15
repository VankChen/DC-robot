@bot.event
async def on_member_join(member):
    print(f"{member}歡迎加入邊緣垃圾群")

@bot.event
async def on_member_remove(member):
    print(f"{member}沒差啊我才不稀罕要滾就滾")