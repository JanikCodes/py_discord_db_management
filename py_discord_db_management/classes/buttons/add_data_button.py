import discord


class AddDataButton(discord.ui.Button):
    def __init__(self, table):
        super().__init__(label="Add Data", style=discord.ButtonStyle.green)
        self.table = table

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        pass