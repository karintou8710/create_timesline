import discord

from dotenv import load_dotenv
import os

print(f"discord version -- {discord.__version__} --")

# envファイル読み込み
load_dotenv()

TOKEN =  os.environ['TOKEN'] #TOKEN

TIMES_ID =  int(os.environ['TIMES_ID']) # HUIT timesline category

# インテントの設定
intents = discord.Intents.default()
intents.members = True

# クライアントオブジェクト作成
client = discord.Client(intents=intents)

# 特定のカテゴリデータを取得
def getCategory(categoryList, ID):
    for guild in categoryList:
        if (guild.id == ID): return guild
            

# 起動時に動作する処理
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('------')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    if message.author.bot:
        return

# 新規参加時に起動するイベント
@client.event
async def on_member_join(member):

    #botは処理しない
    if member.bot:
        return

    name = "times_" + member.display_name
    guild = member.guild
    times = getCategory(guild.categories, TIMES_ID)
    await times.create_text_channel(name)
    

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)