import discord

from py_discord_db_management.classes.views.table_categories import TableCategoryView


class TableOverviewButton(discord.ui.Button):
    def __init__(self, database, table):
        super().__init__(label=table.table_name)
        self.database = database
        self.table = table

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        # Call view with further table operations as buttons
        await interaction.message.edit(view=TableCategoryView(database=self.database, table=self.table))