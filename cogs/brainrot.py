# -- BRAINROT-RELATED COMMANDS --
import ollama
import random
from discord.ext import commands

class Brainrot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def generate_brainrot_response(self, message):
        try:
            # Clean the message content
            user_input = message.content.replace(f'<@{self.bot.user.id}>', '').strip()
            print(user_input)
                
            # Create the prompt
            prompt = f"""
            user message: {user_input}
                
            RESPONSE RULES:
            - ALWAYS maintain 100% connection to user message
            - Use cusses liberally — “fuck”, “shit”, “bitch”, etc.
            - Use unhinged gamer language
            - Include {random.randint(3, 8)} random emojis
            - 30% chance to respond with ONLY 💀
            - Keep the character limit of your response below 2,000 characters AS TO NOT BREAK DISCORD MESSAGES; keep long messages less frequent than short ones
            - Finally, create your response
            """
                
            # Get the raw response first
            raw_response = ollama.chat(
                model='dolphin-phi',
                messages=[{'role': 'system', 'content': prompt}],
                options={'temperature': 1.7}
            )
                
            # Extract the message content properly
            response_content = raw_response['message']['content']
            await message.reply(response_content)
                
            # Random reaction
            if random.random() < 0.3:
                await message.add_reaction(random.choice(['💀', '🤡', '♿', '🖕🏿']))
                    
        except Exception as e:
            print(f"Brainrot Error: {e}")
            await message.reply("💀")

    @commands.Cog.listener()
    async def on_message(self, message):
        # If the message is by the bot itself or
        if message.author.bot or not message.content:
            return
        
        # Check if message is actually a command
        ctx = await self.bot.get_context(message)
        if ctx.valid:
            return await self.bot.invoke(ctx)
            
        if self.bot.user in message.mentions:
            await self.generate_brainrot_response(message)


def setup(bot):  # Setup cog
    bot.add_cog(Brainrot(bot))  # Add cog to bot