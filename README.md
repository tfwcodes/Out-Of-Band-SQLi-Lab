### Solving the lab

<li> └─$ ./interactsh-client 

    _       __                       __       __  
   (_)___  / /____  _________ ______/ /______/ /_ 
  / / __ \/ __/ _ \/ ___/ __ '/ ___/ __/ ___/ __ \
 / / / / / /_/  __/ /  / /_/ / /__/ /_(__  ) / / /
/_/_/ /_/\__/\___/_/   \__,_/\___/\__/____/_/ /_/

                projectdiscovery.io

[INF] Current interactsh version 1.3.1 (latest)

[INF] Listing 1 payload for OOB Testing
[INF] d81es9k940njri5m0rr03crqndfyjeesp.oast.pro

<li> This is our payload for the oob client: curl -H "User-Agent: trigger_callback" "http://127.0.0.1:5000/vulnerable?input=trigger_callback"

<li> After we inject our payload, we get a response in the interactsh-client:
