def get_sample_log_data():
  #generates sample log data for demonstration.
  return [
    {"timestamp":"2025-07-18 12:00", "message":"Server started"},
    {"timestamp":"2025-07-18 12:01", "message":"User logged in"},
    #add more sample log
  ]

def get_sample_genome_data():
  #provides sample DNA sequences for demonstration.
  return ["AGGCTA","CGTAAC","TTAGGC"]

def get_sample_stock_data():
  #sample stock prices for demonstration.
  return [
    {"day":"Monday", "price":150},
    {"day":"Tuesday", "price":155},
    {"day":"Wednesday", "price":145},
    #Add more sample stock data
  ]


def streaming_log_processing():
    
    log_data = get_sample_log_data()

    #use lambda functions to format log message
    format_log = lambda log: f"[{log['timestamp']}]:{log['message']}"

    #formatting and printing each log message
    formatted_logs = [format_log(log) for log in log_data]
    return formatted_logs

#running the stream log processing and printing the results
formatted_logs = streaming_log_processing()
formatted_logs
   
