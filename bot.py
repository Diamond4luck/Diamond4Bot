import discord
import asyncio
import requests
import os
from discord.ext.commands import Bot
from discord.ext import commands
import random


Client = discord.Client()
bot_prefix='!!'
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot Online")
    print("Name: (Diamond4Bot)".format(client.user.name))
    print("ID: ()".format(client.user,id))
    await client.change_presence(game=discord.Game(name='type !!help')  ) 
    
@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(ctx.message.channel, content='This command is on a %.2fs cooldown! Please try again later...' % error.retry_after)
    raise error
               
@client.command(pass_context=True)
async def power(ctx):
    power = open('power.txt').read().splitlines()
    power2 = random.choice(power)
    if ctx.message.author.id == "206027308149112832":
        await client.say("<@!206027308149112832> You can fly!!!")
    else:
        await client.say('%s Your hidden power is: %s' % (ctx.message.author.mention, power2))       
    
@client.command(pass_context=True)
@commands.cooldown(1, 9, commands.BucketType.user)
async def cooldown(ctx):
    cooldown = await client.say("Ok. See if this has cooldown now.")

@client.command(pass_context=True)
async def logs(ctx):
    embed = discord.Embed(title="All the changelogs here!", color=0xE90FF)
    embed.add_field(name="Updated Command!", value="The !!help command is now revamped thanks to vσятєχтнєgнσυℓ#6346! Check his bot and stuff out! Updated in 17/12/2018.")
    embed.add_field(name="New Command!", value="Do !!rps and play Rock Paper Scissors with the bot! Added in 17/9/2018.")
    embed.add_field(name="New Command!", value="Do !!casino and try your luck! Added in 17/9/2018.")
    embed.add_field(name="Minor Update!", value="Some commands have cooldowns to prevent spam! Added in 8/31/2019.")
    embed.add_field(name="New Command!", value="Do !!diary to see other people's hidden messages in their diaries! Added in 18/8/2018.")
    embed.add_field(name="Updated Command!", value="Updated the !!love command. Now you can see how long people had loved together.")
    embed.add_field(name="Updated Command!", value="Updated the !!kill command. **You** can kill other people now!.")
    embed.add_field(name="Updated Command!", value="Updated the !!waud command. It should be more understandable now.")
    embed.add_field(name="New Command!", value="Do !!power to see your secret power! Added in 25/6/2018.")
    embed.add_field(name="New Command!", value="Do !!waud to see what other memebrs are doing. Added in 26/2/2018.")
    embed.add_field(name="Minor Update!", value="Every embed should have colours now! Updated in 13/1/2018.")
    await client.say(embed=embed)   
    
@client.command(pass_context=True)
async def casino(ctx):
    casinostart = await client.say("Bigger or smaller than 50? Say it, and you'll be awarded with a reward!")

    def check(m):
        return 'Bigger', 'Smaller'
    
    message = await client.wait_for_message()
    if 'Bigger' in message.content:
        await client.say("Bigger? OK! Rolling!")
    elif 'Smaller' in message.content:
        await client.say("Smaller? OK! Rolling!")
        
    casinonumber = random.randint(0,100)
    sentcasinon = await client.say("{0}".format(casinonumber))
    casinonumber2 = random.randint(0,100)
    sentcasinon2 = await client.edit_message(sentcasinon,"{0}".format(casinonumber2))
    casinonumber3 = random.randint(0,100)
    sentcasinon3 = await client.edit_message(sentcasinon2,"{0}".format(casinonumber3))
    casinonumber4 = random.randint(0,100)
    sentcasinon4 = await client.edit_message(sentcasinon3,"{0}".format(casinonumber4))
    casinonumber5 = random.randint(0,100)
    casinorewardslist = open('Rewards.txt').read().splitlines()
    casinorewards = random.choice(casinorewardslist)
    if casinonumber5 >= 50:
        await client.edit_message(sentcasinon4,"The number is {0}, which is bigger than 50!".format(casinonumber5))
    else:
        await client.edit_message(sentcasinon4,"The number is {0}, which is smaller than 50!".format(casinonumber5))
    if casinonumber5 >= 50:
        if 'Bigger' in message.content:
            await client.say("It was bigger than 50. You won! Your reward is {}! ".format(casinorewards))
        else:
            await client.say("It was bigger than 50. You lost.")
    elif casinonumber5 <= 50:
        if 'Smaller' in message.content:
            await client.say("It was smaller than 50. You won! Your reward is {}!".format(casinorewards))
        else:
            await client.say("It was smaller than 50. You lost.")
        
