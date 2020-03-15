# RON 

This code uses the huggingface library for the Real Or Not? NLP with disaster tweets 
 https://www.kaggle.com/c/nlp-getting-started/overview
 
 ## Requirement

Install transformers library from
https://github.com/huggingface/transformers

## Basic Usage

### Step 1
In ron.py  set <br/>
 RUN_TYPE = "command_line" :  to specify options from the command line 

 RUN_TYPE = "config_file" : to specify options in a config_file.


### Step 2 
 to run  from the command line: <br/>
```bash
export DATA_DIR=data/
export LOG_DIR=logs/
export OUTPUT_DIR=output/
export MODEL_TYPE=flaubert 
export MODEl_NAME_OR_PATH=flaubert-base-uncased
export TASK_NAME=ron

python ron.py   --model_type $MODEL_TYPE  --model_name_or_path $MODEl_NAME_OR_PATH  --data_dir $DATA_DIR   --output_dir $OUTPUT_DIR --log_dir $LOG_DIR --task_name $TASK_NAME  --do_train   --do_eval --evaluate_during_training

```

#### Example

to run using config_file:<br/>
```bash
python ron.py --config_file /path/to/config_file
```



