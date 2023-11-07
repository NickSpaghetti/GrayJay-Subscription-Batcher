# GrayJay-Subscription-Batcher
Batches subscription json file output from new pipe to GrayJay app

# How to use
1. Open up newpipe app on your android phone.
2. Go to Subscriptions on the accordian.
3. Click the 3 dots then Export to File.
4. Move the file to the device you are running the python script on.
5. Run the following command make sure to change the --source and --outDir flags.  --outDir will create the directory if it does not exist. `python3 <PathTo..\newpipe_subscription_splitter.py> --source "Path To Downloaded newpipe_subscriptions.json file from step 3. --outdir "Your desired output directory"`
