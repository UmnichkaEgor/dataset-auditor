import json
import os 
import argparse

def inspect_json(filepath):
    try:
        with open(filepath, "r") as file_json:
            data = json.load(file_json)
    except (json.JSONDecodeError, FileNotFoundError) as error:
        return {"status":"corrupted", "error":str(error)}
    else:
        return {"status":"ok", "data":data}

def parse_log(filepath):
    w, ww = 0, 0
    try:
        with open(filepath, "r") as file_log:
            for i in file_log:
                data = i.split()
                w += float(data[3])
                ww += 1
    except FileNotFoundError as error:
        return {"status":"corrupted", "error":str(error)}
    else:
        if ww != 0:
            return {"status":"ok", "mean_loss":round(w/ww, 2)}
        else:
            return {"status":"corrupted", "error":"file is empty"}

def scan_directory(dirpath):
    results = {}
    if not os.path.exists(dirpath): 
        return {"error":"Directory not found"}
    for i in os.listdir(dirpath):
        if i.endswith(".json"):
            results[i] = insepct_json(os.path.join(dirpath, i))
        elif i.endswith(".log"):
            results[i] = parse_log(os.path.join(dirpath, i))
    return results

def generate_audit_report(scan_results):
    successful_files = 0
    corrupted_files = 0
    errors = []
    for i, j in scan_results.items():
        if j["status"] == "ok":
            successful_files += 1
        else:
            corrupted_files += 1
            errors.append({"file":i, "error":j["error"]})
    return {"total_files":len(scan_results),
            "successful_files":successful_files,
            "corrupted_files":corrupted_files,
            "errors":errors
}

parser = argparse.ArgumentParser(
    description="Automated dataset auditing tool for validating JSON files and analyzing training logs."
)
parser.add_argument("--dir", type=str, required=True, help="Path to the target directory containing dataset files")
args = parser.parse_args()

with open("audit_report.json", "w") as file:
    json.dump(generate_audit_report(scan_directory(args.dir)), file, indent=4)

print("Report saved to audit_report.json")