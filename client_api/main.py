from pyrogram import Client

api_id = 20088125
api_hash = 'df438ec39f11da28a9fdab53db8bd194'

app = Client('my_account', api_id, api_hash)

app.start()
app.send_message('me', 'Привет, это я!')
app.stop()
