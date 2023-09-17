import json
import yfinance as yf

from datetime import datetime, timedelta
from kafka import KafkaProducer

def fetch(company_symbol):
    current_date = datetime.now()
    end_date = current_date - timedelta(days=1)

    data = yf.download(
        tickers=company_symbol,
        start=current_date - timedelta(days=7),
        end=end_date,
        interval='1m'
    )
    
    return data

def produce(data, topic_name, producer, company_symbol):
    if not data.empty:
        last_row = data.iloc[-1].to_dict()
        last_row['Datetime'] = data.index[-1].strftime('%Y-%m-%d %H:%M:%S') 
        last_row['Symbol'] = company_symbol
        msg = json.dumps(last_row)
        
        producer.send(topic_name, value=msg.encode())
        producer.flush()
        
        print(f"Producing data for {company_symbol} to {topic_name}\n")
        
    else:
        print(f"No data available for {company_symbol}")


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    topic_name = 'stocks'
    companies = ['TSLA', 'GOOG', 'AAPL', 'MSFT']
    
    while True:
        for company_symbol in companies:
            stock_data = fetch(company_symbol)
            produce(stock_data, topic_name, producer, company_symbol) 