@client.command(pass_context=True)
async def casino2(ctx):
    casinostart = await client.say("Bigger or smaller than 50? Say it!")

    def check(m):
        if m.author == ctx.message.author:
            return True
        if m.content in ['Bigger', 'Smaller']:
            return True
        return False

    try:
        message = await client.wait_for_message(check=check, timeout=60)
    except asyncio.TimeoutError:
        await client.say("Guess you don't want to play.")
    else:
        if message.content.capitalize() == 'Bigger':
            await client.edit_message(casinostart, "Bigger? OK! Rolling!")
        else:
            await client.edit_message(casinostart, "Smaller? OK! Rolling!")

    for x in range(5):
        random_ = random.randint(0, 100)
        await client.edit_message(casinostart, random_)
        await asyncio.sleep(5)

    if int(casinostart.content) >= 50:
        if 'Bigger' in message.content:
            await client.edit_message(casinostart, "It was bigger than 50, you won!")
        else:
            await client.edit_message(casinostart, "It was bigger than 50, you lost!")
    else:
        if 'Smaller' in message.content:
            await client.edit_message(casinostart, "It was bigger than 50, you won!")
        else:
            await client.edit_message(casinostart, "It was bigger than 50, you lost!")     
            
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Everything you need here!")
    embed.add_field(name="!!power", value="Do !!power to see what hidden powers you have!")
    embed.add_field(name="!!logs", value="Do !!logs to see what recent changes I did to the bot!")
    embed.add_field(name="!!help", value="Do !!help to get help about the bot!")
    embed.add_field(name="!!casino", value="Do !!casino and see if you can win or not!")
    embed.add_field(name="!!rps", value="Do !!rps and play Rock, Paper, Scissors! with the bot itself!")
    embed.add_field(name="!!yon", value="Do !!yon and see if you want what the bot says!")
    embed.add_field(name="!!yon add", value="Do !!yon add and add your own lines of  Yes or No!")
    embed.add_field(name="!!wyr", value="Do !!wyr and play Would you Rather with the bot!")
    embed.add_field(name="!!wyr add", value="Do !!wyr add and add your own lines of Would You Rather!")
    embed.add_field(name="!!kill", value="Do !!kill and see how you kill someone!")
    embed.add_field(name="!!diary", value="Do !!diary and see other people's diaries!")
    embed.set_footer(text="Page 1 of 2")

    help1 = await client.say(embed=embed)
    await client.say("Type help2 to see the pages.")

    helpembed2 = discord.Embed(title="Second page!")
    helpembed2.add_field(name="!!game", value="Do !!game and the bot guesses your favourite game", inline=False)
    helpembed2.add_field(name="!!moti", value="Do !!diary and see a motivational message!", inline=False)
    helpembed2.add_field(name="!!love", value="Do !!love and see who loves who for how long!", inline=False)
    helpembed2.add_field(name="!!reco", value="Do !!reco and see what the bot recommends a command for you!", inline=False)
    helpembed2.add_field(name="!!ping", value="Do !!diary to ping the bot!", inline=False)
    helpembed2.add_field(name="!!flip", value="Do !!flip and the bot flips a coin for you!", inline=False)
    helpembed2.add_field(name="!!amIgay", value="Do !!amIgay and the bot guesses if you are gay or not.", inline=False)
    helpembed2.add_field(name="!!howIkms", value="Do !!howIkms and see how would you kill yourself! (joke)", inline=False)
    helpembed2.add_field(name="!!chance", value="Do !!chance and see if you're lucky or not! (similar to 8ball)", inline=False)
    helpembed2.add_field(name="!!future", value="Do !!future and see your possible future!", inline=False)
    helpembed2.add_field(name="!!number", value="Do !!number and see your lucky number!", inline=False)
    helpembed2.add_field(name="!!badnumber", value="Do !!badnumber and see your unlucky number!", inline=False)
    helpembed2.set_footer(text="Page 2 of 2")
    #inline is where it doesn't set the first letter in the first word captialised (I think)
    
    def check(m):
        return m.author == ctx.message.author and m.content == 'help2' #from the author who typed the command and detects the next message if there is help2
    
    
    try:
        msg = (await client.wait_for_message(check=check, timeout=120)).content #waits for u to type something.
    except asyncio.TimeoutError:
        return await client.delete_message(help1)

    if msg == 'help2': #if the message is help2 (by you)
        await client.edit_message(help1, embed=helpembed2)      #edits the message of the first embed            

