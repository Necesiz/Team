from AylinRobot import AylinRobot as app
from pyrogram import filters, enums
from pyrogram.types import *
import os, io, time


@app.on_message(filters.command(["alist"],  ["/", ".", "?", "!"]))
async def admins(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`Bu Əmr Yalnız Qruplarda işləyir !`")
    users = "👮 **Admins**:\n"
    bots = "\n🤖 **Bots**:\n"
    async for admin in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           if admin.user.is_bot == False:
               users += f"• **{admin.user.first_name}** - (`{admin.user.id}`)\n"
           elif admin.user.is_bot == True:
               bots += f"• **{admin.user.first_name}** - (`{admin.user.id}`)\n"
    await message.reply(text=(users+bots))


@app.on_message(filters.command("ban",  ["/", ".", "?", "!"]))
async def ban(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("Yalnız qruplarda işləyin !")
    else:
        try:
            if len(message.text.split()) > 1:
                        user_id = message.text.split()[1]
                        chat_id = message.chat.id
                        admin = await app.get_chat_member(message.chat.id, message.from_user.id)
                        try:
                            if admin.privileges.can_restrict_members:
                                 get = await app.get_users(user_id)
                                 await app.ban_chat_member(chat_id, get.id)
                                 return await message.reply(
                                 f'Qadağan edilib  {get.mention}!')
                            else:
                                 await message.reply_text(text = "**İdarəçi hüquqlarınız çatışmır `can_restrict_members `**")
                        except Exception as e:
                               return await message.reply(str(e))                    
            else:
                get = await app.get_chat_member(message.chat.id, message.from_user.id)
                reply = message.reply_to_message
                if not message.reply_to_message:
                    return await message.reply_text("**Kiməsə qadağaya cavab verin .**")
                if not get.privileges:
                    return await message.reply("**Mənə nəzarət etmək üçün Admin Hüquqlarına ehtiyacınız var  (~_^)!**")
                if get.privileges.can_restrict_members:
                     chat_id = message.chat.id
                     user_id  = message.reply_to_message.from_user.id
                     await app.ban_chat_member(chat_id, user_id)
                     await message.reply_text(text= "**Qadağan edildi {}!**".format(reply.from_user.mention))
                else:
                     await message.reply_text(text = "**Sizdə admin hüquqları yoxdur  `can_restrict_members`**")
        except Exception as errors:
           return await message.reply(f"**Error**: {errors}")


@app.on_message(filters.command("unban",  ["/", ".", "?", "!"]))
async def unban(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("Yalnız qruplarda işləyin !")
    else:
        try:
            if len(message.text.split()) > 1:
                        user_id = message.text.split()[1]
                        chat_id = message.chat.id
                        admin = await app.get_chat_member(message.chat.id, message.from_user.id)
                        try:
                            if admin.privileges.can_restrict_members:
                                 get = await app.get_users(user_id)
                                 await app.unban_chat_member(chat_id, get.id)
                                 return await message.reply(
                                'Yaxşı, yenidən qoşula bilərlər .')
                            else:
                                await message.reply_text(text = "**Sizdə admin hüquqları yoxdur  `can_restrict_members`**")
                        except Exception as e:
                               return await message.reply(str(e))                    
            else:
                get = await app.get_chat_member(message.chat.id, message.from_user.id)
                reply = message.reply_to_message
                if not message.reply_to_message:
                    return await message.reply_text("**Qadağanı ləğv etmək üçün kiməsə cavab verin **")
                if not get.privileges:
                    return await message.reply("**MeMənə nəzarət etmək üçün Admin Hüquqlarına ehtiyacınız var  (~_^)!**")
                if get.privileges.can_restrict_members:
                     chat_id = message.chat.id
                     user_id  = message.reply_to_message.from_user.id
                     await app.unban_chat_member(chat_id, user_id)
                     await message.reply_text(text= "**Yaxşı, onlar yenidən qoşula bilərlər .**")
                else:
                     await message.reply_text(text = "**Sizdə admin hüquqları yoxdur  `can_restrict_members`**")
        except Exception as errors:
           return await message.reply(f"**Error**: {errors}")


@app.on_message(filters.command("kick", ["/", ".", "?", "!"]))
async def kick(_, message):
        if len(message.text.split()) > 1:
                user_id = message.text.split()[1]
                chat_id = message.chat.id
                admin = await app.get_chat_member(message.chat.id, message.from_user.id)
                try:
                    if admin.privileges.can_restrict_members:
                         get = await app.get_users(user_id)
                         await app.ban_chat_member(chat_id, get.id)
                         await app.unban_chat_member(chat_id, get.id)
                         return await message.reply(
                         f'Kicked {get.mention}!')
                    else:
                         await message.reply_text(text = "**Sizdə admin hüquqları yoxdur  `can_restrict_members`**")
                except Exception as e:
                   return await message.reply(str(e))                    
        else:
            if not message.reply_to_message:
                   return await message.reply("**Kiməsə təpik atmağa cavab verin .**")
            get = await app.get_chat_member(message.chat.id,message.from_user.id)
            reply = message.reply_to_message
            if not get.privileges:
                  return await message.reply("**Bunu etmək üçün admin olmalısınız .**")
            if get.privileges.can_restrict_members:
                chat_id = message.chat.id
                user_id  = message.reply_to_message.from_user.id
                await app.ban_chat_member(chat_id, user_id)
                await app.unban_chat_member(chat_id, user_id)
                await message.reply_text(text= "**Təpiklə  {}!**".format(reply.from_user.mention))
            else:
                await message.reply_text(text = "**Sizdə admin hüquqları yoxdur  `can_restrict_members`**")


@app.on_message(filters.command("demote", ["/", ".", "?", "!"]))
async def demotes(_, message):
   try:
       if not message.reply_to_message:
             return await message.reply("**Kiməsə cavab verin .**")
       chat_id = message.chat.id
       admin = message.from_user
       user = message.reply_to_message.from_user
       check = await app.get_chat_member(chat_id, admin.id)
       if check.privileges.can_promote_members:
            msg = await message.reply("**Aşağılama Prosesi.**" )
            await message.chat.promote_member(
               user_id=user.id,
               privileges=pyrogram.types.ChatPrivileges(
               can_change_info=False,
               can_invite_users=False,
               can_delete_messages=False,
               can_restrict_members=False,
               can_pin_messages=False,
               can_promote_members=False,
               can_manage_chat=False,
               can_manage_video_chats=False    
))
            await msg.edit(f"""**Admin tərəfindən aşağı salındı **:\n**{admin.mention}**
**Demoted User:** **{user.mention}**""")
   except Exception as errors:
           await message.reply(f"**Error**: {errors}")
       

      
      
@app.on_message(filters.command("promote", ["/", ".", "?", "!"]))
async def promoting(_, message):
     global new_admin
     if not message.reply_to_message:
         return await message.reply("**Təbliğat üçün kiməsə cavab verin .**")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user
     user_stats = await app.get_chat_member(chat_id, admin.id)
     bot_stats = await app.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await message.reply("**lol! Nə vaxt məni admin et !**")
     elif not user_stats.privileges:
         return await message.reply("**Mənə nəzarət etmək üçün Admin Hüquqlarına ehtiyacınız var  (~_^)!**")
     elif not bot_stats.privileges.can_promote_members:
         return await message.reply("**Admin hüquqlarını itirmişəm  `can_promote_members`**")
     elif not user_stats.privileges.can_promote_members:
         return await message.reply("**Sizdə admin hüquqları yoxdur  `can_promote_members`**")
     elif user_stats.privileges.can_promote_members:
          msg = await message.reply_text("**Təşviq Prosesi .**")
          await app.promote_chat_member(
            chat_id,
            new_admin.id,
            privileges=pyrogram.types.ChatPrivileges(
            can_change_info=True,
            can_delete_messages=True,
            can_pin_messages=True,
            can_invite_users=True,
            can_manage_video_chats=True,
            can_restrict_members=True
))
          await msg.edit(f"""**Təşviq edilmiş Admin **:\n**{admin.mention}**
          **New Admin:**\n**{new_admin.mention}** """,
              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Aşağı salmaq ", callback_data="demote"),
                                                        InlineKeyboardButton(text="Sil ", callback_data="close")]]))
                               
     
                     
