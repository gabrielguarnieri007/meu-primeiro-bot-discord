import discord
import os

# Configurando as "intents" (permissões) que ligamos no portal
intents = discord.Intents.default()
intents.message_content = True  # Permissão para ler mensagens
intents.members = True          # Permissão para ver membros

# 'client' é a nossa conexão com o Discord
client = discord.Client(intents=intents)

# Este é um "evento": ele roda UMA vez quando o bot se conecta com sucesso
@client.event
async def on_ready():
    print(f'Logado com sucesso como {client.user}!')
    print('------')

# Este é outro "evento": ele roda CADA VEZ que uma nova mensagem é enviada
@client.event
async def on_message(message):
    # 1. Impede que o bot responda a si mesmo (evita loop infinito)
    if message.author == client.user:
        return

    # 2. A mágica: Se a mensagem começar com '!ping'
    if message.content.startswith('!ping'):
        # 3. O bot vai responder 'pong' no mesmo canal
        await message.channel.send('pong')

# --- A LINHA MAIS IMPORTANTE ---
# Cole seu Token secreto aqui dentro das aspas
client.run('SEU_TOKEN_AQUI')