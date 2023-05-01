import discord
import asyncio
import pytz
import os
from keep_alive import keep_alive
from datetime import datetime, time

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# Define the local timezone for Bangladesh
# bd_tz = pytz.timezone('Asia/Dhaka')

# Define a function that sends a message to the target channel
async def send_message():
  now = datetime.now()
  time_string = now.strftime("%H:%M:%S")
  # get day of week as an integer
  x = now.weekday()

  # Get the current time in Bangladesh timezone
  # current_time = datetime.now(bd_tz).time()
  # time_string = current_time.strftime("%H:%M:%S")
  print(time_string)
  if '00:01' in time_string and x == 4:
    channel = discord.utils.get(client.get_all_channels(), name='js-mentors')
    await channel.send(
      "Weekly Evaluation\n1. Weekly activity - 10 marks\nHow active the mentee was throughout the week based on their daily updates\n2. Communication skill - 10 marks\nBased on their verbal communicating excellence at the weekly presentations\n3. Technical depth - 10 marks\nPerformance in the viva-voce\n\nYou can put the mark on the mentor group using /weekly_evaluation or direct."
    )

    channel = discord.utils.get(client.get_all_channels(), name='spring-boot-mentors')
    await channel.send(
      "Weekly Evaluation\n1. Weekly activity - 10 marks\nHow active the mentee was throughout the week based on their daily updates\n2. Communication skill - 10 marks\nBased on their verbal communicating excellence at the weekly presentations\n3. Technical depth - 10 marks\nPerformance in the viva-voce\n\nYou can put the mark on the mentor group using /weekly_evaluation or direct."
    )

    channel = discord.utils.get(client.get_all_channels(), name='flutter-mentors')
    await channel.send(
      "Weekly Evaluation\n1. Weekly activity - 10 marks\nHow active the mentee was throughout the week based on their daily updates\n2. Communication skill - 10 marks\nBased on their verbal communicating excellence at the weekly presentations\n3. Technical depth - 10 marks\nPerformance in the viva-voce\n\nYou can put the mark on the mentor group using /weekly_evaluation or direct."
    )

    channel = discord.utils.get(client.get_all_channels(), name='dotnet-mentors')
    await channel.send(
      "Weekly Evaluation\n1. Weekly activity - 10 marks\nHow active the mentee was throughout the week based on their daily updates\n2. Communication skill - 10 marks\nBased on their verbal communicating excellence at the weekly presentations\n3. Technical depth - 10 marks\nPerformance in the viva-voce\n\nYou can put the mark on the mentor group using /weekly_evaluation or direct."
    )

    channel = discord.utils.get(client.get_all_channels(), name='django-mentors')
    await channel.send(
      "Weekly Evaluation\n1. Weekly activity - 10 marks\nHow active the mentee was throughout the week based on their daily updates\n2. Communication skill - 10 marks\nBased on their verbal communicating excellence at the weekly presentations\n3. Technical depth - 10 marks\nPerformance in the viva-voce\n\nYou can put the mark on the mentor group using /weekly_evaluation or direct."
    )

    channel = discord.utils.get(client.get_all_channels(), name='kotlin-mentors')
    await channel.send(
      "Weekly Evaluation\n1. Weekly activity - 10 marks\nHow active the mentee was throughout the week based on their daily updates\n2. Communication skill - 10 marks\nBased on their verbal communicating excellence at the weekly presentations\n3. Technical depth - 10 marks\nPerformance in the viva-voce\n\nYou can put the mark on the mentor group using /weekly_evaluation or direct."
    )

    

@client.event
async def on_ready():
  print(f'Logged in as {client.user.name} (ID: {client.user.id})')
  print('------')
  # now = datetime.now()
  # time = now.strftime("%H:%M:%S")
  # print(time)
  # dt = datetime.now()
  # print('Datetime is:', dt)

  # get day of week as an integer
  # x = dt.weekday()
  # print(x)
  # current_time = datetime.now(bd_tz).time()
  # print(bd_tz)
  # print(current_time)
  # print(time(hour=21, minute=42))

  while True:
    await send_message()
    await asyncio.sleep(60)


keep_alive()
client.run(os.getenv('Mehrab_ReminderBot'))
