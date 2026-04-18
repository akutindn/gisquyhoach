# -*- coding: utf-8 -*-
"""Inject AI chat widget vào GIS Quy Hoạch landing page"""
import os

BASE = r"F:\ARCHILABS_AI\gis-landing"

CHAT_CSS = """
/* ══ AI CHAT WIDGET ══════════════════════════════════════════════ */
.ai-chat-btn{position:fixed;bottom:108px;right:28px;z-index:9998;
  width:58px;height:58px;border-radius:50%;
  background:linear-gradient(135deg,#7c3aed,#4f46e5);
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 8px 24px rgba(124,58,237,.5);
  cursor:pointer;border:none;font-size:26px;
  animation:ai-pulse 3s ease-in-out infinite;transition:all .2s;}
.ai-chat-btn:hover{transform:scale(1.1);}
@keyframes ai-pulse{0%,100%{box-shadow:0 8px 24px rgba(124,58,237,.5),0 0 0 0 rgba(124,58,237,.3);}
  60%{box-shadow:0 8px 24px rgba(124,58,237,.5),0 0 0 12px rgba(124,58,237,0);}}
.ai-chat-tooltip{position:fixed;bottom:118px;right:96px;z-index:9998;
  background:rgba(0,0,0,.85);color:#fff;font-size:12px;font-weight:700;
  padding:6px 12px;border-radius:8px;white-space:nowrap;
  backdrop-filter:blur(8px);pointer-events:none;}
.ai-chat-panel{position:fixed;bottom:28px;right:28px;z-index:9997;
  width:380px;height:520px;background:#080f1e;
  border:1px solid rgba(124,58,237,.3);border-radius:20px;
  box-shadow:0 32px 80px rgba(0,0,0,.6);
  display:flex;flex-direction:column;overflow:hidden;
  transform:scale(.95) translateY(20px);opacity:0;
  transition:all .3s cubic-bezier(.34,1.56,.64,1);pointer-events:none;}
.ai-chat-panel.open{transform:scale(1) translateY(0);opacity:1;pointer-events:all;}
.acp-header{background:linear-gradient(135deg,rgba(124,58,237,.2),rgba(79,70,229,.2));
  border-bottom:1px solid rgba(124,58,237,.2);padding:14px 18px;
  display:flex;align-items:center;gap:12px;}
.acp-ava{width:38px;height:38px;border-radius:50%;
  background:linear-gradient(135deg,#7c3aed,#4f46e5);
  display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;}
.acp-info strong{display:block;font-size:14px;font-weight:800;color:#fff;}
.acp-info span{font-size:12px;color:#a78bfa;}
.acp-status{display:inline-block;width:8px;height:8px;border-radius:50%;
  background:#10b981;box-shadow:0 0 6px #10b981;animation:status-blink 2s infinite;}
@keyframes status-blink{0%,100%{opacity:1;}50%{opacity:.5;}}
.acp-close{margin-left:auto;background:none;border:none;color:#6b7280;
  font-size:18px;cursor:pointer;padding:4px;border-radius:6px;transition:all .2s;}
.acp-close:hover{background:rgba(255,255,255,.07);color:#fff;}
.acp-msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:12px;
  scrollbar-width:thin;scrollbar-color:rgba(124,58,237,.3) transparent;}
.acp-msgs::-webkit-scrollbar{width:4px;}
.acp-msgs::-webkit-scrollbar-thumb{background:rgba(124,58,237,.3);border-radius:4px;}
.chat-msg{max-width:85%;animation:msg-in .3s ease;}
@keyframes msg-in{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
.chat-msg.bot{align-self:flex-start;}
.chat-msg.user{align-self:flex-end;}
.msg-bubble{padding:10px 14px;border-radius:14px;font-size:13px;line-height:1.6;}
.chat-msg.bot  .msg-bubble{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);
  border-bottom-left-radius:4px;color:#e2e8f0;}
.chat-msg.user .msg-bubble{background:linear-gradient(135deg,#7c3aed,#4f46e5);
  color:#fff;border-bottom-right-radius:4px;}
.msg-time{font-size:10px;color:#4a5568;margin-top:4px;
  padding:0 4px;text-align:right;}
.chat-msg.bot .msg-time{text-align:left;}
.typing-dots{display:flex;gap:4px;align-items:center;padding:10px 14px;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);
  border-radius:14px;border-bottom-left-radius:4px;width:fit-content;}
.typing-dots span{width:7px;height:7px;border-radius:50%;background:#7c3aed;
  animation:dot-bounce .8s ease-in-out infinite;}
.typing-dots span:nth-child(2){animation-delay:.15s;}
.typing-dots span:nth-child(3){animation-delay:.3s;}
@keyframes dot-bounce{0%,100%{transform:translateY(0);}50%{transform:translateY(-5px);}}
.acp-quick{padding:8px 12px;display:flex;gap:6px;flex-wrap:wrap;
  border-top:1px solid rgba(255,255,255,.05);}
.quick-btn{background:rgba(124,58,237,.12);border:1px solid rgba(124,58,237,.25);
  color:#a78bfa;font-size:11px;font-weight:700;padding:5px 10px;border-radius:20px;
  cursor:pointer;transition:all .2s;white-space:nowrap;}
.quick-btn:hover{background:rgba(124,58,237,.25);color:#c4b5fd;}
.acp-input-row{border-top:1px solid rgba(255,255,255,.07);padding:12px;
  display:flex;gap:8px;align-items:center;}
.acp-input{flex:1;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:10px;padding:10px 14px;color:#fff;font-family:'Be Vietnam Pro',sans-serif;
  font-size:13px;outline:none;resize:none;transition:all .2s;max-height:80px;}
.acp-input:focus{border-color:rgba(124,58,237,.5);box-shadow:0 0 0 3px rgba(124,58,237,.1);}
.acp-send{width:38px;height:38px;border-radius:10px;
  background:linear-gradient(135deg,#7c3aed,#4f46e5);color:#fff;
  border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;
  font-size:16px;transition:all .2s;flex-shrink:0;}
.acp-send:hover{transform:scale(1.05);}
.acp-send:disabled{opacity:.4;cursor:not-allowed;transform:none;}
@media(max-width:768px){
  .ai-chat-panel{width:calc(100vw - 32px);right:16px;bottom:16px;height:460px;}
  .ai-chat-btn{bottom:90px;right:16px;}
  .ai-chat-tooltip{display:none;}
}
"""

