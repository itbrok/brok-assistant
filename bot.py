from pyrogram import Client, filters
import wolframalpha
# from serpapi import GoogleSearch
import wikipedia



brok = Client(
    "Brok",
    api_id = 15314996,
    api_hash = "f9593ac83c56c823b97b145abb158dc1"
)

@brok.on_message(filters.private)
async def hello(client, message):
    if message.text == "hi":
        await message.reply("hey, i'm not here! fuck off")
    # elif message.text in replis:
    #     await message.reply("hey, i'm not here! fuck off")
    elif "calc" in message.text:
        app_id = "HV9AK4-LTAHK2GA2J"
        client = wolframalpha.Client(app_id)
        indx = message.text.lower().split().index('calc')
        query = message.text.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        await message.reply("The answer is \n" + answer)

    # elif "GoogleSearch" in message.text or "Google" in message.text or "كوكل" in message.text:
    #     params = {
    #         "engine": "google",
    #         "q": message.text,
    #         "api_key": "733cc4afd94d300c7c63f52abbbace82e22271a992a6a7511550440bb6594477"
    #     }

    #     search = GoogleSearch(params)
    #     results = search.get_dict()
    #     organic_results = results["organic_results"][0]["snippet"]
    #     await message.reply(organic_results)
    elif "wiki" in message.text or "wikipedia" in message.text or "ويكيبيديا" in message.text:
        query = message.text.replace("wikipedia", "").replace("ويكيبيديا", "").replace("wiki", "")
        wikipedia.set_lang("ar")
        results = wikipedia.summary(query, sentences = 3)
        if len(results) > 3:
            await message.reply(f"According to Wikipedia\n{results}")
        else:
            await message.reply("No results found.")

  
print("i'm running...")
brok.run()
