import discord

def create_db_management_embed(database):
    embed = discord.Embed(title=f"I couldn't find the correct Item..",
                          description=f"You can find your Item Id inside your inventory. Access it with `/inventory`",
                          colour=discord.Color.red())
    return embed