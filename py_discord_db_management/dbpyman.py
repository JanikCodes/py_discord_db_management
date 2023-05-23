import discord

from py_discord_db_management.classes.views.table_overview import TableOverviewView


def create_db_management(database):
    embed = create_db_management_embed(database)
    view = TableOverviewView(database)

    return embed, view

def create_db_management_embed(database):
    embed = discord.Embed(title=f"Database Management",
                          description=f"Connection Status: **{database.get_is_connected()}** \n",
                          colour=discord.Color.red())
    embed.set_footer(text=f"Below are your tables")

    return embed
