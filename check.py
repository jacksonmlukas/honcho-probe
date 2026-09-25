from honcho import Honcho
h = Honcho(workspace_id="jl-probe")
u = h.peer("maya")
print("REP:", u.representation())
print("CARD:", u.get_card())
print("CTX:", u.context())
