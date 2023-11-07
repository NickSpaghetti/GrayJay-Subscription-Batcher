import json
from pathlib import Path
import argparse

def main():
    args = setup_args()
    file_name = args.source
    text = ""
    with open(file_name, "r+") as f:
        text = json.loads(f.read())

    subs =  text["subscriptions"]
    subFileCount = 1
    bathSize = args.batchSize
    outputFilePath = args.outDir
    Path(outputFilePath).mkdir(parents=True,exist_ok=True)
    subBatchs = [subs[i:i+bathSize] for i in range(0,len(subs),bathSize)]
    for subBatch in subBatchs:
        with open(rf"{outputFilePath}\subFile_{subFileCount}.json", "w") as f:
            newPipeSub = {
                        "app_version": text["app_version"],
                        "app_version_int": text["app_version_int"],
                        "subscriptions": subBatch
                }
            json.dump(newPipeSub,f,indent=4)
        subFileCount += 1

def setup_args():
    parser = argparse.ArgumentParser(description='Batch newpipe subscription json output')
    parser.add_argument('-s','--source',type=str,
                        help='source file location for the newpipe json file',required=True)
    
    parser.add_argument('-o','--outDir',type=str,
                    help='output file directory where you want the batch files to live',required=True)
    
    parser.add_argument("-b","--batchSize",type=int,choices=(range(1,100)),required=False,default=99,
                        help="the amount of subscriptions in each file")

    return parser.parse_args()
        

if __name__ == "__main__":
    main()
