import typing
from quart import Quart, render_template, url_for, send_from_directory, redirect
from quart_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
from dotenv import load_dotenv
import os

load_dotenv()

app = Quart(__name__)
app.config["DISCORD_CLIENT_ID"] = 784545186612510811
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]
app.config["DISCORD_REDIRECT_URI"] = os.environ["DISCORD_REDIRECT_URI"]
app.config["DISCORD_BOT_TOKEN"] = os.environ["DISCORD_BOT_TOKEN"]

@app.route("/")
async def index():
    return await render_template("index.html")

@app.route("/favicon.ico")
async def favicon():
    return await send_from_directory(current_app.root_path, "/static/favicon.ico", mimetype="image/x-icon")

@app.route("/oembed.json")
async def oembed():
    return await send_from_directory(current_app.root_path, "/static/oembed.json", mimetype="application/json")


if __name__ == "__main__":    
    app.run(host="0.0.0.0",port=25006, debug=True)