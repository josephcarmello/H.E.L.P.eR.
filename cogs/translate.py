import disnake
from disnake.ext import commands
from disnake import Interaction
from googletrans import Translator, LANGUAGES
import cutlet

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()  # Initialize the Google Translator
        self.katsu = cutlet.Cutlet()  # Use the default romaji style (kunrei)

    @commands.slash_command(name="translate", description="Translate text to a selected language")
    async def translate(self, inter: disnake.ApplicationCommandInteraction, text: str, language: str, romaji: bool = False):
        """
        Translates text to a selected language (either 'es' for Spanish or 'ja' for Japanese).
        Arguments:
        text: The text to be translated.
        language: The language code to translate to ('es' for Spanish, 'ja' for Japanese).
        romaji: Whether to include romaji for Japanese translations.
        """
        if language not in ['es', 'ja']:
            await inter.response.send_message("Please choose 'es' for Spanish or 'ja' for Japanese.", ephemeral=True)
            return

        try:
            translated = self.translator.translate(text, dest=language)

            if language == 'ja':
                translated_text = translated.text
                romaji_text = None
                if romaji:
                    romaji_text = self.katsu.romaji(translated_text)  # Convert Japanese to romaji

                if romaji_text:
                    await inter.response.send_message(f"Translated text (Japanese):\n{translated_text}\nRomaji: {romaji_text}")
                else:
                    await inter.response.send_message(f"Translated text (Japanese):\n{translated_text}")
            else:
                await inter.response.send_message(f"Translated text ({LANGUAGES[language]}):\n{translated.text}")
        except Exception as e:
            await inter.response.send_message(f"Error occurred while translating: {str(e)}", ephemeral=True)

def setup(bot):
    bot.add_cog(Translate(bot))