CHAT_HTML = """
<!-- ══ AI CHAT WIDGET ══════════════════════════════════════════════ -->
<div class="ai-chat-tooltip" id="aiTooltip">🤖 Hỏi Gissy AI</div>
<button class="ai-chat-btn" id="aiChatBtn" title="Chat với Gissy AI">🤖</button>

<div class="ai-chat-panel" id="aiChatPanel">
  <div class="acp-header">
    <div class="acp-ava">🤖</div>
    <div class="acp-info">
      <strong>Gissy AI <span class="acp-status"></span></strong>
      <span>Tư vấn viên GIS · Phản hồi tức thì</span>
    </div>
    <button class="acp-close" id="aiChatClose">✕</button>
  </div>
  <div class="acp-msgs" id="aiMsgs"></div>
  <div class="acp-quick" id="aiQuick">
    <button class="quick-btn" onclick="sendQuick('Chuyển đổi CAD sang GIS mất bao lâu?')">⏱ Mất bao lâu?</button>
    <button class="quick-btn" onclick="sendQuick('Chi phí dịch vụ như thế nào?')">💰 Chi phí?</button>
    <button class="quick-btn" onclick="sendQuick('Thông tư 16 yêu cầu gì về GIS?')">📋 TT16 là gì?</button>
    <button class="quick-btn" onclick="sendQuick('Hồ sơ bị trả lại, GIS Quy Hoạch có hỗ trợ không?')">🆘 Bị trả lại?</button>
  </div>
  <div class="acp-input-row">
    <textarea class="acp-input" id="aiInput" placeholder="Nhập câu hỏi..." rows="1"></textarea>
    <button class="acp-send" id="aiSend" title="Gửi">➤</button>
  </div>
</div>
"""

