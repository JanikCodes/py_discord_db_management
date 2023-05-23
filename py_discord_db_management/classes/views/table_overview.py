import discord

class TableOverviewView(discord.ui.View):
    def __init__(self, database):
        super().__init__()

        from py_discord_db_management.classes.buttons.table_overview_button import TableOverviewButton

        for table in database.tables:
           self.add_item(TableOverviewButton(database=database, table=table))