import time
from honcho import Honcho
h = Honcho(workspace_id="jl-probe")
u = h.peer("maya")
try:
    print("SCHEDULE:", h.schedule_dream(u))
except Exception as e:
    print("schedule_dream failed:", e)
    try:
        print("SCHEDULE (alt):", h.schedule_dream(observer="maya"))
    except Exception as e2:
        print("alt failed:", e2)
time.sleep(150)
print("REP:", u.representation())
print("CARD:", u.get_card())
r = u.chat("Where does Maya live right now? One sentence.", reasoning_level="high", include_evidence=True)
print("ANS:", getattr(r, "content", r))
ev = getattr(r, "evidence", None)
print("EV conclusions:", getattr(ev, "conclusions", None))
print("EV messages:", getattr(ev, "messages", None))
