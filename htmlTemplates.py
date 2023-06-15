css = '''
<style>
.chat-message {
    padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #ff4d4d
}
.chat-message.bot {
    background-color: #475063
}

.chat-message .message {
  color: #fff;
  align-items: center;
  justify-content: center;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">  
    <div class="message">{{MSG}}</div>
</div>
'''
