#switch_by_ingest_format
inPathVideo = None
inPathAudio = None

#switch_by_output_target
outPath = None

#static_by_author
readDef = None
writeDef = None

#init_main_live_code
keptVideo = open(inPathVideo, readDef)
keptAudio = open(inPathAudio, readDef)
unionOutput = open(outPath, writeDef)

#perform merge on timeline data?

#save output