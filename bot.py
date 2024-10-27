from quart import Quart, request, render_template
import discord

app = Quart(__name__)

# Discord bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Discord bot client
client = discord.Client()

# Function to send a message through Discord bot
async def send_message_to_discord(message):
    channel = client.get_channel(YOUR_CHANNEL_ID_HERE)  # Replace YOUR_CHANNEL_ID_HERE with your channel ID
    await channel.send(message)

# Route to render the HTML form
@app.route('/')
async def index():
    return await render_template('index.html')

# Route to handle form submission and send message to Discord
@app.route('/send-message', methods=['POST'])
async def send_message():
    message = request.form['message']
    await send_message_to_discord(message)
    return 'Message sent to Discord!'

# Discord bot event: on ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Run the Flask app and Discord bot
if __name__ == '__main__':
    client.run(BOT_TOKEN)
    app.run()