@client.command(pass_context=True)
async def rps(ctx):
    await client.say("Say Rock, Paper or Scissors!")
    
    def check(m):
        return 'Rock','Paper','Scissor'
    
    message = await client.wait_for_message()
    if 'Rock' in message.content:
        await client.say("You chose rock!")
    elif 'Paper' in message.content:
        await client.say("You chose paper!")
    elif 'Scissors' in message.content:
        await client.say("You chose scissors!")
    return await client.say("Umm, did you do something wrong?")
          
     
    rpsrewardslist = open('Rewards.txt').read().splitlines()
    rpsrewards = random.choice(rpsrewardslist)
    rps1 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision = await client.say(rps1)
    rps2 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision2 = await client.edit_message(rpsdecision,"{}".format(rps2))
    rps3 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision3 = await client.edit_message(rpsdecision2,"{}".format(rps3))
    rps4 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision4 = await client.edit_message(rpsdecision3,"{}".format(rps4))
    rps5 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision5 = await client.edit_message(rpsdecision4,"{}".format(rps5))

    if 'Rock' in rps5:
        if 'Rock' in message.content:
            await client.say("Rock versus Rock, it's a **tie!** You win nothing!")
        elif 'Paper' in message.content:
            await client.say("Paper versus Rock, Rock **wins!** You won! Your prize is {}.".format(rpsrewards))
        elif 'Scissors' in message.content:
            await client.say("Scissors versus Rock, Rock **wins!** You lost!")
    elif 'Paper' in rps5:
        if 'Rock' in message.content:
            await client.say("Rock versus Paper, Paper **wins!** You lost!")
        elif 'Paper' in message.content:
            await client.say("Paper versus Paper, it's a **tie!** You win nothing!")
        elif 'Scissors' in message.content:
            await client.say("Scissors versus Paper, Scissors **wins!** You won! Your prize is {}.".format(rpsrewards))
    elif 'Scissors' in rps5:
        if 'Rock' in message.content:
            await client.say("Rock versus Scissors, Rock **wins!** You won! Your prize is {}.".format(rpsrewards))
        elif 'Paper' in message.content:
            await client.say("Paper versus Scissors, Paper **wins!** You lost!")
        elif 'Scissors' in message.content:
            await client.say("Scissors versus Scissors, it's a **tie!** You win nothing!") 