CHAT_JS = """
// ══ GIS Quy Hoạch AI Chat Widget ══════════════════════════════════════════
(function(){
  const BACKEND = 'http://localhost:8000/chat';
  const FALLBACK_MSG = '😊 Xin lỗi, hệ thống AI đang bảo trì. Bạn vui lòng liên hệ trực tiếp qua Zalo <a href="https://zalo.me/0332945089" target="_blank" style="color:#a78bfa">0332 945 089</a> nhé!';

  let history = [];
  let isOpen  = false;
  let isTyping= false;

  const panel   = document.getElementById('aiChatPanel');
  const btn     = document.getElementById('aiChatBtn');
  const closeBtn= document.getElementById('aiChatClose');
  const msgs    = document.getElementById('aiMsgs');
  const input   = document.getElementById('aiInput');
  const sendBtn = document.getElementById('aiSend');
  const tooltip = document.getElementById('aiTooltip');
  const quick   = document.getElementById('aiQuick');

  // Toggle panel
  btn.onclick = () => { isOpen ? closeChatPanel() : openChatPanel(); };
  closeBtn.onclick = closeChatPanel;

  function openChatPanel(){
    isOpen = true;
    panel.classList.add('open');
    btn.textContent = '✕';
    tooltip.style.display = 'none';
    if (!history.length) sendGreeting();
    setTimeout(() => input.focus(), 300);
  }
  function closeChatPanel(){
    isOpen = false;
    panel.classList.remove('open');
    btn.textContent = '🤖';
    tooltip.style.display = '';
  }

  // Auto-hide tooltip after 4s
  setTimeout(() => { if (!isOpen) tooltip.style.opacity = '0'; }, 4000);

  // Greeting from Gissy
  function sendGreeting(){
    const greet = 'Xin chào! 👋 Tôi là **Gissy** — trợ lý AI của GIS Quy Hoạch. Tôi có thể giúp bạn tìm hiểu về dịch vụ lập hồ sơ quy hoạch trên GIS, Thông tư 16, quy trình và chi phí.\\n\\nBạn đang cần hỗ trợ về vấn đề gì?';
    appendMsg('bot', greet);
    history.push({ role: 'assistant', content: greet });
  }

  // Send message
  async function sendMsg(text){
    if (!text.trim() || isTyping) return;
    text = text.trim();
    appendMsg('user', text);
    history.push({ role: 'user', content: text });
    input.value = '';
    input.style.height = 'auto';
    quick.style.display = 'none';

    showTyping();
    sendBtn.disabled = true;

    try {
      const res = await fetch(BACKEND, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: history }),
        signal: AbortSignal.timeout(15000)
      });
      const data = await res.json();
      hideTyping();
      if (data.error) {
        appendMsg('bot', FALLBACK_MSG);
      } else {
        appendMsg('bot', data.reply);
        history.push({ role: 'assistant', content: data.reply });
      }
    } catch(e) {
      hideTyping();
      appendMsg('bot', FALLBACK_MSG);
    }
    sendBtn.disabled = false;
  }

  // Quick question buttons
  window.sendQuick = (text) => sendMsg(text);

  // Send on button click
  sendBtn.onclick = () => sendMsg(input.value);

  // Send on Enter (Shift+Enter = newline)
  input.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMsg(input.value);
    }
  });

  // Auto-resize textarea
  input.addEventListener('input', () => {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 80) + 'px';
  });

  // Append message bubble
  function appendMsg(role, text){
    const div = document.createElement('div');
    div.className = 'chat-msg ' + role;
    const now = new Date().toLocaleTimeString('vi-VN', {hour:'2-digit',minute:'2-digit'});
    // Convert **bold** and newlines
    const html = text
      .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
      .replace(/\\n/g, '<br>');
    div.innerHTML = `<div class="msg-bubble">${html}</div><div class="msg-time">${now}</div>`;
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
  }

  // Typing indicator
  let typingEl = null;
  function showTyping(){
    isTyping = true;
    typingEl = document.createElement('div');
    typingEl.className = 'chat-msg bot';
    typingEl.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
    msgs.appendChild(typingEl);
    msgs.scrollTop = msgs.scrollHeight;
  }
  function hideTyping(){
    isTyping = false;
    if (typingEl) { typingEl.remove(); typingEl = null; }
  }
})();
"""

# Đọc file hiện tại
with open(os.path.join(BASE, "index.html"), encoding="utf-8") as f:
    html = f.read()

# Thêm CSS vào trước </style>
html = html.replace("</style>", CHAT_CSS + "\n</style>")

# Thêm HTML widget trước floating Zalo (để Zalo vẫn nằm trên cùng)
html = html.replace(
    "<!-- ══ FLOATING ZALO BUTTON",
    CHAT_HTML + "\n<!-- ══ FLOATING ZALO BUTTON"
)

# Thêm JS trước </script>
html = html.replace("</script>", CHAT_JS + "\n</script>")

with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Chat widget đã được tích hợp!")
