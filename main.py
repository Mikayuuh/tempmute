@client.command()
@commands.has_any_role(RolID, RolID, RolID) # komutu role özel yapmak isterseniz :)
async def tempmute(ctx, member : discord.Member, time=0, reason=None):
    if not member or time == 0 or time == str:
        await ctx.channel.send(embed=commanderror)
        return
    elif reason == None:
        reason = "Sebep Verilmedi"

    muteRole = discord.utils.get(ctx.guild.roles, id=RolID) #muted rol id
    await member.add_roles(muteRole)

    tempMuteEmbed = discord.Embed(colour=embedcolour, description=f"**Sebep:** {reason}")
    tempMuteEmbed.set_author(name=f"{member} Mutelendi :+1:", icon_url=f"{member.avatar_url}")
    tempMuteEmbed.set_footer(text=embedfooter)

    await ctx.channel.send(embed=tempMuteEmbed)

    tempMuteModLogEmbed = discord.Embed(color=embedcolour)
    tempMuteModLogEmbed.set_author(name=f"Mute {member}", icon_url=f"{member.avatar_url}")
    tempMuteModLogEmbed.add_field(name="Kullanıcı", value=f"{member.mention}")
    tempMuteModLogEmbed.add_field(name="Moderatör", value=f"{ctx.message.author}")
    tempMuteModLogEmbed.add_field(name="Sebep", value=f"{reason}")
    tempMuteModLogEmbed.add_field(name="Süre", value=f"{str(time)}")
    tempMuteModLogEmbed.set_footer(text=embedfooter)
    modlog = client.get_channel(KanalID) # modlog kanal id
    await modlog.send(embed=tempMuteModLogEmbed) # mute log atar

    tempMuteDM = discord.Embed(color=embedcolour, title="Mute Bildirimi", description="**SUNUCU İSMİ** Sunucusunda Mutelendiniz")
    tempMuteDM.set_footer(text=embedfooter)
    tempMuteDM.add_field(name="Sebep", value=f"{reason}")
    tempMuteDM.add_field(name="Süre", value=f"{time}")

    userToDM = client.get_user(member.id)
    await userToDM.send(embed=tempMuteDM)

    await asyncio.sleep(time)
    await member.remove_roles(muteRole)

    unMuteModLogEmbed = discord.Embed(color=embedcolour)
    unMuteModLogEmbed.set_author(name=f"Unmute {member}", icon_url=f"{member.avatar_url}")
    unMuteModLogEmbed.add_field(name="Kullanıcı", value=f"{member.mention}")
    unMuteModLogEmbed.set_footer(text=embedfooter)
    modlog = client.get_channel(kanalID) # modlog kanal id
    await modlog.send(embed=unMuteModLogEmbed) # unmute log atar
