import discord

class TableCategoryView(discord.ui.View):
    def __init__(self, database, table):
        super().__init__()

        self.add_item(self.ReturnOverviewButton(database))
        self.add_item(self.AddDataButton(database, table))
        self.add_item(self.DeleteDataButton(database, table))

    class ReturnOverviewButton(discord.ui.Button):
        def __init__(self, database):
            super().__init__(label="Return")
            self.database = database

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.defer()

            from py_discord_db_management.views.table_overview_view import TableOverviewView
            await interaction.message.edit(view=TableOverviewView(database=self.database))
    class AddDataButton(discord.ui.Button):
        def __init__(self, database, table):
            super().__init__(label="Add Data", style=discord.ButtonStyle.green)
            self.database = database
            self.table = table

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.defer()

            # we create an empty array with the size of the table columns count
            columns = self.table.get_visible_columns()

            from py_discord_db_management.views.table_add_data_view import TableAddDataView
            await interaction.message.edit(view=TableAddDataView(database=self.database, table=self.table, columns=columns))

    class DeleteDataButton(discord.ui.Button):
        def __init__(self, database, table):
            super().__init__(label="Delete Data", style=discord.ButtonStyle.danger)
            self.database = database
            self.table = table

        async def callback(self, interaction: discord.Interaction):

            # we create an empty array with the size of the table columns count
            columns = self.table.get_columns()

            await interaction.response.send_modal(self.DeleteDataModal(database=self.database, table=self.table))

        class DeleteDataModal(discord.ui.Modal):
            def __init__(self, database, table):
                super().__init__(title=f"Adding to {table.get_table_name()}")
                self.database = database
                self.table = table

                self.add_item(discord.ui.TextInput(label=f"Primary Key", required=True))

            async def on_submit(self, interaction: discord.Interaction):
                await interaction.response.defer()

                # retrieve the data from the input
                primary_key = self.children[0].value

                self.database.remove_data_from_table(table=self.table, primary_key=primary_key)
