import discord
from discord.ext import commands
import random

bot = commands.Bot(';')

with open('kinks.txt') as fp:
    kink_list = fp.read().split('\n')

@bot.command()
async def love(ctx, target: discord.Member, target2: discord.Member = None):
    if target2 is None:
        val = abs(ctx.author.id - target.id)
        if val == 0:
            await ctx.send(f'❤️ You love yourself 100% ❤️')
        else:
            await ctx.send(f'❤️ **{ctx.author.name}** has {val % 100}% love with **{target.name}** ❤️')
    else:
        val = abs(target.id - target2.id)
        if val == 0:
            await ctx.send(f'❤️ You love yourself 100% ❤️')
        else:
            await ctx.send(f'❤️ **{target.name}** has {val % 100}% love with **{target2.name}** ❤️')

@bot.command()
async def ppsize(ctx, target: discord.Member = None):
    if target is None:
        target = ctx.author
    val = target.id % 12
    pp = '8' + '=' * val + 'D'
    abrev = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'an', 'a', 'a', 'an', 'a']
    await ctx.send(f'**{target.name}** has {abrev[val]} **{val}** incher: **{pp}**')

@bot.command()
async def ship(ctx: commands.Context, target: discord.Member = None):
    if target is None:
        target = ctx.author
    
    members = ctx.guild.members
    members = [m for m in members if m.top_role.permissions.kick_members and not m.bot]
    random.seed(target.id)
    member = random.choice(members)
    
    await ctx.send(f'? **{target.name}** has been shipped with... **{member.name}** ?')

@bot.command()
async def kinks(ctx: commands.Context, target: discord.Member = None):
    if target is None:
        target = ctx.author
    random.seed(target.id)
    kink = random.choices(kink_list, k=7)
    msg = '\n'.join(f'{i}) {k}' for i,k in enumerate(kink, start=1))
    await ctx.send(f'**{target.name}** has the following kinks...\n{msg}')

@bot.command()
async def subdom(ctx: commands.Context, target: discord.Member = None):
    if target is None:
        target = ctx.author
    
    random.seed(target.id)
    val = random.randint(0, 1)
    val = '**submissive** ?' if not val else '**dominant** ?'
    await ctx.send(f'**{target.name}** is definitely {val}')

@bot.command()
async def party(ctx: commands.Context, target: discord.Member = None):
    if target is None:
        target = ctx.author

    random.seed(target.id)
    val = random.randint(0, 1)
    if target.id == 249640962144337920:
        val = 0
    val = '**republican** ?' if not val else '**liberal** ?'
    await ctx.send(f'**{target.name}** is definitely a {val}')

@bot.command()
async def horoscope(ctx: commands.Context, target: discord.Member = None):
    if target is None:
        target = ctx.author
    
    horoscopes = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    random.seed(target.id)
    h = random.choice(horoscopes)
    emoji = h.lower()
    await ctx.send(f':{emoji}: **{target.name}** is a **{h}** :{emoji}:')

bot.run('')