def lineup_students(st):
    a = st.split()
    return sorted(a,key=len,reverse=True)
print(lineup_students('Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'))





