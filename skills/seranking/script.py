import os
import json
import httpx

BASE = "https://api.seranking.com/v1"

try:
    api_key = os.environ["SERANKING_API_KEY"]
    inp = json.loads(os.environ.get("INPUT_JSON", "{}"))
    action = inp.get("action", "")

    if action == "backlinks_summary":
        domain = inp.get("domain", "")
        with httpx.Client(timeout=45) as c:
            r = c.get(
                f"{BASE}/backlinks/summary",
                headers={"Authorization": f"Token {api_key}"},
                params={
                    "apikey": api_key,
                    "target": domain,
                    "mode": "domain",
                    "output": "json",
                },
            )
            r.raise_for_status()
            data = r.json()

        summary_list = data.get("summary", [])
        if summary_list:
            s = summary_list[0]
            print(json.dumps({
                "domain": domain,
                "domain_rating": s.get("domain_inlink_rank"),
                "backlinks": s.get("backlinks"),
                "referring_domains": s.get("referring_domains"),
            }))
        else:
            print(json.dumps({"domain": domain, "domain_rating": None, "backlinks": 0}))
    else:
        print(json.dumps({"error": f"Unknown action: {action}"}))

except Exception as e:
    print(json.dumps({"error": str(e)}))
