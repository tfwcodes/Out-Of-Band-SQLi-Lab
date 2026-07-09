### Solving the lab



<li> We firstly start our interact sh client: 
    └─$ ./interactsh-client 
[INF] Current interactsh version 1.3.1 (latest)

[INF] Listing 1 payload for OOB Testing
[INF] d81es9k940njri5m0rr03crqndfyjeesp.oast.pro

<li> This is our payload for the oob client: curl -H "User-Agent: trigger_callback" "http://127.0.0.1:5000/vulnerable?input=trigger_callback"

<li> After we inject our payload, we get a response in the interactsh-client:
