import discord

class TableCategoryView(discord.ui.View):
    def __init__(self, database, table):
        super().__init__()

        from py_discord_db_management.classes.buttons.add_data_button import AddDataButton
        from py_discord_db_management.classes.buttons.return_to_overview_button import ReturnOverviewButton

        self.add_item(ReturnOverviewButton(database))
        self.add_item(AddDataButton(table))


