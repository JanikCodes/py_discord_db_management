import itertools
import discord

class TableAddDataView(discord.ui.View):
    def __init__(self, database, table, columns, column_index=0):
        super().__init__()
        self.database = database
        self.table = table
        self.columns = columns
        self.column_index = column_index

        self.add_item(self.ReturnButton(database, table))

        # Check if we can even add more data
        if not self.column_index >= len(table.get_columns()):

            if column_index == 0:
                self.add_item(self.ContinueButton("Start", database, table, columns, column_index))
            else:
                self.add_item(self.ContinueButton("Continue", database, table, columns, column_index))
        else:
            # Finished filling all columns
            self.database.add_data_to_table(table=self.table, columns=self.columns)

    class ReturnButton(discord.ui.Button):
        def __init__(self, database, table):
            super().__init__(label="Return")
            self.database = database
            self.table = table

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.defer()

            from py_discord_db_management.views.table_categories_view import TableCategoryView
            await interaction.message.edit(view=TableCategoryView(database=self.database, table=self.table))

    class ContinueButton(discord.ui.Button):
        def __init__(self, label, database, table, columns, column_index):
            super().__init__(label=label, style=discord.ButtonStyle.green)
            self.database = database
            self.table = table
            self.columns = columns
            self.column_index = column_index

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.send_modal(self.AddDataModal(database=self.database, table=self.table, columns=self.columns, column_index=self.column_index))

        class AddDataModal(discord.ui.Modal):
            def __init__(self, database, table, columns, column_index):
                super().__init__(title=f"Adding to {table.get_table_name()}")
                self.database = database
                self.table = table
                self.columns = columns
                self.column_index = column_index
                # create a start column index to later address the index when assigning the value to the tb_data
                self.start_column_index = column_index

                # style=discord.TextStyle.paragraph
                column_counter = self.column_index

                # create individual input based on column
                for index, column in itertools.islice(enumerate(self.columns[self.column_index:], start=self.column_index), 5):
                    # increase counter
                    column_counter += 1
                    self.add_item(discord.ui.TextInput(label=f"{column.get_field()}", required=not column.get_nullable(), placeholder=str(column.get_default()) ))

                self.column_index = column_counter

            async def on_submit(self, interaction: discord.Interaction):
                await interaction.response.defer()

                # retrieve the data from each input
                for index, value in enumerate(self.children):
                    column_val = None if not str(value) else str(value)

                    self.columns[self.start_column_index + index].set_attached_data(column_val)

                await interaction.message.edit(view=TableAddDataView(database=self.database, table=self.table, columns=self.columns, column_index=self.column_index))
