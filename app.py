from flask import Flask, request, jsonify  # Import Flask with a capital 'F'
import datetime

app = Flask(__name__)  # Change 'flask' to 'Flask'

@app.route('/api', methods=['GET'])  # Fix the quotes and 'GET' instead of 'GET']
def get_info():
    slack_name = request.args.get('slack_name')  # Correct the spelling of 'args' and 'slack_name'
    track = request.args.get('track')

    current_day = datetime.datetime.utcnow().strftime('%A')
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')  # Correct the strftime format string

    github_file_url = "https://github.com/JCaryourday/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/JCaryourday/repo"

    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