@client.command(pass_context=True)
async def badminton(ctx):
    badmintonplayers = random.choice([x for x in ctx.message.server.members if not x.bot])
    await client.say("You are now competing with {}.".format(badmintonplayers))
    await client.say("It's your turn to serve. Serve high or low?")
    
    def check(m):
      return 'High','Low'
    
    message = await client.wait_for_message()
    if 'High' in message.content:
        await client.say("You served a high ball!")
    elif 'Low' in message.content:
        await client.say("You served a low ball!")
    else:
        await client.say("You randomly served the ball, and the referee gives you a foul! Match ended!")
        
    playerserve = random.choice(["The player sucessfully hit the ball!","The player missed the ball!"])
    playerstatus = await client.say(playerserve)
    playerhit = random.choice(["The player hits a high ball!","The player hits a low ball!"])
    
    if 'The player sucessfully hit the ball!' in playerserve:                                 
        await client.say("{} Where should you be? Behind or Front?".format(playerhit))
    elif 'The player missed the ball!' in playerserve:
        await client.say("Congratulations! You won!")
        
   def check(m):
      return 'Behind','Front'
    
    message = await client.wait_for_message()
    if 'Behind' in message.content:
        await client.say("You went backwards!")
    elif 'Front' in message.content:
        await client.say("You went forward!")
    else:
        await client.say("You rushed off and people thought you raged quit! Match ended!")
        
    shuttercock = random.choice(["The ball lands an in! You lost!","However, the ball lands an out! You won!"])
    
    if 'The player hits a low ball!' in playerhit:
        if 'Front' in message.content:
            await client.say("You feel like you can hit the ball! High or low?")
        elif 'Behind' in message.content:
            await client.say("Oh no! You are unable to hit the ball!")
            await client.say("It's an in! You lost!")
     elif 'The player hits a high ball!' in playerhit:
        if 'Behind' in message.content:
            await client.say("You feel like you can hit the ball! High or low?")
        elif 'Front' in message.content:
            await client.say("Oh no! You are unable to hit the ball!")
            await client.say(shuttercock)
               
            
            
                      
@client.group(pass_context=True, invoke_without_command=True)
async def yon(ctx):
    yesornolist = open('yesorno.txt').read().splitlines()
    yesornolist2 = random.choice(yesornolist)
    yon = await client.say(" {} Choose Y or N .".format(yesornolist2))
    await client.add_reaction(yon,'\U0001f1fe')
    await client.add_reaction(yon,'\U0001f1f3')
    
@yon.command(pass_context=True)
async def add(ctx,*, string):
    yonopen = open("yesorno.txt", "a")
    yonopen.write("\n{}".format(string))
    yonopen.close()
    await client.say("Added!")

@client.group(pass_context=True, invoke_without_command=True)
async def wyr(ctx):
    wyrlist = open('wyr.txt').read().splitlines()
    wyrlist2 = random.choice(wyrlist)
    wyr = await client.say("Would you rather {}? Choose A or B.".format(wyrlist2))
    await client.add_reaction(wyr,'\U0001f170')
    await client.add_reaction(wyr,'\U0001f171')
    
@wyr.command(pass_context=True)
async def add(ctx,*, string):
    wyropen = open("wyr.txt", "a")
    wyropen.write("\n{}".format(string))
    wyropen.close()
    await client.say("Added!")

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def kill(ctx):
    kill = open('Deaths.txt').read().splitlines()
    death = random.choice(kill)
    victim = random.choice([x for x in ctx.message.server.members if not x.bot])
    if ctx.message.author.id == "206027308149112832":
        embed = discord.Embed(title='A crime has been commited!', description = '<@!206027308149112832> killed {} {}!'.format(victim.display_name, death))
    else:
        embed = discord.Embed(title='A crime has been commited!', description = '{} killed {} {}!'.format(ctx.message.author.mention, victim.display_name, death))
    await client.say(embed=embed)
    