@app.on_callback_query(filters.regex("demote"))
async def demoting(_, query):
         chat_id = query.message.chat.id
         stats = await app.get_chat_member(query.message.chat.id, query.from_user.id)
         if stats.privileges.can_promote_members:
                  await app.promote_chat_member(
                     chat_id,
            new_admin.id,
            privileges=pyrogram.types.ChatPrivileges(
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_video_chats=False    
))
                  await query.message.edit(f"""**Admin tərəfindən aşağı salın :**\n** {query.from_user.mention}**
**Vəzifəsi aşağı salınmış Admin :**\n**{new_admin.mention}**""")    
         else:
               await query.answer("Siz aşağı edə bilməzsiniz !", show_alert=True )
                    
        
@app.on_message(filters.command("del", ["/", ".", "?", "!"]))
async def delete(_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     user_stats = await app.get_chat_member(chat.id, user.id)
     bot_stats = await app.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
           return await m.reply_text("Make Me Admin REEE!!")
     elif not user_stats.privileges:
            return await m.reply_text("Only Admins are allowed to use this command!")    
     elif not reply:
            return  await m.reply_text("reply to message for deleting")
     elif not bot_stats.privileges.can_delete_messages:
              return await m.reply_text("**I'm missing the permission of**:\n`can_delete_messages`")
     elif not user_stats.privileges.can_delete_messages:
              return await m.reply_text("**your are missing the permission of**:\n`can_delete_messages`")
     elif user_stats.privileges.can_delete_messages:
               await reply.delete()
               await m.delete()
               
                     
@app.on_message(filters.command(["setgtitle","setchattitle"], ["/", ".", "?", "!"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     new_title = m.text.split(None, 1)[1]
     user_stats = await app.get_chat_member(chat.id, user.id)
     bot_stats = await app.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
           return await m.reply_text("Make Me Admin REEE!!")
     elif not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     elif not bot_stats.privileges.can_manage_chat:
               await m.reply_text("**I'm missing the permission of**:\n`can_manage_chat`")
               return 
     elif not user_stats.privileges.can_manage_chat:
               await m.reply_text("**your are missing the permission of**:\n`can_manage_chat`")
               return 
     elif user_stats.privileges.can_manage_chat:
               await m.chat.set_title(new_title)
               await m.reply_text(f"Successfully set {new_title} as new chat title!")

@app.on_message(filters.command(["setgpic","setchatpic"], ["/", ".", "?", "!"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     user_stats = await app.get_chat_member(chat.id, user.id)
     bot_stats = await app.get_chat_member(chat.id, "self")
     
     if not reply:
              return await m.reply_text("reply only document or photo")
      
     elif not bot_stats.privileges:
            return await m.reply_text("Make Me Admin REEE!!")
             
     elif not user_stats.privileges:
           return await m.reply_text("Only Admins are allowed to use this command!")
             
     elif not bot_stats.privileges.can_change_info:
             return await m.reply_text("**I'm missing the permission of**:\n`can_change_info`")
                
     elif not user_stats.privileges.can_change_info:
               return await m.reply_text("**your are missing the permission of**:\n`can_change_info`")
                
     elif user_stats.privileges.can_change_info:
               msg = await m.reply("**New Group Photo Process.**")
               photo = await reply.download()
               await bot.set_chat_photo(chat.id, photo=photo)
               await msg.edit_text("**Successfully group photo Applied**")

