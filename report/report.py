import json;

def json_report(parsing_result, timestamp):
    with open(f"results/report_{timestamp}.json", "w") as f:
        json.dump(parsing_result, f, indent=4)