@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def diary(ctx):
    ContentsDiary = open('Diary.txt').read().splitlines()
    ContentsDiary2 = random.choice(ContentsDiary)
    AuthorOfDiary = random.choice([x for x in ctx.message.server.members if not x.bot])
    Day = random.randint(1,31)
    Month = random.choice(["January", "February", "March","April","May","June","July","August","September","October","November","December"])
    embed = discord.Embed(title='You found {}"s diary!'.format(AuthorOfDiary), description = '"Dear Diary, I,{}, {}"'.format(AuthorOfDiary, ContentsDiary2))
    embed.add_field(name="Written in",value="{}/{}/2018.".format(Day, Month))
    embed.set_image(url="https://cdn.discordapp.com/attachments/347731992227610625/480550401968701440/diary.jpg")
    await client.say(embed=embed)
    
@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def love(ctx):
    love = random.choice([x for x in ctx.message.server.members if not x.bot])
    love2 = random.choice([x for x in ctx.message.server.members if not x.bot])  
    years = random.randint(0, 20)
    months = random.randint(0, 12)
    days = random.randint(0,32)
    embed = discord.Embed(title='We have found a secret couple in the server!', description = '{} loved {} for {} years, {} months and {} days!'.format(love.display_name, love2.display_name, years, months, days))
    embed.set_image(url="https://cdn.discordapp.com/attachments/385419071727992834/472017700110073876/download.jpg")
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def reco(ctx):
    recommended = open('Reco.txt', encoding = "UTF-8").read().splitlines()
    recommended2 = random.choice(recommended)
    embed = discord.Embed(title='I recommend you to try out this command...', description = '**{}**'.format(recommended2))
    embed.set_image(url="https://cdn.discordapp.com/attachments/385419071727992834/462927747149463573/download.jpg")
    await client.say(embed=embed)                       

@client.command(pass_context=True)
async def waud(ctx):
    waud = open('WAUD.txt').read().splitlines()
    wauds = random.choice(waud)
    wauddo = random.choice(["you are doing it right now!","you are not doing it right now, but later.","you are not doing it right now.","you don't do it at all."])
    waudhum = random.choice([x for x in ctx.message.server.members if not x.bot])
    await client.say(' {}, you are {}. If I had to guess, {}.'.format(waudhum.display_name,wauds,wauddo))
    
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!!")

@client.command(pass_context=True)
async def flip(ctx):
    flip = random.choice(["Heads","Tails","DA MIDDLE"])
    await client.say(flip)

@client.command(pass_context=True)
async def amIgay(ctx):
    Areyougay = random.choice(["Maybe","YES,DUH","NOPE"])
    await client.say(Areyougay)
    
@client.command(pass_context=True)
async def howIkms(ctx):
    kms = random.choice (["Jumping off from Trump's wall","Eating too much KFC","Assassinated by Kim Jong Un","Be surrounded by gay people","Killed by a goddamn clown","Having Ebola, Cancer and Depression at the same time","Be surrounded by creepers","Meeting Herobrine for the first time","Attempting to kill hackers","Being as old as 9999 years old","People calling you cringy/idiot"])
    await client.say(kms)

@client.command(pass_context=True)
async def pong(ctx):
    await client.say("Ping!")

@client.command(pass_context=True)
async def pingpong(ctx):
    await client.say("Pong Ping!")

@client.command(pass_context=True)
async def pongping(ctx):
    await client.say("Ping Pong Pung!")

@client.command(pass_context=True)
async def pung(ctx):
    await client.say("What do you expect me to say, huh? PINGPONGPUNGPUN?! WHAT THE HELL BRUH")

@client.command(pass_context=True)
async def roulette(ctx,*, string):
    roulette = random.choice([x for x in ctx.message.server.members if not x.bot])
    await client.say("The winner of ``%s`` is ``%s``" % (string, roulette.display_name))
    
@client.command(pass_context=True)
async def chance(ctx):
    luck = random.choice(["Try again later","Maybe","NOPE","50% chance","Definitely not","Yes, definitely","It depends on your fate","Dunno, maybe ask the owner of this bot?"])
    await client.say(luck)

