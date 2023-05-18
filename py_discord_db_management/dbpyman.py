import discord


def create_db_management(database):
    embed = create_db_management_embed(database)
    view = create_db_management_view(database)

    return embed, view

def create_db_management_embed(database):
    embed = discord.Embed(title=f"Database Management",
                          description=f"Connection Status: **{database.get_is_connected()}** \n",
                          colour=discord.Color.red())
    embed.set_footer(text=f"Below are your tables")

    return embed

class create_db_management_view(discord.ui.View):
    def __init__(self, database):
        super().__init__()

        for table in database.tables:
           self.add_item(TableButton(table=table))

class TableButton(discord.ui.Button):
    def __init__(self, table):
        super().__init__(label=table.table_name)
        self.table = table
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        columns_text = str()

        for column in self.table.columns:
            columns_text += f"{column.field} ({column.type}) Nullable: {column.null} Key: {column.key} Default: {column.default} Extra: {column.extra}\n"

        await interaction.followup.send(columns_text)