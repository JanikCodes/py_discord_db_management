import discord

class TableOverviewView(discord.ui.View):
    def __init__(self, database):
        super().__init__()

        for table in database.tables:
            # hide hidden tables from view
            if not table.get_hidden():
                self.add_item(self.TableOverviewButton(database=database, table=table))

    class TableOverviewButton(discord.ui.Button):
        def __init__(self, database, table):
            super().__init__(label=table.get_table_name())
            self.database = database
            self.table = table

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.defer()

            # Call view with further table operations as buttons
            from py_discord_db_management.views.table_categories_view import TableCategoryView
            await interaction.message.edit(view=TableCategoryView(database=self.database, table=self.table))