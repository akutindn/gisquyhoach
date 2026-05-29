# -*- coding: utf-8 -*-
"""Fix JS conflict in chat widget — rename history → chatHistory, fix IIFE"""
import os, re

BASE = r"F:\ARCHILABS_AI\gis-landing"
with open(os.path.join(BASE,"index.html"), encoding="utf-8") as f:
    html = f.read()

# Tìm IIFE block cuối cùng (chat widget)
pattern = r'\(function\(\)\{.*?\}\)\(\);'
matches = list(re.finditer(pattern, html, re.DOTALL))
print(f"Found {len(matches)} IIFE blocks")

# IIFE mới sạch — dùng chatHistory, không shadow window.history
NEW_JS = r"""(function(){
  var BACKEND = 'http://localhost:8000/chat';
  var FB = '\u{1F60A} Xin l\u1ED7i, AI \u0111ang b\u1EA3o tr\xEC. Li\xEAn h\u1EC7 Zalo <a href="https://zalo.me/0332945089" target="_blank" style="color:#a78bfa">0332 945 089</a>';
  var chatHistory = [];
  var isOpen = false;
  var isTyping = false;

  function $(id){ return document.getElementById(id); }
  var panel    = $('aiChatPanel');
  var btn      = $('aiChatBtn');
  var closeBtn = $('aiChatClose');
  var msgs     = $('aiMsgs');
  var inp      = $('aiInput');
  var sendBtn  = $('aiSend');
  var tooltip  = $('aiTooltip');
  var quick    = $('aiQuick');

  if(!btn || !panel){ console.warn('GisVN Chat: elements not found'); return; }

  btn.addEventListener('click', function(){ isOpen ? close() : open(); });
  closeBtn.addEventListener('click', close);

  function open(){
    isOpen = true;
    panel.classList.add('open');
    btn.textContent = '\u2715';
    tooltip.style.display = 'none';
    if(!chatHistory.length) greeting();
    setTimeout(function(){ inp.focus(); }, 350);
  }
  function close(){
    isOpen = false;
    panel.classList.remove('open');
    btn.textContent = '\uD83E\uDD16';
    tooltip.style.display = '';
  }

  function greeting(){
    var g = 'Xin ch\xE0o! \uD83D\uDC4B T\xF4i l\xE0 Gissy \u2014 tr\u1EE3 l\xFD AI c\u1EE7a GisVN.\n\nT\xF4i c\xF3 th\u1EC3 gi\xFAp b\u1EA1n t\xEC m hi\u1EC3u d\u1ECBch v\u1EE5, Th\xF4ng t\u01B0 16, quy tr\xECnh v\xE0 chi ph\xED. B\u1EA1n \u0111ang c\u1EA7n h\u1ED7 tr\u1EE3 v\u1EC1 v\u1EA5n \u0111\u1EC1 g\xEC?';
    addBubble('bot', g);
    chatHistory.push({role:'assistant', content: g});
  }

  async function send(text){
    text = (text||'').trim();
    if(!text || isTyping) return;
    addBubble('user', text);
    chatHistory.push({role:'user', content: text});
    inp.value = '';
    inp.style.height = 'auto';
    if(quick) quick.style.display = 'none';
    showDots();
    sendBtn.disabled = true;
    try {
      var res = await fetch(BACKEND, {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({messages: chatHistory}),
        signal: AbortSignal.timeout(15000)
      });
      var d = await res.json();
      hideDots();
      var reply = d.error ? FB : d.reply;
      addBubble('bot', reply);
      if(!d.error) chatHistory.push({role:'assistant', content: reply});
    } catch(e){
      hideDots();
      addBubble('bot', FB);
    }
    sendBtn.disabled = false;
  }

  window.sendQuick = send;

  sendBtn.addEventListener('click', function(){ send(inp.value); });
  inp.addEventListener('keydown', function(e){
    if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); send(inp.value); }
  });
  inp.addEventListener('input', function(){
    inp.style.height = 'auto';
    inp.style.height = Math.min(inp.scrollHeight,80)+'px';
  });

  function timeStr(){
    return new Date().toLocaleTimeString('vi-VN',{hour:'2-digit',minute:'2-digit'});
  }
  function addBubble(role, text){
    var d = document.createElement('div');
    d.className = 'chat-msg '+role;
    var h = text.replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/\n/g,'<br>');
    var align = role==='user' ? 'right' : 'left';
    d.innerHTML = '<div class="msg-bubble">'+h+'</div><div class="msg-time" style="text-align:'+align+'">'+timeStr()+'</div>';
    msgs.appendChild(d);
    msgs.scrollTop = msgs.scrollHeight;
  }

  var typingEl = null;
  function showDots(){
    isTyping = true;
    typingEl = document.createElement('div');
    typingEl.className = 'chat-msg bot';
    typingEl.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
    msgs.appendChild(typingEl);
    msgs.scrollTop = msgs.scrollHeight;
  }
  function hideDots(){
    isTyping = false;
    if(typingEl){ typingEl.remove(); typingEl = null; }
  }

  setTimeout(function(){
    if(!isOpen && tooltip){ tooltip.style.opacity='0'; tooltip.style.transition='opacity 1s'; }
  }, 4000);
})();"""

if matches:
    # Thay IIFE cuối cùng (chat widget)
    last = matches[-1]
    html = html[:last.start()] + NEW_JS + html[last.end():]
    print("Replaced last IIFE block")
else:
    # Append trước </script>
    html = html.replace("</script>", NEW_JS + "\n</script>", 1)
    print("Appended new JS before </script>")

with open(os.path.join(BASE,"index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("✅ Fixed!")
