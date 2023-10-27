from rumours import *

# non-rumours
claim_count = 0

for event in events:
    for source_tid in os.listdir(f"{root}/{event}/non-rumours/"):

        if source_tid != ".DS_Store":
            text, time = extract_information(source_tid, 'non-rumours')

            data[f"N_{claim_count}"] = {
                "info": {
                    f"{source_tid}": {
                        "text": text,
                        "time": time
                    }
                },

                "label": 0
            }

            data_ids[f"R_{claim_count}"] = {
                "eid": f"R_{claim_count}",
                "post_ids": [source_tid]
            }

            for claim_file in os.listdir(f"{root}/{event}/non-rumours/{source_tid}/reactions"):
                data_ids[f"R_{claim_count}"]["post_ids"].append(claim_file[0:-5])
                text, time = extract_information_from_comment_file(source_tid, claim_file, 'non-rumours')
                data[f"N_{claim_count}"]["info"][f"{claim_file[0:-5]}"] = {
                    "text": text,
                    "time": time
                }

        claim_count += 1