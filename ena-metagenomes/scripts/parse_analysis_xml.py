# https://www.ebi.ac.uk/ena/browser/api/xml/ERZ1749185

import os
import xmltodict
import json
from collections import defaultdict

field_counts = defaultdict(int)

out = open("data/tsv/analyses.tsv", "w")
fields = ["analysis_id", "title", "name", "type", "coverage", "program", "platform", "mol_type", "tpa", "run_id", "sample_id", "study_id", "biosample_id", "bioproject_id", "ftp"]
out.write("\t".join(fields)+"\n")

for index, file in enumerate(os.listdir("data/xml/analyses")):
    
    if not index % 1000: 
        print(index)
        
    info = {}
    path = os.path.join("data/xml/analyses", file)
    data = xmltodict.parse(open(path).read())["ANALYSIS_SET"]["ANALYSIS"]
    
    print(data)
    quit()
    
    # skip records without an assembly
    if "SEQUENCE_ASSEMBLY" not in data["ANALYSIS_TYPE"].keys(): 
        continue
    
    info["analysis_id"] = file
    info["title"] = data["TITLE"]
    info["ftp"] = "ftp.sra.ebi.ac.uk/vol1/"+data["FILES"]["FILE"]["@filename"]
    
    if "RUN_REF" not in data:
        info["run_id"] = "None"
    elif isinstance(data["RUN_REF"], list):
        info["run_id"] = ",".join([_["@accession"] for _ in data["RUN_REF"]])
    else:
        info["run_id"] = data["RUN_REF"]["@accession"]
    
    info["sample_id"] = data["SAMPLE_REF"]["IDENTIFIERS"]["PRIMARY_ID"] if "SAMPLE_REF" in data else None
    info["study_id"] = data["STUDY_REF"]["IDENTIFIERS"]["PRIMARY_ID"] if "STUDY_REF" in data else None
    
    try: info["biosample_id"] = data["SAMPLE_REF"]["IDENTIFIERS"]["EXTERNAL_ID"]["#text"] 
    except: info["biosample_id"] = None    
    try: info["bioproject_id"] = data["STUDY_REF"]["IDENTIFIERS"]["SECONDARY_ID"] 
    except: info["bioproject_id"] = None
    info.update(data["ANALYSIS_TYPE"]["SEQUENCE_ASSEMBLY"])
    info =  {k.lower(): v for k, v in info.items()}

    rec = [str(info[f]) if f in info else "None" for f in fields]
    out.write("\t".join(rec)+"\n")
