import time
from honcho import Honcho

h = Honcho(workspace_id="jl-probe")
user = h.peer("maya")
asst = h.peer("assistant")
s = h.session("probe-1")
s.add_peers([user, asst])

msgs = [
    user.message("I just moved to Boston for a new job at a biotech startup."),
    asst.message("Congrats! How are you finding Boston?"),
    user.message("Cold. I run along the Charles most mornings though, usually 5k."),
    user.message("My manager wants me to present at the offsite next month, kind of dreading it."),
    asst.message("What's the presentation on?"),
    user.message("Our assay pipeline. I'm more comfortable in the lab than on stage."),
    user.message("Big news: I took a role at a hospital system in Chicago. Moving next week."),
    asst.message("That's a big change. Excited?"),
    user.message("Yeah. Sad to lose the river runs though."),
    user.message("Settled in Chicago now. Lakefront path isn't bad actually."),
]
s.add_messages(msgs)

print("waiting for deriver..."); time.sleep(120)

qs = {
  "update":  "Where does Maya live right now? One sentence.",
  "absent":  "What is Maya's favorite movie? One sentence.",
  "implied": "Is Maya more of an introvert or extrovert? One sentence, and say how confident you are.",
}
for level in ["minimal", "high"]:
    for name, q in qs.items():
        for i in range(3):
            try:
                r = user.chat(q, reasoning_level=level, include_evidence=True)
            except TypeError:
                r = user.chat(q, reasoning_level=level)
            ans = getattr(r, "content", r)
            print(f"[{level}][{name}][run{i}] {ans}")
            ev = getattr(r, "evidence", None)
            if ev:
                print("   evidence:", getattr(ev, "conclusions", ev))
        print()

print("REPRESENTATION:"); print(user.representation(search_query="location"))
print("CARD:"); print(user.get_card())
