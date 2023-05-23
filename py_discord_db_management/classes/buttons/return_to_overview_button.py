import discord

from py_discord_db_management.classes.views.table_overview import TableOverviewView


class ReturnOverviewButton(discord.ui.Button):
    def __init__(self, database):
        super().__init__(label="Return", style=discord.ButtonStyle.danger)
        self.database = database

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        await interaction.message.edit(view=TableOverviewView(database=self.database))