@client.command(pass_context=True)
async def future(ctx):
    future = random.choice (["In the future, you may die early.","In the future,you may find a cute girl but didn't have a stable family.","In the future, you may found a rich girl, but she kept arguing with you. A few days later, you divorced her, and got depression until you got another relationship.","In the future, you found a braniac girl, but she is loyal to you and you got married happily. You got a good family and died in the age of 100.","In the future, you got your dream job, got a good wife, and got 2 good kids. You died in the age of 120.","In the future, you got your dream job, but your boss wants to fire you asap, so after working for a year, you got fired for no reason.","In the future, you didn't got your dream job, but the salary is high and your co-workers and your boss treats you like a family. You found love there too, and died in the age of 90 with happiness.","In the future,you won the lottery, and you earned 1$.","In the future, you won the lottery of 1 million dollars.","In the future, you bought a ticket for the lottery, but unluckily you lost.","In the future, you were forced to be in war. You died in the battlefield, but hey at least your name will be famous...","In the future, you died pretty early because you fell from a mountain.","`In the future, you met some famous youtubers, and they chose you as their sidekick.","In the future, you got what normal people do.A normal job, a normal family and a normal life. You died because of being too normal.","In the future, you became a millionaire and because of that, you donated a heck ton of money to the needy. In fact, you donated A LOT until you became famous and loved by everyone.",])                               
    await client.say(future)
    
@client.command(pass_context=True)
async def number(ctx):
    luck = random.randint(0, 100)
    await client.say('Your lucky number for today is ``{0}``! Go use that number and win good stuff!'.format(luck))

@client.command(pass_context=True)
async def badnumber(ctx):
    badnumber = random.randint(0,100)
    await client.say('Your unlucky number for today is ``{0}``! Try not to use this number or you will face the consequences...'.format(badnumber))
    
#these here are test commands/references
                         
@client.command(pass_context=True) #embed
async def embed(ctx):
    embed = discord.Embed(title='EMBED PLZ WORK', description='PLEASE MAKE THIS WORK')
    embed.set_image(url="https://cdn.discordapp.com/attachments/385419071727992834/393317821381345280/Wrong.png")
    await client.say(embed=embed)                         

@client.command(pass_context=True) #bot responding to your actions
async def test(ctx):
    await client.say('hi')
    greet = await client.wait_for_message(content='hi')
    await client.say('oo someone replied')
    greet2 = await client.wait_for_message(content='kill')
    await client.say('oi wanna fight')
    greet3 = await client.wait_for_message(content='ok m8 lets go')
    await client.say('ok lets dance u fat boi')
    await client.say('what are u gonna start off with')
 
    def fight(msg):
        return msg.content.startswith('Punch') or msg.content.startswith('Kick')
        
    message = await client.wait_for_message(check=fight)
    await client.say("your text here")                         
                         
@client.command(pass_context=True) #bot talking to u in DM
async def pm(ctx):
    pm = await client.start_private_message(ctx.message.author)
    await client.send_message(pm, "o.o hello there.")
    
@client.command(pass_context=True)
async def poke(ctx, member: discord.Member,string):
    await client.send_message("%s" % (member, string))
                         
@client.command(pass_context=True) #cooldown
async def cd(ctx):
    await asyncio.sleep(10)
    await client.say("Wait for 10 seconds.")
                         
@client.command(pass_context=True) #emoji react
async def reac(ctx):
        embed = discord.Embed(title="Going to be edited.", description="Thumbs up to update.")
        msgtest = await client.say(embed=embed)
        res = await client.wait_for_reaction(['👍', '👎'], message=msgtest)
        embed2 = discord.Embed(title="Embed1", description ="embed2")
        await client.edit_message(msgtest, embed=embed2)
                         
@client.command(pass_context=True) #editing message
async def edit(ctx):
    edit = await client.say("Edit.")
    await client.add_reaction(edit,'2\u20e3')
    edit2 = await client.wait_for_reaction(['3\u20e3'], message=edit)
    await client.edit_message(edit, "Edited!")                         
                  
client.run(str(os.environ.get('BOT_TOKEN')))



