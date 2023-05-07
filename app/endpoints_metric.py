from prometheus_client import start_http_server, Counter, Gauge, Histogram
import re
from datetime import datetime
import os
# start_http_server(8601)
# Define Prometheus metrics
num_errors = Counter('num_errors', 'Number of ERROR messages')
num_info = Counter('num_info', 'Number of INFO messages')
num_warning = Counter('num_warning', 'Number of WARNING messages')
func_execution_time = Histogram('func_execution_time', 'Time taken to execute each function', ['function_name'])
common_errors = Counter('common_errors', 'Most common errors', ['error_type'])
# log_messages_per_module = Counter('log_messages_per_module', 'Distribution of log messages across different modules', ['filename'])
# avg_log_messages_per_module = Gauge('avg_log_messages_per_module', 'Average number of log messages per module', ['filename'])
# log_messages_per_function = Counter('log_messages_per_function', 'Number of log messages per function', ['function_name'])
# Open the log file
def metrics(): 
    print(os.getcwd())  
    with open('logs.log', 'r') as f:
        

        log_contents = f.read()
            
        # Remove escape sequences from the log file    
        log_contents = re.sub(r'\x1b\[\d+;\d+m', '', log_contents)
        
        # Split the log file into lines and remove empty lines
        log_lines = [line.split('\x1b[0m')[0] for line in log_contents.split('\n')]
        log_lines = [line for line in log_lines if line.strip()]
        
        # Parse the log data and insert it into the database
        for line in log_lines:
            my_string = line
            timestamp = my_string.split('/')[1].strip()     
            filename = my_string.split('/')[2].strip()   
            log_level = my_string.split('/')[3].strip()
            function_name = my_string.split('/')[4].strip()
            message = my_string.split('/')[5].strip()
            line_number = my_string.split('/')[7].strip().rstrip('/')
            load_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S,%f')
            if log_level == 'ERROR':
                num_errors.inc()
                # Add the error type to the common_errors metric
                common_errors.labels(error_type=message).inc()
            elif log_level == 'INFO':
                num_info.inc()
            elif log_level == 'WARNING':
                num_warning.inc()  
                    # Record the execution time for the function
            if function_name and message.startswith('Finished execution'):
                execution_time = float(message.split()[-2])
                func_execution_time.labels(function_name).observe(execution_time)
            
            # # Record the number of log messages for the module and function
            # log_messages_per_module.labels(filename).inc()
            # log_messages_per_function.labels(function_name).inc()

            # Calculate the average number of log messages per module
            # avg_log_messages = {}
            # for module, count in log_messages_per_module.collect()[0].samples:
            #     avg_log_messages[module] = count / len(log_messages_per_module.labels._buckets[0]._value._value)
            # avg_log_messages_per_module.set(avg_log_messages)
                 
            return function_name, filename
        
def summary():
    return "Logs Analysis."
